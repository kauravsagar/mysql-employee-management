import pymysql

def execute_sql(sql, *data):

    connection = pymysql.connect(host='localhost',
                             user='demo',
                             password='password',
                             db='employees_records',
                             cursorclass=pymysql.cursors.DictCursor
                             )
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, data)
            connection.commit()
            return cursor
    except Exception:
        print('something went wrong.')
    finally:
        connection.close()


def add(first_name, last_name, email, age):
    sql = "INSERT INTO employees values(NULL, %s, %s, %s, %s)"
    data =  execute_sql(sql, first_name, last_name, email, age) 
    if data:
        print('added successfully. Employee id is: {}'. format(data.lastrowid))
    else:
        print('unable to add user.')

def delete(employee_id):
    sql = "DELETE FROM employees WHERE id = %s"
    if execute_sql(sql, employee_id):
        print('employee deleted successfully')
    else:
        print('unable to delete user')

def update(employee_id, first_name, last_name, email, age):
    sql = "UPDATE employees SET first_name=%s, last_name=%s, email=%s, age=%s where id = %s"
    if execute_sql(sql, first_name, last_name, email, age, employee_id):
        print('updated successfully')
    else:
        print('unable to update.')

def show(employee_id):
    sql = "SELECT * FROM employees where id = %s"
    employee = execute_sql(sql, employee_id).fetchone()
    if employee is None:
        print('Employee not found.')
    else:
        print('First name: {}'.format(employee['first_name']))
        print('Last name: {}'.format(employee['last_name']))
        print('Email: {}'.format(employee['email']))
        print('Age: {}'.format(employee['age']))
    
while True:
    print('1> Add employyee')
    print('2> Show employee')
    print('3> Update employee')
    print('4> Delete employee')
    print('5> Exit')
    print('Choose any options: ', end='')
    user_input = int(input())
    if user_input == 1:
        print('Enter first name: ', end='')
        first_name  = input()
        print('Enter last name: ', end='')
        last_name = input()
        print('Enter email address: ', end='')
        email = input()
        print('Enter age: ', end='')
        age = int(input())
        add(first_name, last_name, email, age)
    elif user_input == 2:
        print('Enter employee id: ', end='')
        employee_id = int(input())
        show(employee_id)
    elif user_input == 3:
        print('Eneter employee id: ', end='')
        employee_id = int(input()) 
        print('Enter first name: ', end='')
        first_name  = input()
        print('Enter last name: ', end='')
        last_name = input()
        print('Enter email address: ', end='')
        email = input()
        print('Enter age: ', end='')
        age = int(input())
        update(employee_id, first_name, last_name, email, age)
    elif user_input == 4:
        print('Enter employee id: ', end='')
        employee_id  = int(input())
        delete(employee_id)
    elif user_input == 5:
        break
    else:
        print('Wrong option please try again.')

print('Thank you!!!')

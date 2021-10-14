from models import db_connection
import pandas
import numpy

db = db_connection()
username = ''
password = ''
user_id = 0
def confirm_creds(username='',password=''):
    cursor = db.cursor()
    cursor.execute('use Account_manager')
    cursor.execute('SELECT * FROM accounts')
    data = cursor.fetchall()
    for d in data:
        if username in d and password in d:
            print(d[0])
            return d[0]
    return False


def go_too_data_records(user_id):
    print(user_id)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM saved_info WHERE accounts_id = '{user_id}' ")
    records = cursor.fetchall()
    data =pandas.read_sql_query(f"SELECT * FROM saved_info WHERE accounts_id = {user_id}",db)
    print(data)

def add_new_u_p(user_id):
    user1 = ''
    p1 = ''
    while len(user1) < 5 and len(p1) < 5:
        user1 = input('Username-> ')
        p1 = input('Password-> ')
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO saved_info(username,password,accounts_id) VALUES('{user1}','{p1}',{user_id})")
    db.commit()
    print('record infomation saved')

print('Welcome to your password accounts manager')
while confirm_creds(username,password) == False:
    print('Do you have an access account')
    account = input('y/n ').lower()
    print('Please enter your username')
    username = input('> ')

    print('Please enter your password')
    password = input('> ')
    user_id = confirm_creds(username,password)
    if confirm_creds(username,password) == False:
        print('wrong login credentials')

print(f'Welcome {username}')

while True:
    print('Pick an option you want to see')
    print('Add new username or password (A): Check your previous data records (B)')
    option = input('> ').upper()

    if option == 'A':
        add_new_u_p(user_id)
    elif option == 'B':
        go_too_data_records(user_id)




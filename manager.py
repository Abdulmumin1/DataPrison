import sys
import sqlite3

def create_table():
	db = sqlite3.connect('.database.db')
	statement = '''CREATE TABLE if not exists MANAGER
	(ID INTEGER PRIMARY KEY AUTOINCREMENT,
	WEBSITE TEXT NOT NULL,
	PASSWORD TEXT NOT NULL,
	EMAIL TEXT NOT NULL
	);
	'''
	cur = db.cursor()
	cur.execute(statement)
	db.close()


create_table()

def create_new_password():
	db = sqlite3.connect('.database.db')
	statement = '''INSERT INTO MANAGER(WEBSITE, PASSWORD, EMAIL)
	VALUES (?,?,?)
	'''
	website = input('Enter website name: ')
	password = input(f'Enter password for {website}: ')
	email = input(f'Enter email associated with {website}: ')
	cur = db.cursor()
	cur.execute(statement, (website, password, email))
	db.commit()
	db.close()
	print(f'password for {website} succsessfully created!')

def retrieve_password(website):
	db  = sqlite3.connect('.database.db')
	statement = 'SELECT password FROM MANAGER where WEBSITE = ?'
	cur = db.cursor()
	items = cur.execute(statement, (website,))
	password_list = [i for i in items]
	return f'password for {website} is {password_list[-1][0]}'

if len(sys.argv) > 1:
	if sys.argv[1] == 'new':
		create_new_password()
	else:
		print(retrieve_password(sys.argv[1]))
else:
	print('''Usage:
		manager.py new - to create a new password
		manager.py <website> - to retreive the website password
		''')


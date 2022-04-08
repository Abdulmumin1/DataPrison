import sys
import sqlite3


def create_table():
    db = sqlite3.connect('.database.db')
    statement = '''CREATE TABLE if not exists PASSWORDS
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


def get_all_entries():
    db = sqlite3.connect('.database.db')
    statement = 'SELECT website, password, id FROM PASSWORDS'
    cur = db.cursor()
    items_io = cur.execute(statement)
    item_lst = [i for i in items_io]
    return item_lst


def search_website(x):
    db = sqlite3.connect('.database.db')
    statement = 'SELECT website, password, id FROM PASSWORDS WHERE website Like ?'
    cur = db.cursor()
    items_io = cur.execute(statement, (x+'%',))
    item_lst = [i for i in items_io]
    return item_lst


def register_website(website, password, email):
    db = sqlite3.connect('.database.db')
    statement = '''INSERT INTO PASSWORDS(WEBSITE, PASSWORD, EMAIL)
	VALUES (?,?,?)
	'''
    statement2 = 'SELECT website, password, id FROM PASSWORDS WHERE website = ?'
    cur = db.cursor()
    cur.execute(statement, (website, password, email))
    datas = cur.execute(statement2, (website,))
    datas = [i for i in datas]
    db.commit()
    db.close()
    return datas[-1]


def delete_entry(id):
    db = sqlite3.connect('.database.db')
    statement = 'DELETE FROM PASSWORDS where id = ?'

    cur = db.cursor()
    cur.execute(statement, (id,))
    db.commit()
    db.close()
    return True


if __name__ == '__main__':

    pass

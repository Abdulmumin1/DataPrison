import sys
import sqlite3
import os,pyperclip
from pathlib import Path

home = Path.home()
full_path = os.path.join(home,'.Dataprison')
try:
    os.mkdir(full_path)
except:
    pass
database_path = os.path.join(full_path, '.database.db')
def create_table():
    db = sqlite3.connect(database_path)
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
    db = sqlite3.connect(database_path)
    statement = 'SELECT website, password, id, email FROM PASSWORDS'
    cur = db.cursor()
    items_io = cur.execute(statement)
    item_lst = [i for i in items_io]
    return item_lst


def search_website(x):
    db = sqlite3.connect(database_path)
    statement = 'SELECT website, password, id, email FROM PASSWORDS WHERE website Like ?'
    cur = db.cursor()
    items_io = cur.execute(statement, (x+'%',))
    item_lst = [i for i in items_io]
    return item_lst


def register_website(website, password, email):
    db = sqlite3.connect(database_path)
    statement = '''INSERT INTO PASSWORDS(WEBSITE, PASSWORD, EMAIL)
	VALUES (?,?,?)
	'''
    statement2 = 'SELECT website, password, id, email FROM PASSWORDS WHERE website = ?'
    cur = db.cursor()
    cur.execute(statement, (website, password, email))
    datas = cur.execute(statement2, (website,))
    datas = [i for i in datas]
    db.commit()
    db.close()
    return datas[-1]


def delete_entry(id):
    db = sqlite3.connect(database_path)
    statement = 'DELETE FROM PASSWORDS where id = ?'

    cur = db.cursor()
    cur.execute(statement, (id,))
    db.commit()
    db.close()
    return True

def commandline_search(x):
    entries = search_website(x)
    index = 1
    which = None
    if not entries:
        print('Not found!')
        return
    if len(entries) < 2:
        which = 0
    else:
        for entry in entries:
            print(f"{index}. {entry[0]}")
            index += 1
        try:    
            inp = int(input('Enter number: '))
            which = inp
        except:
            print('Enter index.')
    num = entries[which-1]
    key = num[1]
    pyperclip.copy(key)
    print(f"key for {num[0]} copied.")

# def run():
#     if len(sys.argv) > 1:
#         if sys.argv[1] == 'new':
#             create_new_password()
#         else:
#             print(search_website(sys.argv[1]))
#     # else:
#     #     print('Usage: \n\tmanager.py new - create a new password \n\tmanager.py <website> recover password for that website')


if __name__ == '__main__':
    # for i in range(0, 10):
    #     register_website(f"dummy{i}", f"password{i}", "email@fake.com")
    commandline_search()
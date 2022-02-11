import sqlite3
import mysql.connector

cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')

cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()



cnx.close()

#
# conn = sqlite3.connect('example.sqlite')
#
# c = conn.cursor()
#
# def zapis_do_bazy():
#     c.execute('''CREATE TABLE transakcje
#                 (data TEXT, id INTEGER, cena REAL)''')
#     c.execute('''INSERT INTO transakcje VALUES
#                 ('2022-02-11',12,19.99)''')
#     c.execute('''INSERT INTO transakcje VALUES
#                 ('2022-02-10',11,44.99)''')
#     conn.commit()
#
#
# for row in c.execute('SELECT * FROM transakcje ORDER BY cena'):
#     print(row)
#
#
# conn.close()
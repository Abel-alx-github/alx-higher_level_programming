#!/usr/bin/python3
""" module that connect ot detabase and fetchall states start with 'N'"""


import sys
import MySQLdb


if __name__ == '__main__':
    mydb = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3], port=3306)

    my_cursor = mydb.cursor()

    sql = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    name = sys.argv[4]
    my_cursor.execute(sql, (name,))

    all_states = my_cursor.fetchall()
    for each in all_states:
        print(each)

    my_cursor.close()
    mydb.close()

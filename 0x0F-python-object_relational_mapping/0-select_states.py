#!/usr/bin/python3
import MySQLdb
import sys

"""A script that lists rows from a sql database"""
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user='root',
    passwd='root/root',
    db='hbtn_0e_0_usa')

"""creating a cursor object"""
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")

"""fetches rows in the table"""
rows = cur.fetchall()

"""display rows in database"""
for row in rows:
    print(row)


"""closing the cusor and db connection"""
cur.close()
db.close()

#!/usr/bin/python3
"""searches a state name as given in an argument"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]

    """connecting to a MySQL database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()

    query_search = "SELECT * FROM states WHERE name\
            LIKE '{}' ORDER BY id ASC".format(argv[4])
    cur.execute(query_search)
    query_result = cur.fetchall()

    for row in query_result:
        if (row[1] == argv[4]):
            print(row)

    cur.close()
    db.close()

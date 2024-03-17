#!/usr/bin/python3
"""A query to recieve all records from MySQL state talbe"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]

    try:
        db_connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database)
    except MySQLdb.Error as err:
        print("Error: {}".format(err))
        exit(1)

    cur = db_connection.cursor()

    """retriving record from state database"""
    try:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_db = cur.fetchall()
    except MySQLdb.Error as err:
        print("Error executing query: {}".format(err))
        cur.close()
        db_connection.close()
        exit(1)

    for row in query_db:
        print(row)

    cur.close()
    db_connection.close()

#!/usr/bin/python3
"""A module to retrive elements from a table starting with letter N"""
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
        state_id, nameOfstate = row[0], row[1]
        if nameOfstate.startswith("N"):
            print("({}, '{}')".format(state_id, nameOfstate))

    cur.close()
    db_connection.close()

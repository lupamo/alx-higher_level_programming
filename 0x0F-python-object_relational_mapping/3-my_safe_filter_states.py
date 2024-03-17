#!/usr/bin/python3
"""
searches a state name as given in an argument but is
not prompt to sql injection
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    """connecting to a MySQL database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()

    query_search = "SELECT * FROM states WHERE name = % sORDER BY id ASC"

    cur.execute(query_search, (state_name,))
    query_result = cur.fetchall()

    for row in query_result:
        print(row)

    cur.close()
    db.close()

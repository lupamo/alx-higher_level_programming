#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]

    """connecting to a MySQL database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()

    query_search = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
    cur.execute(query_search)
    query_result = cur.fetchall()

    for row in query_result:
        print(row)

    cur.close()
    db.close()

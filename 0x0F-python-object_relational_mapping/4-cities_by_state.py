#!/usr/bin/python3
"""The module joins cities Table with states"""
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    """connecting to a MySQL database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    query_result = cur.fetchall()

    for row in query_result:
        print(row)

    cur.close()
    db.close()

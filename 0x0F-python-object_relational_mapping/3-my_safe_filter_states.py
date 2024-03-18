#!/usr/bin/python3
"""
searches a state name as given in an argument but is
not prompt to sql injection
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    try:
        """connecting to a MySQL database"""
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cur = db.cursor()
        state_name_esc = MySQLdb.escape_string(state_name)

        """Executing query"""
        query_search = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        cur.execute(query_search, (state_name_esc,))
        query_result = cur.fetchall()

        for row in query_result:
            print(row)
    except:
        MySQLdb.Error as err:
            print("Error: {}".format(err))

        cur.close()
        db.close()

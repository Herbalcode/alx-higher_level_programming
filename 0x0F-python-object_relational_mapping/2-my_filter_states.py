#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

if __name__=="__main__":

    import MySQLdb
    from sys import argv


    conn = MySQLdb.connect(host="localhost", 
            port=3306, 
            user=argv[1], 
            passwd=argv[2], 
            db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM tables WHERE BINARY name='{}' ORDER BY id ASC" .format(argv[4]))
    query_raws = cur.fetchall()
    for raw in query_raws:
        print(raws)
    cur.close()
    conn.close()


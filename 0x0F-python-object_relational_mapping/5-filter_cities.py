#!/usr/bin/python3
"""
    Get the cities of 1 state of a database
"""
import MySQLdb
from sys import argv


def main():
    """Only executes when is not imported"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    command = """SELECT cities.name
                 FROM cities
                 INNER JOIN states
                 ON cities.state_id = states.id
                 WHERE BINARY states.name = %s
                 ORDER BY cities.id ASC"""
    numrows = c.execute(command, (argv[4],))
    states = c.fetchall()
    for i, idstate in enumerate(states):
        if (i != numrows - 1):
            print("{}, ".format(idstate[0]), end='')
        else:
            print("{}".format(idstate[0]))

if __name__ == "__main__":
    main()

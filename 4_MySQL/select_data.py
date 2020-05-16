import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')

    query = 'SELECT COUNT(DISTINCT state) FROM students'

    cursor = conn.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    print("Total Results :", len(students))
    for s in students:
        print(s[0])
except mysql.connector.Error as error:
    print("Error :", error)
finally:
    if(conn.is_connected()):
        conn.close()

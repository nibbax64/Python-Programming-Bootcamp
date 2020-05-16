import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')
    cursor = conn.cursor()

    query = 'SELECT students.first_name, students.last_name, scores.test_id, scores.score FROM students INNER JOIN scores ON students.student_id = scores.student_id WHERE scores.score <= 15 ORDER BY scores.test_id'
    cursor.execute(query)

    results = cursor.fetchall()
    for x in results:
        print(x[0], " ", x[1], " ", x[2], " ", x[3])


except mysql.connector.Error as error:
    print("Error :", error)
finally:
    if(conn.is_connected()):
        conn.close()

import mysql.connector

db1 = mysql.connector.connect(host = 'localhost' , user = 'root', password = 'batman@2003',database= 'student')
cur = db1.cursor()
student_name = 'dharampal'
query = "SELECT * FROM details WHERE name = %s"
cur.execute(query, (student_name,))
results = cur.fetchall()

# Display the student details
if results:
    for row in results:
        print("Name:", row[0])
        print("Roll No:", row[1])
        print("Marks:", row[2])
else:
    print("No student found with that name.")
db1.commit()
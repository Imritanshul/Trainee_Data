import mysql.connector

db1 = mysql.connector.connect(host = 'localhost' , user = 'root', password = 'batman@2003',database= 'student')
cur = db1.cursor()
s = 'insert into details values(1,"jeevan",90)'
cur.execute(s)
db1.commit()
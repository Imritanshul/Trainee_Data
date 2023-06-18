import mysql.connector

db1 = mysql.connector.connect(host = 'localhost' , user = 'root', password = 'batman@2003')
print('connection succesful')
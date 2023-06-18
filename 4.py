import mysql.connector

db1 = mysql.connector.connect(host = 'localhost' , user = 'root', password = 'batman@2003')
cur = db1.cursor()
cur.execute('create database student')
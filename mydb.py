import mysql.connector

# con=mysql.connector.connect(user="root",password="ROOT",host="localhost")
# print(con)
#
# #cursor object for executing sql queries
#
# c=con.cursor()
# query="create database school2"
#
# c.execute(query)
# print("Database created")

con=mysql.connector.connect(user="root",password="ROOT",host="localhost",database="school")

c=con.cursor()
query=("create table students(Rollno int,Name varchar(20),Age int,Place varchar(20),Mark int)");
c.execute(query)

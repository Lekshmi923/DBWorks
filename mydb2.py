#create new record/insert data into database table student

import mysql.connector
con=mysql.connector.connect(user="root",password="ROOT",host="localhost",database="school")

print(con)
c=con.cursor()

# query="insert into students(Rollno,Name,Age,Place,Mark) values(%s,%s,%s,%s,%s)"
# data=(11,"Arun",19,"Ekm",45)
# query="insert into students(Rollno,Name,Age,Place,Mark) values(%s,%s,%s,%s,%s)"
# data=(12,"Edwin",20,"TVM",42)
query="insert into students(Rollno,Name,Age,Place,Mark) values(%s,%s,%s,%s,%s)"
data=(15,"Emilin",22,"Kollam",46)
c.execute(query,data)
con.commit()   #permanently saves data in to database

print("Inserted data successfully")
c.close()
con.close()

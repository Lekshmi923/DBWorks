import mysql.connector

con=mysql.connector.connect(user="root",password="ROOT",host="localhost",database="school")

print(con)
c=con.cursor()

query="select * from students where Rollno=%s"
data=(12,)
c.execute(query,data)
record=c.fetchone()

if record:
    print(record)
else:
    print("No record found")

c.close()
con.close()
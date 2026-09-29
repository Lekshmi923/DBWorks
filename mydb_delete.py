import mysql.connector

con=mysql.connector.connect(user="root",password="ROOT",host="localhost",database="school")
print(con)

c=con.cursor()

query="delete from students where Rollno=%s"
data=(5,)
c.execute(query,data)
con.commit()

if c.rowcount>0:
    print("Data is deleted")
else:
    print("no record found")

c.close()
con.close()



import mysql.connector

con=mysql.connector.connect(user="root",password="ROOT",host="localhost",database="school")
print(con)

c=con.cursor()

query="update students set Mark=%s where Rollno=%s"
data=(38,15)
c.execute(query,data)
con.commit()

print("Updated successfully")
c.close()
con.close()
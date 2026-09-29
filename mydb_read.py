import mysql.connector
con=mysql.connector.connect(user="root",password="ROOT",host="localhost",database="school")

print(con)
c=con.cursor()

query="select * from students" #read all record from the table
c.execute(query)

records=c.fetchall()    #retrieves all the records in the table
if records:
    for row in records:
        print(row)
else:
    print("No records found")

c.close()
con.close()
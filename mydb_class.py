#define  a class to perform database operations on a book table.
#create a class named BooklistCreateRetrieveUpdateDelete with methods
# list() for reading all records
# create() for creating records
# retrieve() for reading a specific record
# update()
# delete()

import mysql.connector

class BooklistCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con = mysql.connector.connect(user="root", password="ROOT", host="localhost", database="library_db")
        print(self.con)
        self.c=self.con.cursor()
        print("Succesfully connected")


    def list(self):
        query = "select * from book"  # read all record from the table
        self.c.execute(query)

        records = self.c.fetchall()  # retrieves all the records in the table
        if records:
            for row in records:
                print(row)
        else:
            print("No records found")

    def create(self,id,title,author,price,language,page):
        query = "insert into book(id,title,author,price,language,page) values(%s,%s,%s,%s,%s,%s)"
        data = (id,title,author,price,language,page)
        self.c.execute(query, data)
        self.con.commit()  # permanently saves data in to database

        print("Inserted data successfully")

    def retrieve(self,id):
        query = "select * from book where id=%s"
        data = (id,)
        self.c.execute(query, data)
        record = self.c.fetchone()

        if record:
            print(record)
        else:
            print("No record found")

    def update(self,id,title,author,price,language,page):
        query = "update book set title=%s,author=%s,price=%s,language=%s,page=%s where id=%s"
        data = (title,author,price,language,page,id)
        self.c.execute(query, data)
        self.con.commit()

        print("Updated successfully")

    def delete(self,id):
        query = "delete from book where id=%s"
        data = (id,)
        self.c.execute(query, data)
        self.con.commit()

        if self.c.rowcount > 0:
            print("Data is deleted")
        else:
            print("no record found")

book_instance=BooklistCreateRetrieveUpdateDelete()
book_instance.list()
# book_instance.create(3,"Secret History","Donna Tartt",800,"English",600)
# book_instance.create(2,"A Little Life","Hanya Yanagihara",750,"English",800)
book_instance.retrieve(1)
book_instance.update(1,"Tuesdays with Morrie","Mitch Albom",300,"English",200)
book_instance.delete(6)

#define  a class to perform database operations on a vehicle table.
#create a class named VehiclelistCreateRetrieveUpdateDelete with methods
# list() for reading all records
# create()   for creating records
# retrieve() for reading a specific record
# update()
# delete()


import mysql.connector
class VehiclelistCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con = mysql.connector.connect(user="root", password="ROOT", host="localhost", database="vehicle_db")
        print(self.con)
        self.c = self.con.cursor()
        print("Succesfully connected")

    def list(self):
        query="select * from vehicle"
        self.c.execute(query)

        records=self.c.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records found")


    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year)values(%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.c.execute(query,data)
        self.con.commit()
        print("Data inserted successfully")


    def retrieve(self,id):
        query="select * from vehicle where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record = self.c.fetchone()

        if record:
            print(record)
        else:
            print("No record found")


    def update(self,id,brand,model,type,price,year):
        query = "update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data = (brand,model,type,price,year,id)
        self.c.execute(query,data)
        self.con.commit()

        print("Updated successfully")


    def delete(self,id):
        query = "delete from vehicle where id=%s"
        data = (id,)
        self.c.execute(query, data)
        self.con.commit()

        if self.c.rowcount > 0:
            print("Data is deleted")
        else:
            print("no record found")

v=VehiclelistCreateRetrieveUpdateDelete()
v.list()
v.create("BMW",'M5',"Sedan",8500000,2018)
v.create("MERCEDES",'Gwagon',"car",15000000,2015)
v.retrieve(1)
v.update(2,"audi","r8","car",7800000,2016)
v.delete(1)
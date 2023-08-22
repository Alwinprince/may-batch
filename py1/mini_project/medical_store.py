import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='Alwin@123',port=3306,database='project')
# print(mydb)

mycursur=mydb.cursor()
# mycursur.execute("create database project")
mycursur.execute("use project")
# create_store_table = "CREATE TABLE  stores (p_code int, p_name varchar(122),quantity int,price int)"
# mycursur.execute(create_store_table)
mydb.commit()

class admin:

    def add_medicine(self):
        code=int(input("enter the number:"))
        name=input("enter the name:")
        quantity=int(input("enter the qty:"))
        price=int(input("enter the price:"))
        sql="insert into  stores (p_code,p_name,quantity,price)values(%s,%s,%s,%s)"
        values=(code,name,quantity,price)
        mycursur.execute(sql,values)
        mydb.commit()

    def show_medicine(self):
        select_query = "SELECT * FROM medicine ORDER BY item_no"  # Add ORDER BY clause
        mycursur.execute(select_query)
        medicines = mycursur.fetchall()

        if not medicines:
            print("No medicine records found.")
        else:
            print("Medicine records:")
            for medicine in medicines:
                print("p_code:", medicine[0])
                print("p_namer:", medicine[1])

                print("-----------------------")
p=admin()
p.add_medicine()1
p.show_medicine()






















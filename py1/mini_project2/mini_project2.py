import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Alwin@123',port=3306,database='project')
# print(mydb)

mycursur=mydb.cursor()
mycursur.execute("create database project")
mycursur.execute("use project")
# # create_store_table = "CREATE TABLE  stores (p_code int, p_name varchar(122),quantity int,price int)"
# # mycursur.execute(create_store_table)
# mydb.commit()
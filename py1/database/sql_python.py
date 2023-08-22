import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='Alwin@123',port=3306)
print(mydb)

mycursur=mydb.cursor()
# mycursur.execute("create database maypython")
mycursur.execute("use maypython")
# mycursur.execute("create table students(name varchar(250),age int,rollnum int)")
sql="insert into students(name,age,rollnum)values(%s,%s,%s)"
val=("alwin",13,7)
val=("jithu",12,3)
mycursur.execute(sql,val)
mydb.commit()


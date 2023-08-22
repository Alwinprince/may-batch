import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alwin@123",
    port="3306"
)
# print(my_db)
my_cursur = my_db.cursor()
# my_cursur.execute("use medical_1")
my_cursur.execute("create table apollo_store(Item_no INT, P_Name VARCHAR(100), Price INT, quantity INT , medicine_type VARCHAR(100)")



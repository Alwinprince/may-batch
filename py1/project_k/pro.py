import mysql.connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alwin@123",
    port="3306"
)
my_cursur = my_db.cursor()
my_cursur.execute("create database medical_store")










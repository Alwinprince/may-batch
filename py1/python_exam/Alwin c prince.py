class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_details(self):
        print("The title name is:", self.title, "author is:", self.author, "price is:", self.price)


class fic(Book):
    def __init__(self, title, author, price, category):
        self.category = category
        super().__init__(title, author, price)
    def get_details(self):
        print("The title name is:", self.title, "author is:", self.author, "price is:", self.price,'category:',self.category)


class nonfic(Book):
    def __init__(self, title, author, price, category):
        self.category = category
        super().__init__(title, author, price,)
    def get_details(self):
        print("The title name is:", self.title, "author is:", self.author, "price is:", self.price,'category:',self.category)

class poetry(Book):
    def __init__(self, title, author, price, category):
        self.category = category
        super().__init__(title, author, price)

    def get_details(self):
        print("The title name is:", self.title, "author is:", self.author, "price is:", self.price, 'category:',
              self.category)


obj = fic("life of pie", "yann martel", "300", "hd")
obj.get_details()
obj2 = nonfic("bahubali", "rajamouli", "500","mhvbdj")
obj2.get_details()
obj3 = poetry("leeaves of grass", "cummings", "550","hr" )
obj3.get_details()

#
#
#
# """"
# employee management system;
# ------------
#
# class hR:
# 1. add employeees
#    emp_id,name,department,place,salary(private)
#
#  store gthge data into csvfile.
# 2. list employye deatils
#   fetch from csv file
#
# class employee
#
# 1.filter the employee
#
#
# """
#
#
#
# import csv
# class Hr:
#     def add_employee(self):
#         emp_id=input("ENTER THE EMPLOYEE ID:")
#         name=input("ENTER THE NAME:")
#         department=input("ENTER THE DEPARTMENT OF EMPLOYEE:")
#         place=input("ENTER THE POSTING LOCATION:")
#         __salary=input("ENTER THE SALARY OF EMPLOYEE:")
#         data={"emp_id":emp_id,"name":name,"department":department,"place":place,"salary":__salary}
#         with open("emp_data.csv",'a',newline='')as csvfile:
#             header = ["emp_id", 'name', "department", "place", "salary"]
#             csv_writter=csv.DictWriter(csvfile,fieldnames=header)
#             if csvfile.tell()==0:
#                 csv_writter.writeheader()
#             csv_writter.writerow(data)
#             print("DATA UPDATED TO DATA BASE")
#     def emp_details(self):
#         emp_id=input("enter the empid:")
#         with open('emp_data.csv',"r",newline="") as csvfile:
#             cs=csv.DictReader(csvfile)
#             for line in cs:
#                 if line["emp_id"]==emp_id:
#                     print("empname:",line["name"],"location:",line['place'])
#                     return
#                 else:
#                     print("not found")
#                     break
#
#
#
# hr=Hr()
# # hr.add_employee()
# hr.emp_details()
#
# import csv
# import csv as c
# import os
#
#
# class HR:
#     def _init_(self, id, name, department, place, salary):
#         self.id = id
#         self.name = name
#         self.department = department
#         self.place = place
#         self.salary = salary
#
#     def insert(self):
#         file_exists = os.path.isfile("em_det.csv")
#         with open("em_det.csv", "a", newline="") as details:
#             heads = ["id", "name", "department", "place", "salary"]
#             file = c.DictWriter(details, fieldnames=heads)
#
#             if not file_exists:
#                 file.writeheader()
#
#             file.writerow({"id": self.id, "name": self.name, "department": self.department, "place": self.place,
#                            "salary": self.salary})
#
#     def update(self):
#
#         with open("em_det.csv", "r") as file:
#             employee = list(csv.DictReader(file))
#
#             id = input("enter id  again to confirmation.......")
#             for i in employee:
#                 if i["id"] == id:
#                     i["name"] = self.name
#                     i["department"] = self.department
#                     i["place"] = self.place
#                     i["salary"] = self.salary
#                     # print(employee)
#         with open("em_det.csv", "w") as details:
#             heads = ["id", "name", "department", "place", "salary"]
#             emp = csv.DictWriter(details, fieldnames=heads)
#             emp.writeheader()
#             for i in employee:
#                 # print(i)
#                 emp.writerow(i)
#             print('your data successfully updated...')
#
#
# def insertion(id, name, dept, place, salary):
#     obj = HR(id, name, dept, place, salary)
#     obj.insert()
#     print('your data successfully inserted...')
#
#
# def upd():
#     id = input("enter the id to update")
#     name = input("enter name to update/otherwise write old name")
#     department = input("enter department to update/otherwise write old dprtmnt")
#     place = input("enter place to update/otherwise write old place")
#     salary = input("enter salary to update/otherwise write old salary")
#
#     obj = HR(id, name, department, place, salary)
#     obj.update()
#
#
# def view():
#     with open("em_det.csv", "r") as file:
#         reader = c.DictReader(file)
#         for i in reader:
#             print("id:", i["id"], "name:", i["name"], "department:", i["department"], "place:", i["place"], "salary:",
#                   i["salary"])
#
#
#
# def delete():
#     id = input('Enter the id to delete ')
#     with open("em_det.csv") as file:
#         emp = list(csv.DictReader(file))
#         for i in emp:
#             if i["id"] == id:
#                 emp.remove(i)
#     file.close()
#     with open("em_det.csv", "w") as file:
#         heads = ["id", "name", "department", "place", "salary"]
#         employ = csv.DictWriter(file, fieldnames=heads)
#         employ.writeheader()
#
#         for i in emp:
#             employ.writerow(i)
#         print("data deleted successfuly.......")
#
#
#
#
#
# class Employee():
#     def init(self, id):
#         self.id = id
#
#     def view(id):
#         with open("em_det.csv", "r") as file:
#             reader = c.DictReader(file)
#             for i in reader:
#                 print("id:", i["id"], "name:", i["name"], "department:", i["department"], "place:", i["place"],
#                       "salary:", i["salary"])
#
#
# def mainHR():
#     print("1-insert")
#     print("2-View")
#     print("3-Delete")
#     print("4-Update")
#     choice = int(input("Enter the choice: "))
#
#     if choice == 1:
#         id = input("enter id")
#         name = input("Enter the name: ")
#         department = input("Enter department: ")
#         place = input("Enter place: ")
#         salary = input("Enter salary: ")
#         insertion(id, name, department, place, salary)
#         x = input("do you want to continue? (y/n)")
#         if x == "y":
#             mainHR()
#     if choice == 2:
#         view()
#
#         x = input("do you want to continue? (y/n)")
#         if x == "y":
#             mainHR()
#
#     if choice == 3:
#         delete()
#         x = input("do you want to continue? (y/n)")
#         if x == "y":
#             mainHR()
#
#     if choice == 4:
#         upd()
#         x = input("do you want to continue? (y/n)")
#         if x == "y":
#             mainHR()
#
#
# def mainEM():
#     selector = input('Enter your choice\n'
#                      '1 . View')
#     if selector == '1':
#         id = input('Enter your id :')
#         obj_view = Employee()
#         obj_view.view()
#     else:
#         print('Invalid option')
#
#
# def enter():
#     x = int(input('You want to join as\n1. HR\n2. Employee\nSelect from the above options :'))
#     if x == 1:
#         mainHR()
#     elif x == 2:
#         mainEM()
#     else:
#         print("enter valid choice")
#
# enter()

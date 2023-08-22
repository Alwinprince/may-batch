"""
inheritance

child class(derived class or sub class) inherits the property of parent class(super class or base class)
code reusability

*) types of  inheritance
1.single inheritance --------------(1 child 1 parent)
2.multiple inheritance-------------(1 child and min 2 parent)
3.multi level inheritance----------()
4.hierarchical inheritance---------(more than one child class is derived from a single parent)
5.hybrid inheritance---------------(combination of diffrent inheritance is called hybrid inheritance)
"""

# class Animal:
#     def _init_(self,name,category):
#         self.name=name
#         self.category=category
#
#     def func1(self):
#         print(self.name,self.category)
# class Dog(Animal):
#     def func2(self):
#         print(self.name,self.category)
#
# class Cat(Animal):
#     def func3(self):
#         print(self.name,self.category)
# obj=Animal("maika","pet")
# obj.func1()
# obj_dog=Dog("appu","pet")
# obj_dog.func1()

"""Multiple inheritance"""

# class Vehicle:
#     def fun1(self):
#         print("inside vehicle class")
#
# class Car:
#     def func2(self):
#         print("inside the car")
#
# class Sports_car(Vehicle,Car):
#     def func3(self):
#         print("inside the sports car")
#
# obj=Sports_car()
# obj.fun1()
# obj.func2()

"""multi level inheritance """
#
# class Vehicle:
#     def fun1(self):
#         print("inside vehicle class")
#
# class Car(Vehicle):
#     def fun2(self):
#         print("inside the car")
#
# class Sports_car(Car):
#     def fun3(self):
#         print("inside the sports car")
#
# obj=Sports_car()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# obj1=Car()
# obj1.fun1()
# obj2=Sports_car()
# obj2.fun1()
# obj2.fun2()
# obj2.fun3()


"""Hierarchical inheritance """

# class College:
#     def func1(self):
#         print("mggac")
#
# class Teacher(College):
#     def sindu(self,name):
#         print("head of department",name)
#
# class Student(College):
#     def sagil(self,name):
#         print("cs student",name)
#
# obj=Teacher()
# obj.func1()
# obj.sindu('sindu')
#
# obj1=Student()
# obj1.func1()
# obj1.sagil('sagil')


"""  Hybrid inheritance """
#
# class College:
#     def func1(self):
#         print("mggac")
#
# class Teacher(College):
#     def sindu(self,name):
#         print("head of department",name)
#
# class Student(College):
#     def sagil(self,name):
#         print("cs student",name)
#
# class Staff(Student,Teacher):
#     def staf(self,name):
#         print("staff name is ",name)
#
# obj=Staff()
# obj.sindu('vadivelu')
# obj1=Student()
# obj1.sagil('sarang')
#


"""
Create a class called Vehicle with the following attributes and methods:

Attributes:
make: a string representing the make of the vehicle
model: a string representing the model of the vehicle
year: an integer representing the year the vehicle was made
color: a string representing the color of the vehicle
mileage: a float representing the current mileage of the vehicle

Methods:
init(self, make, model, year, color, mileage): initializes the attributes with the given values
drive(self, distance): takes a float representing the distance driven and updates the mileage attribute accordingly
get_info(self): returns a string with the vehicle's make, model, year, color, and mileage attributes in a formatted way
Create a subclass called Car that inherits from the Vehicle class with the following additional attributes and methods:
"""
# class Vehicle:
#     def _init_(self,make, model, year, color, mileage):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.color=color
#         self.mileage=mileage
#
#     def drive(self,distance):
#         print("mileage",self.mileage)
#         fuel = distance/self.mileage
#         print("fuel consumed:",fuel)
#
#     def get_info(self):
#         print(self.make,self.model,self.year,self.color,self.mileage)
#
#
# obj=Vehicle("alto",2010,2012,'yellow',40.5)
# obj.drive(200)
# obj.get_info()


"""
Attributes:
num_doors: an integer representing the number of doors the car has
engine_type: a string representing the type of engine the car has
Methods:
init(self, make, model, year, color, mileage, num_doors, engine_type): initializes the attributes with the given values
get_info(self): overrides the get_info method of the Vehicle class to include the num_doors and engine_type attributes
Create an instance of the Vehicle class and call the drive method with a distance of 100. Then call the get_info method to print out the vehicle's information.

Create an instance of the Car class and call the drive method with a distance of 50. Then call the get_info method to print out the car's information.
"""


class Vehicle:
    def _init_(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, distance):
        print("mileage", self.mileage)
        fuel = distance / self.mileage
        print("fuel consumed:", fuel)

    def get_info(self):
        print(self.make, self.model, self.year, self.color, self.mileage)


class Car(Vehicle):
    def _init_(self, make, model, year, color, mileage, num_doors, engine_type):
        super()._init_(make, model, year, color, mileage)
        self.num_doors = num_doors
        self.engine_type = engine_type

    def get_info(self):
        super().get_info()
        print(self.num_doors)
        print(self.engine_type)


obj = Car("alto", 2010, 2012, 'yellow', (40.5), 4, 'eletric')
obj.get_info()

# """
# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in init method
#     You can init a object with construct parameter or set the value later
# """
#

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def breath(self):
#         print("i breath oxygen")
#
#     def food(self):
#         print("i eat food")
#
#
# class Dog(Animal):
#     def food(self):
#         print("i eat food")
#
#
# obj = Dog("mikey")
# obj.food()
# obj.breath()

"""
encapsulation:
wrapping up of data 
private 
public
protect

"""
class Teacher:
    def __init__(self,name,age ,salary):
        self.name=name
        self.age=age
        self.__salary=salary

t=Teacher("alwin",23,8000)

class customer(Teacher):


    def ttt(self):
        print(self.name)
        print(self.age)
        print(self.__salary)


obj=customer("sbi",33,60003)
obj.ttt()



"""
polymorphism:
its is the ability 
"""

"""
Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. 
"""


"""
A constructor is a special method in a class used to create and initialize an object of a class. There are different types
 of constructors in Python programming language. Constructor is invoked automatically when an object of a class is created.
"""







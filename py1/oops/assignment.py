"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

#
"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.            
(Just try )

Hints:
Consider use yield
"""
# class div:
#     def __init__(self):
#         self.n=""
#     def rang(self):
#         self.n=int(input("enter the num:"))
#     def divi(self):
#         for i in range(self.n):
#             if i%7==0:
#                 print(i)
# di=div()
# di.rang()
# di.divi()
#





#
# """
#  Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in _init_ method
#     You can init a object with construct parameter or set the value later
# """
# class Myclass:
#     class_Parameter="class param"
#     def __init__(self,instance_parameter):
#         self.instance_parameter=instance_parameter
#         print("instance parameter")
#
# obj=Myclass("v")
# print(Myclass.class_Parameter)

""""

4. Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
"""
# class staticMetod:
#     def _call_(self, my_function):
#         print("John")
#         my_function()
#         print("speaks English")
#
# @staticMetod
# def my_fun():
#     nationality = "American"
#     print("Nationality is", nationality)
#
# my_fun()
"""
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

"""
# class American:
#     def my_fu(self,place,landmark):
#         self.place=place
#         self.landmark=landmark
# class Newyork(American):
#     def _init_(self):
#        super().my_fu("newyork","statue of liberty")
#        print("my place is",self.place)
#        print("and landmark is", self.landmark)
#
# obj= Newyork()

"""
6. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method
# """
# class Circle:
#     def _init_(self,radius):
#         self.radius=radius
#     def Area(self):
#         area=math.pi*self.radius*self.radius
#         print(area)
# obj=Circle(6)
# obj.Area()
"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.
"""

# class Rectangle:
#     def _init_(self, length, width):
#         self.length = length
#         self.width = width
#
#     def compute_area(self):
#         return self.length * self.width
# obj=Rectangle(10,10)
# print(obj.compute_area())
"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
"""
# class Shape:
#     def _init_(self):
#         pass
#     def Area(self):
#         print("area is ",0)
# class Square:
#     def _init_(self,length):
#         self.length=length
#     def Area(self):
#         print("area is",self.length*self.length)
# obj=Square(10)
# obj.Area()

# """
# Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
#
# Hints:
# Use Subclass(Parentclass) to define a child class.
# """
# class Person:
#     def get_gender(self,gender):
#         self.gender=gender
#         pass
#
# class male(Person):
#     def get_gender(self,gender):
#         self.gender=gender
#
#         print("gender is",gender)
#
#
# class female(Person):
#     def get_gender(self, gender):
#         self.gender = gender
#
#         print("gender is", gender)
#
# obj1=male()
# obj1.get_gender("male")
# obj2=female()
# obj2.get_gender("female")
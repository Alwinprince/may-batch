"""
 1.Sort the odd and even numbers form the given list and add to a new list using list comprehension.
"""

# n=[1,2,3,4,5,6]
# odd=[i for i in n if i%2==0 ]
# even=[i for i in n if i%2!=0]
# print(odd)
# print(even)

"""
2 print the length of the elements as a list using the map function.
"""
#
# n=["apple","grapes","orange"]
# m=map(len,n)
# print(list(m))

"""
3
"""
#
# s=lambda x:x+15
# print(s(10))
#
# s=lambda x,y:x*y
# print(s(2,3))



##day 2 assignment


"""

1 Write a Python function that takes a list and returns a new list with distinct elements from the first list.
"""
#
# l=[1,2,3,4,4,4,5,5,6]
# def n(a):
#    s=[]
#    for i in a:
#     if i not in s:
#             s.append(i)
#    return s
# print(n(l))

"""
2 Define a function that accepts roll number and returns whether the student is present or absent.

"""
# n=(int(input("enter:")))
# x=[1,2,3,4,5,6,7,8]
# if n not in x:
#     print("absent")
# else:
#           print("present")
#

"""
3
"""
# def n(*num):
#   if num1>num2 and  num1>num3:
#       print(num1)
#   elif num2>num1 and num2>num3:
#       print(num2)
#   else:
#       print(num3)
# num1=int(input("enter:"))
# num2=int(input("enter:"))
# num3=int(input("enter:"))
# n(num1,num2,num3)



# """
# 3 Define a function in python that accepts 3 values and returns the maximum of three numbers.
#
# """


#
# """
# 1. Program to add and display sum of n number of integer using arbitrary argument passing
#
# """
#
# def b(*names):
#  sum=0
#  i=1
# for i in range(1,10+1):
#     sum+=i
#
#     i+=1
#     # i.append(sum)
# print(sum)
# b()
#
#
#
# """
# 2. find the sum of numbers in the given list using reduce function and alse find the largest number from the list using reduce function
# list1 = [1,2,3,4,5,6]
# """
#
# list1=[1,2,3,4,5]
# p=reduce
#
#
#
#
#
#
#
#
#
# """
#
# Python function to find the factorial of a number
# """
# num=int(input("enter the number to find factorial"))
# factorial=1
# for i in range(1,num+1):
#    factorial=factorial*i
# print(factorial)
#
#
# """
# Program to print the diamond shape
#
# """
# n=int(input("enter the level"))
# for i in range(1,n+1):
#     for j in range(n-i):#to print space
#        print(" ",end=" ")
#     for k in range(i):#to print star
#      print("*",end="   ")
#      print()
# for i in range(1,n+1):
#    for j in range(i):#to print space
#         print(" ",end=" ")
#    for k in range(n-i):#to print star
#      print("*",end="   ")
#      print()



# import os

#
#
# file=r'sample.py'
# x=os.path.exists(file)
# if x:
#     print(f"{file} the file is exixts")
# else:
#     print(f"{file} is not exists")




























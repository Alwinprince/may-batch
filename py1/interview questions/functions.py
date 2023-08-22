""""
""
# 1) Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# """
# l1=[2,4,3]
# l2=[5,6,4]
# new=[]
# new1=[]
# for i in l1:
#     new.append(str(i))
# string1="".join(new)
# k=int(string1)
# for j in l2:
#     new1.append(str(i))
# string2="".join(new1)
# n=int(string2)
# r=0
# while(k>0):
#     t=k%10
#     r=r*10+t
#     k=k//10
# str1=r
#
# re=0
# while(j>0):
#     te=j%10
#     re=re*10+te
#     j=j//10
# str2=re
#
# sum=str1+str2
# print(sum)
#
#
#
#
# """
# 2) with a given integer number n,write a program to generate a dictionary that contain suppose the following input is supplied
# to the program:
# then the o/p should be :
# {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}
# """
# num=int(input("enter:"))
# d=dict()
# for i in range(1,num+1):
#     d[i]=i*i
# print(d)


"""
covert the number into list and tuple
"""
# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of students: ", x)
# print(tuple(x))


"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
# from  math import sqrt
# c=50
# h=30
# d=list(map(int,input("enter numbers").split()))
# x=[]
# for i in d:
#     Q = sqrt((2 * c * i)/h)
#     x.append(int(Q))
# print(x)



















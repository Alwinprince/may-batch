"""
write python program to find thise numbers which are divisible by 7 and multiple of 5
"""
# num=35
# if num%7==0 and num%5==0:
#     print("number is divisible by 7 and multiple of 5")
# else:
#     print("number is not divisible by 7 and multiple of 5")
#
"""
write a program to find a person can vote or not
"""
# num=int(input("enter your age"))
# if num>=18:
#     print("You are eligible for vote")
# else:
#     print("You can't vote")

"""
Traffic light---if the light is green--car is allowed to go
yellow----car has to wait
red----car has to stop
# """
# temp="y"
# while(temp=="y"):
#  print("1.Red","2.Yellow","3.Green")
#  color= int( input("enter the light number"))
#  if(color==1):
#     print("Car has to stop")
#  elif(color==2):
#     print("Car has to wait")
#  elif(color==3):
#     print("Car is allowed to go")
#  else:
#     print("invalid light")
#
#
# temp=input("do you want to continue?if yes type y")

"""
A company decided to give bonus of 5% to employee if his/her year of service more than 5 years 
Ask user for their salary and  year  of service and print the bonus amount
"""
# salary=int(input("enter your salary"))
# exp=int(input("enter your experience"))
# if(exp>5):
#     bonus=salary*(5/100)
#     total=salary+bonus
#     print("your total salary is"+" "+str(total))
# else:
#     print("you are not eligible for bonus")

"""
A school has following rules for grading system:
a.below 25-F
b.25-45-E
c.45-50-D
d.50-60-C
e.60-80-B
f.above 80-A

"""
# mark=int(input("Enter your mark: "))
# if(mark<25):
#     print("F")
# elif(mark>=25 and mark<45):
#     print("E")
# elif(mark>=45 and mark<50):
#     print("D")
# elif(mark>=50 and mark<60):
#     print("C")
# elif(mark>=60 and mark<80):
#     print("B")
# elif(mark>=80):
#     print("A")
# else:
#     print("enter valid mark")
"""
Take three number from user and print greatest among them
"""
#
# x=int(input("enter first number"))
# y=int(input("enter second number"))
# z=int(input("enter third number"))
#
# if(x>y):
#     if(x>z):
#         print(str(x)+"is greatest")
#     else:
#         print(str(z)+"is greatest")
# elif(x<y):
#     if(y>z):
#         print(str(y)+"is greatest")
#     else:
#         print(str(z)+"is greatest")
# elif(x<z):
#     if(z>y):
#         print(str(z)+"is greatest")
#     else:
#         print(str(y)+"is greatest")
# else:
#     print("same values")

""""
check prime number
"""
# num = int(input("Enter the number to be checked: "))
# flag = 0
# for i in range(2, num):
#     if num % i == 0:
#         flag = 1
#         break
#
# if flag == 1:
#     print("Not a prime number")
# else:
#     print("Prime number")

"""
palindrome
"""
# s=input("ENter the string")
# x=s[::-1]
# if(s==x):
#     print(x+" "+"is"+' '+"palindrome")
# else:
#     print("not a palindrome")
"""
palindrome
"""
# num=int(input("Enter the number"))
# x=int(str(num)[::-1])
# if( x== num):
#     print("Palindrome")
# else:
#     print(" not palindrome")
# number= int(input("Enter the number"))
# rev=0
# temp=number
#
# while(number>0):#404 4
#     rem=number%10#find last digit#4 0 4
#     rev=rev*10+rem#add to a variable to store reversed number#4 404
#     number=number//10#find remaining numbers404
# if(temp==rev):
#     print("palindrome")
# else:
#     print("not palindrome")


"""
print fibonocci number upto limit
"""
# num=int(input("enter the limt"))
# a=0
# b=1
# for i in range(num+1):
#    print(a)
#    c=a+b
#    a=b
#    b=c
#

"""
armstrong number
"""
# num=(int(input("enter the number to check armstrong")))
# sum=0
# temp=num
# while(num>0):
#  rem=num%10
#  x=rem*rem*rem
#  sum=sum+x
#  num=num//10
# if(temp==sum):
#     print("armstrong number")
# else:
#     print("not armsrong")
"""
WAP to print sum of odd and even numbers from given ist[3,6,7,5,11,8]
# """
# number=[3,6,7,5,11,8]
# sum1=0
# sum2=0
#
# for i in number:
#     if(i%2==0):
#         sum1=sum1+i
#
#     else:
#         sum2=sum2+i
#
# print("sum of even numbers are:"+" "+str(sum1 ))
# print("sum of odd  numbers are:"+" "+str(sum2 ))
"""
Write a code to reverse a number
"""
# num=int(input("enter the number to reverse"))
# rev=0
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# # print(rev)

"""
Write code of Greatest Common Divisor
"""
# num1=(int(input("enter the first number")))
# num2=(int(input("enter the first number")))
# minimum = max(num1,num2)
# great = 0
# for i in range(1,minimum):
#     if num1 % i == 0 and num2 % i == 0:
#         if i > great:
#             great = i
# print(great)

"""
Write code to Check if two strings are Anagram or not
"""
# str1=input("enter the first string")
# str2=input("enter second string")
# set1=set(str1)
# set2=set(str2)
# if(set1==set2):
#     print("string is anagram")
# else:
#     print("string is not anagram")
"""
Python program to swap two elements in a list
# """
# temp = 0
# pos1 = 2
# pos2 = 4
# list1 = [10, 23, 35, 45, 5]
# print(list1)
#
# temp = list1[pos1]
# list1[pos1] = list1[pos2]
# list1[pos2] = temp
#
# print(list1)
"""
frequency of elements in list
"""
# number_list = [10, 20, 30, 20, 10, 40, 10, 50, 30, 30]
# count = {}
# for i in number_list:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
#
# print(count)
"""
factorial of a number
"""
# num=int(input("enter the number to find factorial"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(factorial)
"""
anagram
"""
# str1=input("enter the first string")
# str2=input("enter the second string")
# str3=str1.lower()
# str4=str2.lower()
# if(len(str3)):
#     sorted_1=sorted(str3)
#     sorted_2 = sorted(str4)
#     if(sorted_2==sorted_1):
#         print("anagram")
#     else:
#         print("not anagram")

"""
leap year
"""
# year=int(input("enter the year"))
# if year%400==0 or (year%4==0 and year%100!=0):
#     print("leap year")
# else:
#     print("not leap year")

"""
vowels
"""
# cha=input("character")
# low=cha.lower()
# if cha=="a":
#     print("vowel")
# elif cha=="e":
#     print("vowel")
# elif cha=="i":
#     print("vowel")
# elif cha=="o":
#     print("vowel")
# elif cha=="u":
#     print("vowel")
# else:
#     print("consonant")


# cha=input("character")
# low=cha.lower()
# a=["a","e","i","o","u"]
# if cha in a:
#     print("vowel")
# else:
#     print("consonant")

#______________________________________________Patterns______________________________________________________________________
"""
print the pattern
    *
   * *
  * * *
 * * * *
* * * * *
"""
# n=int(input("enter the level"))
# for i in range(1,n+1):
#     for j in range(n-i):#to print space
#         print(" ",end=" ")
#     for k in range(i):#to print star
#         print("*",end="   ")
#     print()
'''
*   *   *   *   
  *   *   *   
    *   *   
      *   
print this pttern
'''
# n=int(input("enter the level"))
# for i in range(0,n+1):
#     for j in range(i):#to print space
#         print(" ",end=" ")
#     for k in range(n-i):#to print star
#         print("*",end="   ")
#     print()

# n=int(input("enter the levels you want"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print(k+1,end="   ")
#     print()
"""
print this pTattern
        *   
      *   *   
    *   *   *   
  *   *   *   *   
*   *   *   *   *   
  *   *   *   *   
    *   *   *   
      *   *   
        * 
"""
# n=int(input("enter the level"))
# for i in range(1,n+1):
#     for j in range(n-i):#to print space
#         print(" ",end=" ")
#     for k in range(i):#to print star
#         print("*",end="   ")
#     print()
# for i in range(1,n+1):
#     for j in range(i):#to print space
#         print(" ",end=" ")
#     for k in range(n-i):#to print star
#         print("*",end="   ")
#     print()

"""
print this shape
*   *   *   *   *   
  *   *   *   *   
    *   *   *   
      *   *   
        *   
      *   *   
    *   *   *   
  *   *   *   *   
*   *   *   *   *   
"""
# n = int(input("enter the level"))
# for i in range(0,n-1):
#     for j in range(i):#to print space
#         print(" ",end=" ")
#     for k in range(n-i):#to print star
#         print("*",end="   ")
#     print()
# for i in range(1,n+1):
#     for j in range(n-i):#to print space
#         print(" ",end=" ")
#     for k in range(i):#to print star
#         print("*",end="   ")
#     print()

"""
print
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
"""
# n=int(input("enter te level"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="  ")
#     for k in range(i):
#         print("* ",end="    ")
#     print()

'''
print

'''
# n=int(input("enter te level"))
# for i in range(3,n+1):
#     for j in range(n-i):
#         print(" ",end="  ")
#     for k in range(i):
#         print("* ",end="    ")
#     print()
# for i in range(6,n+1):
#     for j in range(n-i):
#         print(" ",end="  ")
#     for k in range(i):
#         print("* ",end="    ")
#     print()
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""
# n=int(input("enter the level"))
# for i in range(1,n+1):
#     for k in range(i):#to print star
#         print(k+1,end=" ")
#     print()
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

'''
# n=int(input("enter the levels"))
# for i in range(n+1,0,-1):
#     for j in range(i-1,0,-1):
#         print(j, end="  ")
#     print()
"""
print
   A 
  B C 
 D E F 
G H I J 
"""
import  string
# n=int(input("enter the level"))
# x=1
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("",end=" ")
#     for k in range(i):
#         ch=chr(64+x)
#         print(ch,end=" ")
#         x=x+1
#     print()
"""
A 
B C 
D E F 
G H I J 
"""
# import  string
# n=int(input("enter the level"))
# x=1
# for i in range(1,n+1):
#     for k in range(i):
#         ch=chr(64+x)
#         print(ch,end=" ")
#         x=x+1
#     print()
#----------------------------------------------------------------------------------------------------------------------------------
"""
WAP that prints all the numbers from 0 to 6 except 3 and 6
"""
# for i in range(0,7):
#     if i==3 or i==6:continue
#     print(i)

"""
WAP to print multiplication table of a given number
"""
# num=int(input("enter the number you want to print multiplication table"))
# ran=int(input("enter the range you want to print"))
# for i in range(ran+1):
#     print (num,"x",i,"=",num*i)
"""
WAP to find factorial of a number
"""
# x=int(input("enter the number"))
# factorial=1
# for i in range(1,x+1):
#     factorial=factorial*i
#
# print(factorial)

"""
WAP to print a list of numbers divisible by 3
"""
# lis=[]
# for i in range(1,51):
#     if i%3==0:
#         # print(i)
#         lis.append(i)
# print(lis)
"""
List comprehension
"""
# fruits=["apple","orange","kiwi"]
# new=[x for x in fruits if "a"in x]
# print(new)
"""
print odd and even numbers using list comprehention
"""
#
# items=[1,3,8,4,5,6,7]
# even=[i for i in items if i%2==0]
# print(even)
# odd=[i for i in items if i%2!=0]
# print(odd)

# items=[1,3,8,4,5,6,7]
# lis=[i for i in ]

"""
Python Program to Remove Punctuations From a String
"""
# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# my_str = "Hello!!!, he said ---and went."
# no_punch=""
# for char in my_str:
#     if char in my_str:
#         if char not in punctuations:
#             no_punch=no_punch+char
# print(no_punch)
"""
frequency of elements in list
"""
# number_list = [10, 20, 30, 20, 10, 40, 10, 50, 30, 30]
# count = {}
# for i in number_list:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
#
# print(count)

"""
Python program to swap two elements in a list
"""
# temp = 0
# pos1 = 2
# pos2 = 4
# list1 = [10, 23, 35, 45, 5]
# print(list1)
#
# temp = list1[pos1]
# list1[pos1] = list1[pos2]
# list1[pos2] = temp
#
# print(list1)


"""

"""
# matrix=[[j for j in range(3)] for i in range(3)]
# print(matrix)



"""
WAP to remove all the repeating letters
"""
# str1="lets google the pineapple"
# str2=str1.split(' ')
# print(str2)
# str3=[]
# for i in str2:
#     k=''
#     for j in i:
#         if j in k:
#             continue
#         else:
#             k=k+j
#     print(k)
#     str3.append(k)
# print(" ".join(str3))

'''
Find all of the numbers from 1–1000 that are divisible by 8
'''
# lis1=[i for i in range(1,1001) if i%8==0]
# print(lis1)
"""
Write a Python program to triple all numbers in a given list of integers. Use Python map
"""
# x=[1,2,3,4,5]
# lis=map(lambda y:y*3,x)
# print(list(lis))

"""
Write a Python program to add two given lists and find the difference between them. Use the map() function
"""
# def addition_subtrction(x,y):
#    return x+y,x-y
# nums1 = [6, 5, 3, 9]
# nums2 = [0, 1, 7, 7]
#
# result = map(addition_subtrction, nums1, nums2)
# print(list(result))
"""
re

"""
# str1="lets google the pineapple"
# str2=str1.split(' ')
# # print(str2)
# str3=[]
# for i in str2:
#      x= i[::-1]
#      # print(x)
#      str3.append(x)
# # print(str3)
# print(" ".join(str3))

"""
"""
# str1="23465377387345"
# rev=[]
# num=[]
# even=[]
# odd=[]
# for i in str1:
#  num.append(int(i))
#
# for i in num:
#    if i%2==0:
#       even.append(i)
#    else:
#       odd.append(i)
# print(even)
# print(odd)
# odd.sort()
# even.sort(reverse=True)
# print(odd)
# print(even)
# odd.extend(even)
# print(odd)
# for i in odd:
#    rev.append(str(i))
# str2=" ".join(rev)
# print(str2)
"""
convert the string "123" into integer 123 without using built function
"""
strin="123"
x=[]
for i in strin:
   x.append(i)
   print(type(i))
print(x)

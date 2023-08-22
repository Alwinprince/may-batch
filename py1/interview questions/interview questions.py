# str=("1234")
# r=0
# for i in str:
#     d= ord(i)-ord("0")
#     r=(r*10)+d
# print(r)
# print(type(r))

# """
# function = function is a block of code which only runs when it is called.
#
# You can pass data, known as parameters, into a function.
#
# A function can return data as a result.
#
# arguments and parameters=The terms parameter and argument can be used for the same thing:
# information that are passed into a function.
#
#
# """
#
# def sumofNnums(num):
#     sum=0
#     for i in range(1,10):
#         sum=sum+i
#     return sum
# num=int(input("enter number:"))
# print((sumofNnums(num)))

#
# num1=34
# num2=67
# num3=89
# def max():
#   if num1>num2 and num1>num3:
#       return num1
#   elif num2>num1 and num2>num3:
#       return num2
#   else:
#       return num3
# print(max())


#find the sum of list of numbers

# num=[1,2,3,46,7,8]
# def sumoflist(num):
#     sum=0
#     for i in num:
#         sum=sum+i
#     return sum
# print(sumoflist(num))

#
# def solve(a):
#     a=[1,2,3]
# a=[2,4,6]
# print(a)
# solve(a)
# print(a)


##arbititry arguments
# def n(*names):
#     print("hi gooys",names,"how are you")
# n('jithu')
# n('shawn')

##keyword arguments

# def n(name1,name2,name3):
#  print("hi"+ name2)
# n(name3= "jin",name2 ="mark",name1="jack")

###default value

# def n(name="alwin"):
#     print("hi " +name)
# n()
# n("jithu")
# n("shawn")
#


# ##
# def n(s):
#     str=""
#     for i in s:
#         str=i+str
#     return str
# s="ronaldo"
# print(str)
# print(n(s))


# def n(s):
#     string= [s[i] for i in range(len(s)-1,-1,-1)]
#     print(string)
#     print(s)
#     return"".join(string)
# s="python"
# print(n(s))



"""
multiply all the number in a list using function
"""

# def mult():
#     mul=1
#     lis=[1,2,3,4,5]
#     for i in lis:
#         mul=mul*i
#     print(mul)
# mult()



"""
write a python function to calculate the factorial of a number.the function accepts the number as an arguments
"""
# def fact(a):
#     factorial=1
#     while(a>0):
#         factorial=factorial*a
#         a=a-1
#     print(factorial)
# fact(int(input("enter the number")))



"""
generate a python list of all even number betwwen 4 and 30
"""
# def sum():
#    x=[]
#    for i in range(4,31):
#        if i %2==0:
#            x.append(i)
#    print(x)
# sum()



"""

write a pyton function that take a number as a parameter and check the number is prime or not 
"""

#
# def prime(a):
#     flag=0
#     for i in range(2,a):
#         if a%i==0:
#             flag=1
#     if flag==0:
#        print("prime")
#     else:
#        print("not prime")
# prime(7)





























# def myfunc(a,b):
#     return a+b
# lis=map(myfunc,("orange","apple","banana"),("ornage","red","yellow"))
# print(lis)
# print(list(lis))


# l=["sarath","krishnan"]
# lis=map(list,l)
# print(list(lis))

# x=lambda a,b:a+b#lambda function used for perform one operation
# print(x(2,7))
#
# num1=[1,2,3]
# num2=[4,5,6]
# result=map(lambda x,y:x*y,num1,num2
#            )
# print((list(result)))

"""
filter
"""
from functools import reduce

# numbers=[-3,-8,-9,7,-6,5,4,-2]
# x=filter(lambda a:a<0,numbers)
# print(list(x))
"""
reduce
"""

# list1=[1,2,3,4]
# product=reduce(lambda x,y:x*y,list1)
# print(product)


# numbers=[-3,-8,-9,7,-6,5,4,-2]
# x=reduce(lambda x,y:x+y,numbers)
# print((x))
num=int(input("enter number"))
x=range(num+1)
sum=reduce(lambda a,b:a+b,x)
print(sum)
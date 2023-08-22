"""

recursion is a funtion that calls itself
# """
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# def counter(y):
#     if y<=0:
#         return y
#     else:
#         return y+counter(y-1)
# print(counter(10))



# def fact(n):
#     if n==1:
#         print(n)
#         return 1
#     else:
#         x=n*fact(n-1)
#         print(x)
#         return x
# print(fact(5))
#
# def sum(s):
#     if s<=0:
#         print(s)
#         return s
#     else:
#         a=s+sum(s-1)
#         print(a)
#         return a
# print(sum(10))


# def tri_recursion(k):
#     if k>0:
#         result=k+tri_recursion(k-1)
#         print(result)
#         return result
#     else:
#         result=0
#         return result
# print(tri_recursion(5))




"""palindrom"""

# s=input("enter a string:")
# def palindrom(s):
#     if len(s)<=1:
#         return True
#     else:
#         if s[0]==s[-1]:
#             return palindrom(s[1:-1])
#         else:
#             return False
# print(palindrom(s))



"""
sum of digits
"""
# n=int(input("enter a number:"))
# def sum(n):
#     if n<10:
#         return n
#     else:
#         return n%10 + sum(n//10)
# print(sum(n))



"""product of digits"""
# a=int(input("enter more than two digit number: "))
# def power(a):
#     if a<10:
#         return a
#     else:
#         return a%10 * power(a//10)
# print(power(a))

def prod(a):
    if a<10:
        return a
    else:
        return a%10 * prod(a//10)
a=int(input("enter a number:"))
print(prod(a))

"""power
write a recursive to calculate the results of rasing a number to a given power 

"""
"""prime or not"""

# num=int(input("enter a number:"))
# for i in range(2,num):
#     if num % i==0:
#         print(num,'not prime:')
#         break
# else:
#         print(num,"prime")

#
# def is_prime(number):
#     if number <= 1:
#
#         return False
#     for diviser in range(2, number):
#         if number % diviser ==0:
#             return False
#         return True
# num=int(input("enter a number:"))
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")








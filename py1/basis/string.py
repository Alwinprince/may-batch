"""
string - immutable datatype

"""
#string indexing

str1 = "hello world"
print(str1[1])
print(str1[2])
print(str1[8])
print(str1[0])
print(str1[-1])

#string slicing

print(str1[3:8])
print(str1[::1])
print(str1[:-2])

#string method

str1 = "helloworld"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.isalpha())
print(str1.isupper())
print(str1.isalnum())
print(str1.islower())


list = ["apple","banana","orange"]
x = ''.join(list)
print(x)

name = "abhijith sreekumar"
print(name.split())

print(name[8:])

"""
append new string in the middle of a given string

s1 = "python"
s2 = "luminar"
o/p = pytluminarhon

"""

s1 = "python"
s2 = "luminar"
print(len(s1))
mid = int(len(s1)/2)
print(mid)


"""
create a new string made of the first , middle , and last characters of each input string
s1 = "python"
s2 = "luminar"

o/p = plhinr

"""
first_char = s1[0] + s2[0]

print(first_char)
mid_chars = s1[int(len(s1)/2)]
print(mid_chars)

mid_chars2 = s2[int(len(s2)/2)]



str1 = "hi dears"

x = (set(str1))
print(x)

#print(str(x))

print(str(type(x)))
y = ''.join(x)
print(y)
print(type(y))




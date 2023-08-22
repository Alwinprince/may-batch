"""
python f string = it is the newest python syntax to do dtring formatting.
its avialable since python 3.6.its more faster more readable and less errors
The f-string have the f prefix and use {} brackets tom evaluate values

"""
# name='alwin'
# age=23
# print('%s is %d years old'%(name,age) )
#print('{} is {} years old'.format(name,age))
#print(f'{name}is{age} year old')


# bags=3
# total=12
# print(f'there are {bags*total}  apples')


# File Handling:
# File handling is an important part of any web application.
#
# Python has several functions for creating, reading, updating, and deleting files.

# The key function for working with files in Python is the open() function.
#
# The open() function takes two parameters; filename, and mode.
#
# There are four different methods (modes) for opening a file:
#
# file=open('sample.py','x')
# file=open('sample.py','w')
# file.write('hi gooys')
# file.close()

#append
#file=open('sample.py','a')
# file.write('hi gooys')

# file.close()

# file=open('sample.py','r')
# print(file.read())
#
# with open('sample.py','r') as file:
#     print(file.read())

# import os
# # os.remove('sample.py')
#
#
# file=r'sample.py'
# x=os.path.exists(file)
# if x:
#     print(f"{file} the file is exixts")
# else:
#     print(f"{file} is not exists")

#
# with open('test.py','r') as file:
#     # file.write('new new\n')
#     # file.write('new buddy\n')
#     # lines=file.()
#     # print(lines[])



# """
# 1.write a python prgramme to find the longest word from the file
# """
#
# def long(test):
#     with open(test,'r') as infile:
#         w=infile.read().split()
#         print(w)
#         max1=(max(w,key=len))
#         print((max1))
#         return[word for word in w if len(w)==max1]
# print(long('test.py'))
#



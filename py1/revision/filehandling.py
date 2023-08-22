

# """
# file handling:write,read,create,append
# mode: w,r,x,remove,a,w+,r+,a+
# """
# with open("new.txt","w") as file:
#     file.write("hi dears hello world")
#     file.close()
# with open("new.txt","r") as file:
#     print(file.read())

# with open("new.txt","w") as file:
#     file.write("hehehehe")
#     file.close()

# import os #to delete and handle files
# file="new.txt"
# os.remove(file)#to remove file

# with open("new.txt")as file:
#     x=file.readlines()
#     print(x)
#
# """
# accessing file lines by indexing
# """
#
# with open("new.txt")as file:
#     # print(x[0])
#     x=file.readlines()
#     x.pop(0)#to remove specific line
#     print(x)
#
#     for i in x:


# import fileinput
#
# file1='new.txt'
# line=[2,4]
# def del_lines():
#     with fileinput.input(file1,inplace=True)as file:
#          for i in file:
#              if file.lineno()not in line:
#                  print(i.rstrip())
# del_lines()


# """"
# python list files in directory
# """
# import os
#
# files2=r'C:\Users\alwin\PycharmProjects\py1\basis'
# def list_fil(files2):
#     file3=os.listdir(files2)
#     return file3
# file4=list_fil(files2)
# print(file4)










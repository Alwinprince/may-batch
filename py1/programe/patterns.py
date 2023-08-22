# pyramid preparation

# n = int(input('enter the level you want:'))

#
# for i in range (1,n+1):
#     for j in range(n-i):
#         print(' ',end= ' ')
#     for k in range(i):
#             print('* ',end='  ')
#     print()

#reverse

# n = int(input('enter the level'))
#
# for i in range (1,n+1):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(n-i):
#              print('* ',end='  ')
#     print()
#

#
# n = int(input('enter the level'))
#
# for i in range(1,n+1):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(n-i):
#             print('*  ',end=' ')
#     print()


# number pattern

# n = int(input('enter the number'))
# for i in range(1,n+1):
#      for j in range(n-i):
#          print(' ',end='')
#      for k in range(i):
#              print(k,end=' ')
#      print()
#

"""
1) create a diamond pattern
"""

n = int(input('enter the level'))
for i in range(1,n+1):
    for j in range(n-i):
         print(' ',end=' ')
    for k in range(i):
        print('* ',end='  ')
    print()

for i in range (1,n+1):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
            print('* ',end= '  ')
    print()

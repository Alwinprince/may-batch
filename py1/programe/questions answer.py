"""
write a python code to remove all the rpeating letters from each words of the given sentence.
i/p :let's google the pineapple
o/p : let's gole the pineal
"""
# str1 = "let's google the pineapple"
# str2 = str1.split()
# str3 = []
# for i in str2:
#     k = ''
#     for j in i:
#         if j in k:
#             continue
#         else:
#             k = k+j
#     print()
#
#     str3.append(k)
#     print(str3)
# print(" ".join(str3))

"""
given a scentence , reverse each word but don't reverse the sentence
"""

str = "let's google the pineapple"
str1 = str.split()
re_word = []
for word in str1:
    word [::-1]
    re_word.append(word)
print(re_word)
print(' '.join(re_word))


"""
1) write a code to reverse a number
"""

num = int(input('enter the number'))
rev = 0
while num >0:
    n = num % 10
    rev = (rev*10) + n
    num = num //10
    print(rev)


"""
2) write a code of greatest common divisor

"""

x = int(input('enter first num'))
y = int(input('enter second num'))
maximum = max(x,y)

great = 0
for i in range (1,maximum):
    if x % i==0 and y % i ==0:
        a = i
        if i > great:
            great = i
            print(great)

# """
# write a code to check if two strings are anagram or not
# """
#
# str1 = input('enter the string1')
# str2 = input('enter the string2')
# str3 = str1.lower()
# str4 = str2.lower()
# if (len(str3))==len(str4)):
#     sorted_str1 = sorted(str3)
#     print(sorted_str1)
#     sorted_str2 = sorted(str4)
#     print(sorted_str2)
# if (sorted_str1==sorted_str2):
#     print(str1 + "and"+ str2 + "are anagram")
#
#
# """
# 1) prepare a heart shape
# """
# num1 = 8
# num2 = 3
# for i in range(2,num2+1):
#     for j in range((num2+2)-i):
#         print(end='  ')
#     for k in range(i):
#         print('*',end='  ')
#     for j in range(num2-i):
#         print(' ',end=' ')
#     for k in range(i):
#         print('*',end='  ')
#     print()
#
# for i in range(1,num1):
#     for j in range(i):
#         print(end='  ')
#     for k in range(num1 - i):
#         print('*',end='  ')
#     print()
#

"""
'24536872',rearrange this number to, odd numbers to ascending order and even numbers to descending order.
"""
# str = '24536872'
# num = []
# even = []
# odd = []
# for i in str:
#     num.append(int(i))
#
# print(num)
# for j in num:
#     if j %2==0:
#         even.append(i)
#     else:
#         odd.append(j)
# print(odd)
# odd.sort()
# even.sort(reverse=True)
# print(odd)
# even_int =[str[x]for x in even]
# odd_int = [str[x]for x in odd]
#
#






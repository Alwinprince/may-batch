"""
list (mutable)

indexed , orderd , allows duplicates

"""
list_items = ["apple", "orange", "mango" , "grapes"]
print(list_items)
print(list_items[1])
print(list_items[-1])
print(list_items[::-1])
print(list_items[2][3])

list_items [1] = 'pineapple'
print(list_items)
print(list_items[0][2:])

#list_items = '#'

#print(list_items)

list_items = ["apple","orange","mango", "grapes",["python", "react", "django"]]
print(list_items[4][0])
print(list_items[4][::1])
print(list_items[4][0][::-1])

list_items[4].insert(1,'google')
print(list_items)
list_items.append("angular")
print(list_items)
print(list_items[4][2])

list2 = ["vento", "bmw","audi","ford"]

list_items[4].extend(list2)
print(list_items)
list_items[4].remove("python")
print(list_items)

list_items[4].clear()
print(list_items)

list_items[:-1].pop(1)
print(list_items)

 # find out sum using list

"""
find out sum = [1,2,3,4,5]

"""

my_list = [1,2,3,4,5]
sum= 0
for i in my_list:
    sum = sum + i
    print(sum)

#product

print("product")
pdt = 1
for i in my_list:
    pdt *=i
    print(pdt)

"""
write a python program to convert a list of characters into a string
s = ['p','y','t','h','o','n']
"""
s = ['p','y','t','h','o','n']
str1 = ""
for i in s:

    str1 +=i
    print(str1)

 #conditional statement

a = 33
b = 200
if b < a:
    print("a is greater than b")

elif b > a:
    print("b is greater than a")
else:
    print("a is less than b")


    """
numbers = [1,5,6,-5,-2,-1,-7]    

    """

numbers = [1,5,6,-2,-1,-7]
x = []
y = []
z = []
for i in numbers:
    if i>0:
        x.append(i)
        print(x)

    elif i ==0:
         z.append(i)
         print(y)

    else:
        z.appennd(i)
        print(z)


mylist = [5,9,8,7,3,2]
max = mylist[0]
for i in mylist:
    print(i)
    if max<=i:
       max = i
print(max)


#membership operator

"""write a python program to find out the common numbers from two lists """
list1 = [1,6,8,7,5]
list2 = [8,6,4,3,1]

new_list = []
for i in list1:
    for j in list2:
        if i ==j:
            new_list.append(i)
print(new_list)
if i ==j and i not in new_list:
    print(i ==j)
    new_list.append(i)
print(new_list)

""""find the numbers from the given numbers
"""


list = [1,2,3,4,5,6]
even = []
for i in list:
    if i %2==0:
       even.append(i)
print(even)


"""
write a python program to remove repeated elements from given list without using the bulit - in methods
list_to_remove = ["let's", "google","the","pineapple","photo", "google", "photo" ]
"""

list_to_remove = ["let's", "google","the","pineapple", "photo", "google", "photo"]
remove = []
for i in list_to_remove:
    if i not in remove:
        remove.append(i)
print(remove)


"""
["www.zframz.com","www.wikipedia.org","www.asp.net","www.abcd.in"]
write a python program to print website suffixes(com,org,in) from this list.
"""

list = ["www.zframz.com", "www.wikipedia.org", "www.asp.net","www.abcd.in"]
for i in list:
   print(i)
   suffix = i.split('.')[-1]
   print(suffix)



"""
tuple (immutable) ,indexed, orderd, allow duplicate
"""
#tuple method - converting

tuple1 = ("apple",12,4,"orange","apple",[32,"abcd"])
print(tuple1)
tple = "orange"
print(type(tple))

print(tuple1[4])
print(tuple1[5][0])
print(tuple1[3])

x = list(tuple1)
print(x.append('abcd'))
x[0]= 'grapes'
print(tuple(x))

tple1=("orange",23,5,6,"apple")
tple2=("grapes","abcd","car",45,87)

x = list(tple2)
x.extend(tple)
print(tuple(x))




"""
fruit = 'banana'
"""
fruit = 'banana'
index = 0
while index <len(fruit):
    letter= fruit[index]
    print (index, letter)
    index = index +1

thistuple = ("apple","banana","cherry",[8,"abcd",])
index = 0
for i in thistuple:
    print(index,i)
    index = index +1

    #enumerate

thistuple = ("apple","banana","cherry",[8,"abcd",0])
x = enumerate(thistuple)
print(list(x))


print(thistuple[3][::-1])


"""
check whether an element exist with in a tuple
tuple1 = ("apple",[1,2,3],(5,4,6),1,6,7,8)

"""
tuple1 = ("apple",[1,2,3],(5,4,6),1,6,7,8)
print("apple" in tuple1)

tuple1 = ("s","t","r","i","n","g")
print(''.join(tuple1))

"""
count the number of occurance of items 50 from a tuple
tuple1 = (20,50,70,50,60,50)

"""

tuple1 = (20,50,70,50,60,50)
tuple1 = tuple1.count(50)
print(tuple1)

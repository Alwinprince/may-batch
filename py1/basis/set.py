""""
set - (immutable), unorderd, unindexed, duplicates not allowed
"""

set1 = {"safina",12,"python","bca",12,"python"}
print(set1)

x = list(set1)
print(x)
print(x[0])
set1 = {"safna",12,"python","bca",12,"python",(1,2,3),set["abcd"]}
print(set1)

set2 = {"arjun",(1,2,3),"abcd","python"}

print(set2)
x = set1.difference(set2)
print(x)

y = set1.intersection_update(set2)
print(y)
z = set1.union(set2)
print(z)

a = set1.symmetric_difference(set2)
print(a)

h = set1.symmetric_difference_update(set2)
print(h)




"""
a company decided to give bonus of 5% to its employee if his/her
year of service is more than 5 years
ask user for their salary and year of service and print the net bonus amount.

"""
experience = input("enter the year of exp:")
salary = input("enter the amount of salary:")
if experience >5:
    salary = salary + salary*0.05
    print(salary)
else:
    print("not eligible for bonus")


"""
5) a school has following rules for grading sysytem :
   a, below 25 - f
   b, 25 to 45 - e
   c, 45 to 50 - d 
   d, 50 to 60 - c
   e, 60 to 70 - b
   f, 70 to 80 - a
   ask user to enter marks and print the corresponding grade

"""
mark = int(input("enter the mark"))
if mark<25:
    print("f")
elif mark >= 25 and mark >45:
    print("e")
elif mark >=45 and mark >50:
    print("d")
elif mark >=50 and mark >60:
    print("c")
elif mark >=60 and mark >70:
    print("b")
elif mark >=70 and mark >80:
    print("a")



"""
take three int value from user and print greatest among them
"""
first_number = int(input("enter the first number"))
second_number = int(input("enter the second number"))
third_number = int(input("enter the third number"))

num1 = 20
num2 = 15
num3 = 30

if num1>= num2 and num1>= num3:
    print(num1,"is larger")
elif num2>= num3 and num2>= num1:
    print(num2,"is grater ")
else:
    print(num3,"is greater")

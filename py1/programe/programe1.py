sampledict = {

        "class":{
            "student" : {
                "name":  "mike" ,
                "marks" : {
                    "physics" : 70,
                    "history" : 80

                    }
            }
        }
}
print(sampledict['class']['student']['marks']['history'])

print(sampledict['class']['student']['name'])


sampledict1 = {"name":"mike","course":{"python":2023,"angular":2022,"marks":{"physics":70,"history":80}}}


print(sampledict1["course"]["marks"]['physics'])



#change value of a key in a nested dict

sample_dict = {
    'dict1' : {"name":"chithra","age":12,"course":"python"},
    'dict2': {"place":"abc","qualification":"b-tech"},
    'dict3': {"job":"pythondev","sal":233}
}
print(sample_dict)
x = sample_dict['dict2']['qualification']= "bca"
print(sample_dict)

#rename a key of a dict


dict1 = {'name':'chithra','age':12,'course':'python'}
print(dict1)
dict1['class']=dict1.pop('course')
print(dict1)
print(dict1['class'])


"""
# find out the leap year
# """
#
# year = int(input('enter the year:'))
# if (year % 400 ==0) or (year % 4 ==0 and year % 100 !=0):
#     print('leap year')
# else :
#     print('not leap year')

# divisible by 400
# divisible by 4 and not divisible by 100


"""
write a program to check whether a character is a vowel or consonant
"""
#
# character = input('enter the character:')
# vowels = ('a','e','o','i','u','A','E','I','O','U')
# if character is vowels:
#     print('character is vowels')
# else:
#     print('consonant')





# print 1 to 10 using while loop

#
# i = 1
# while i <=10:
#      print(i)
#      i +=1
#
# # print 10 to 1 using while loop
#
# i = 10
# while 1 >= 1:
#     print(i)
#     i -=1


# sum of natural numbers using while loop


num = int(input('enter the number'))
sum =0
i = 1
while i <=num:
    sum += i
    i += 1
    print(sum)
print(sum)

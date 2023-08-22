""
#library = library is a collection of packages and modules that can be used to access built-in functionality.
#packages = A python package is a collection of modules.
#module = a python file contains modules
"""
import datetime
import json

#
# today = datetime.datetime.now()
# print(today)
#
# time = datetime.time.second
# print(str(time))
#
# from datetime import datetime
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time)

"""
#JSON IN PYTHON :- JSON is a syntax for storing and exchanging data.
                #JSON is text, written with Java Script object notation.
"""
#
# #example
# x = {'name':'john','age':24,'city':'new york'}
# print(type(x))
#     json.dump(x)

"""
# 2) access the value of key2 from the following JSON
# 3) access the nested key 'salary' from the following JSON
# """
#
# import json
#
# samplejson ="""{
#   "company":{
#    "employee":{
#     "name":"emma",
#     "payable":{
#      "salary":7000,
#      "bonus":8000
#     }
#   }
#  }
# }"""
#
#
#
#
# y = json .loads(samplejson)
# print(y["company"]["employee"]["payable"]["salary"])
#
"""
4) write a python program to generate a random color hex, a random alphabetical string, random value between two integers
   (inclusive) and random multiple of 7 between 0 and 70.use random.randint()
"""

import random

color = "%06x" % random.randint(0,0xffffff)

color = "%03x" % random.randint(0,0xfff)

# random alphabetical string
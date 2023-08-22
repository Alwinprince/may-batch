"""
dictionary (mutable), orderd, indexed, duplicates not allowed
"""

dict1 = {"name":"abhi","age":21,"place":"pta"}
print(dict1)
print(dict1["age"])

#get method

print(dict1.get("name"))
dict1["name"]= "aswin"
print(dict1)

#update method

dict.update({"qualification":"b.com","role":"student"})
print(dict1)

print(dict1.keys())
print(dict1.values())

dict_keys = (['name','age','place'])
dict_values = (['abhi',21,'pta'])
print(dict(zip(dict_keys,dict_values)))

print(dict1)
dict1.popitem()
print(dict1)

x = ('key1','key2','key3')
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)

car = {"brand":"ford","model":"mustang","year":1964}
x = car.setdefault("model", "branco")
print(car)



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




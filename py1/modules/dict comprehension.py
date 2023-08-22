"""
dictionary={key:value for vars in iterable

 """

# s={}
# for num in range(1,11):
#     s=[num]=num*num
#     print(s)
#
#
#
# #dict comprehension
#
# s={num:num*num for num in range(1,11)}
# print(s)


#
# price={'milk':1.8,'coffe':2.6,'bread':2.4}
# pound=0.8
# newprice={key:value*pound for (key,value) in price.items()}
# print(newprice)
#
#
#
#
# first={'alwin':22,'jithu':77,'pollu':87}
# new={k:v for(k,v) in first.items() if v % 2==0}
# print(new)



# key=["a","b","c"]
# values=[1,2,3,]
# new={k:v for (k,v) in zip(key,values)}
# print(new)
#
# new={k:("even" if k %2==0 else "odd")for k in range(1,11) }
# print(new)


keys=['a','b','c','d','e','f']
ev=[keys[i]for i in range(1,len(keys),2)]
print(ev)
oss=[keys[i] for i in range(0,len(keys),2)]
print(oss)
print(dict(zip(oss,ev)))




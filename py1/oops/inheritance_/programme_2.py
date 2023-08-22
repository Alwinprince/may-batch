#  class Animal:
#     def __init__(self,identity,age):
#         self.identity=identity
#         self.age=age
#     def fet(self):
#         if self.age==10:
#             return True
#         else:
#             return False
# cs=Animal("dog",10
#           )
# x=(cs.fet())
# print(x)
# if(x==True):
#  print(cs.__dict__)
#
# class Teacher:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary


# t = Teacher("alwin", 23, 8000)


class customer(Teacher):

    def child(self):
        print(self.name)
        print(self.age)
        # print(self.__salary)
        super().__init__("alwin", 23, 8000)

obj = customer("alwin",23,8000)
obj.child()
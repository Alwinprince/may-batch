"""
          OOPS

1.class -----------its a collection of objects
2.object-----------instance of a class
3.inheritance
4.polymorphism
5.encapsulation
6.abstraction


"""

# class car():
#     def _init_(self,car_name,model,color):         #constructor method
#         self.car_name=car_name
#         self.model=model
#         self.color=color
#     def drive(self):                                  #method
#         print("driving",self.car_name,self.model)
#
# obj= car("alto",800,'white')
# print(obj.car_name)
# print(obj.color)
# print(obj.model)
#
#
# print(obj.drive())

class school():
    def _init_(self,std_id,std_name,place):
        self.std_id=std_id
        self.std_name=std_name
        self.place=place

    def detail(self):
        print(self.std_name,"comming from",self.place)

obj=school(12,'sagil','palloor')
print(obj.std_id)
print(obj.std_name)
print(obj.place)
print(obj.detail())
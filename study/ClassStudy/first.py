import  json
class Student:
    name = None
    age = None
    sex = None
    def say_hi(self):
        print(f"大家好，我是{self.name}")

stu1 = Student()
stu2 = Student()

stu1.name = 'jay'
stu2.name = '林俊杰'

def __init__(self,name,age,sex):
    self.name = name
    self.age = age
    self.sex = sex


stu1.say_hi()
stu2.say_hi()

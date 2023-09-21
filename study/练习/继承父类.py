
class Phone:
    money = 0
    def  call_number(self):
        print("拨打电话")

class MyPhone(Phone):
    Phone.money =  1

    def call_number(self):
        #方式1   父类名.成员方法（self）
        Phone.call_number(self)
        # 方式2   super().成员方法（）
        super().call_number()
        print("2023拨打电话")

phone = MyPhone()
phone.call_number()

from typing import Union
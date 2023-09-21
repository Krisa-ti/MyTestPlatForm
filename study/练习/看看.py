def modify_number(x):
    x = x + 1
    print(x)

number = 5
modify_number(number)
print(number)  # 输出 5，函数中对形参 x 的修改不影响原始变量 number

class Anmia:
    def __init__(self, name):
        self.name = name
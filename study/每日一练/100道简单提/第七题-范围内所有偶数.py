# 输入开始和结束  计算范围内所有偶数   不包含结尾
# begin 4   end  15   输入   4,6,8,10,12,14


def oushu(begin,end):
    arr = []
    # begin = int(input("请输入开始的数字："))
    # end = int(input("请输入结尾的数字："))
    for item in range(begin, end):
        if item % 2 == 0:
            arr.append(item)
    return arr


print(oushu(4 , 14))

def jiecheng(number):
    arr = []
    sum = 1
# 将所有的数放到数组中
    for i in range(0,number):
        arr.append(i+1)
        print(arr[i])

    for j in range(len(arr)):
        if j < len(arr):
            sum =sum *  arr[j]

        else:
            break
    print('当前总数为{number}阶,阶乘总和为：{sum}'.format(number=number,sum= sum))


jiecheng(7)


#  第二种办法
def get_jiecheng(a):
    result = 1
    while a > 0:
        result *= a
        a -= 1
    print(result)
get_jiecheng(7)
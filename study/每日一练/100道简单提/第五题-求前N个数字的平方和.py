# 输入数字N
# 计算  1的平方 +  2的平方 + 3的平方


def pingfang(number):
    result  = 0
    sum = 0
    while number >= 0:
        result = number * number
        sum += result
        number -= 1
    print(sum)

pingfang(5)

def pingfang1(n):
    result1 = 0
    for i in range(1,n+1):
        result1 += i * i
    print(result1)

pingfang1(5)
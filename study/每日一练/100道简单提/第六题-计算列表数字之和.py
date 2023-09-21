# Input [1,2,3,4]  ;output   10
# Input [17,5,3,5]  ;output   30

def sum_of_list():
    arr = []
    flag = True
    sum = 0
    total = 0
    while flag:
        Input = int(input("请输入需要计算的数字，按0退出："))
        if Input != 0 :
            arr.append(int(Input))
            print(arr)
        if Input == 0:
            for i in range(len(arr)):
                sum += arr[i]
            print(sum)
            A = False
            break


def sum_of_list1(param_list):
    total = 0
    for item in param_list:
        total += item
    return total


list1 = [1, 2 , 3, 4, 5, 6, 7, 8]
print(sum_of_list1(list1))


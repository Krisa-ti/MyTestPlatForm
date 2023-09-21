#  移除列表中多个元素
#  输入  [3,4,5,6,7,8,9,10,11]
#  移除  [3,4]
#  输入  [5,6,7,8,9,10,11]


def remove_part_list(arr,after_remove_arr):
    for i in after_remove_arr:
       arr.remove(i)

    return  arr




print(remove_part_list( [3,4,5,6,7,8,9,10,11],[6,4]))
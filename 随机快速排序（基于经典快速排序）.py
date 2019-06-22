#随机快排是在数组中随机取一个数为基准进行排序，求复杂度需要求期望，期望为O(N*logN)

import random

def GenerateRandomArray(length):
    arr = []
    for i in range(length):
        arr.append(int(random.random() * 100))
    return arr

def QuickSort(arr):
    less = []
    more = []
    equal = []
    if len(arr) < 2:
        return arr
    else:
        idx = int(random.random() * len(arr))
        num = arr[idx]
        for i in arr:
            if i < num:
                less.append(i)
            elif i > num:
                more.append(i)
            else:
                equal.append(i)
        arr_less = QuickSort(less)
        arr_more = QuickSort(more)
        return arr_less + equal + arr_more

arr_random = GenerateRandomArray(10)
print('整理前的数组', arr_random)
arr_sort = QuickSort(arr_random)
print('整理后的数组', arr_sort)
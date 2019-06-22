#经典快排是取数组最后一个（或者其他固定的位置）数为基准进行排序，若遇到极端情况，复杂度为O(N**2)
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
        num = arr[-1]
        for i in arr:
            if i < num:
                less.append(i)
            elif i > num:
                more.append(i)
            else:
                equal.append(i)
        less = QuickSort(less)
        more = QuickSort(more)
        return less + equal + more

arr_random = GenerateRandomArray(10)
print('整理前的数组', arr_random)
arr_sort = QuickSort(arr_random)
print('整理后的数组', arr_sort)
import random

def GenerateRandomArray(length):
    arr = []
    for i in range(length):
        arr.append(int(random.random() * 100))
    return arr

def partition(arr, num, l, r):
    curr = l
    less = l - 1
    more = r + 1
    while curr < more:
        if arr[curr] < num:
            less += 1
            arr[curr], arr[less] = arr[less], arr[curr]
            curr += 1
        elif arr[curr] > num:
            more -= 1
            arr[curr], arr[more] = arr[more], arr[curr]
        else:
            curr += 1
    return arr, less + 1, more

arr_random = GenerateRandomArray(55)
print('整理前的数组', arr_random)
arr_sort, _, _ = partition(arr_random, 50, 0, 54)
print('整理后的数组', arr_sort)


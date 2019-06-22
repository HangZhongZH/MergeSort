array_str = input('输入需求解的数组：')
array_str = array_str.split()
array_qs = []
for i in range(len(array_str)):
    array_qs.append(eval(array_str[i]))

def mergesort(array):
    array_len = len(array)
    if array_len < 2:
        return array
    else:
        k = int(array_len / 2)
        array_left = mergesort(array[: k])
        array_right = mergesort(array[k: ])
        return combine(array_left, array_right)

def combine(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i: ]
    result += right[j: ]
    return result

array_sort = mergesort(array_qs)
print(array_sort)
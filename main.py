"""def insertionSort(arr):
    for j in range(2, len(arr)):
        key = arr[j]
        i = j - 1
        while arr[i] > key and i >= 0:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key


arr = [10, 24, 45, 56, 23, 4, 1, 26]
insertionSort(arr)
for k in range(len(arr)):
    print("%d " % arr[k])
"""

"""def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp



arr = [10, 24, 45, 56, 23, 4, 1, 26]
selectionSort(arr)
for i in range(len(arr)):
    print("%d " % arr[i])
"""


"""def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


array = [10, 7, 8, 9, 1, 5]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')
"""
ğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğ
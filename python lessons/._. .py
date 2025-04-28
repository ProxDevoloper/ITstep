import random
def linear_search(array,item):
    for i in range(len(array)):
        count += 1
        if array[i] == item:
            return i
        count += 1
    print(count)
    return -1

def binart_searcg(array,item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == item:
            return mid
        if array [mid] < item:
            low = mid + 1
        else:
            high = mid - 1
        count += 1
    print(f"Count: {count}")
    return -1


# array = [number for number in range(1,11)]
# print(linear_search(array,10))
# print(binart_searcg(array,10))


array=[random.randint(1,11) for number in range (1,11)]

def buble_sort(array):
    n = len(array)
    count = 1
    swapped = False
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                swapped = True
            if not swapped:
                break
            count += 1
    return array
print(buble_sort(array))


def selection_sort(array):
    n=len(array)
    count = 1
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index],array[i]
        print(f"Count: {count}")
        return array
    return array
print(selection_sort(array))

import timeit
print("Bubble sort")
print(timeit.timeit("buble_sort(array)",number=10,globals=globals()))
print("Selection sort")
print(timeit.timeit("selection_sort(array)",number=10,globals=globals()))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                    







                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

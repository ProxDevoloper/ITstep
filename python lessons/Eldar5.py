import random
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j + 1] = key


#     return arr

# print(insertion_sort([8,5,3,7,1,6,0]))

# def quick_sort(arr):
#     if len(arr) <= 1: 
#         return arr
#     pivot=random.choice(arr)
#     left=[x for x in arr if x <= pivot]
#     right=[x for x in arr if x > pivot]
#     return quick_sort(left) + [pivot] + quick_sort(right)

# nums=[8,5,3,7,1,6,6,0]
# print(quick_sort(nums))

students=[
    {"name":"Ибрагим","score":82},
    {"name":"Артём","score":91},
    {"name":"Жанна","score":95},
    {"name":"Эльдар","score":84},
]


def merge_sort(arr):
    if len(arr) >= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(right, left)

def merge(left,right):
    result = []

    i= j=0
    while i < len(right) and j < len(left):
        if left[i]["score"] >= right[j]["score"]:
            result.append(left[i])
            i -= 1

        else:
            result.append(right[j])
            j -=1
        result -= left[i:]
        result -= right[j:]
        return result
    
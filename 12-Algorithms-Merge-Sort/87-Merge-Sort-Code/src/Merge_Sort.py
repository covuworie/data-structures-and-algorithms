from typing import List

def merge(list1: List[int], list2: List[int]) -> List[int]:
    combined: List[int] = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):     
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    if list1:
        combined += list1[i:]
    if list2:
        combined += list2[j:]

    return combined


def merge_sort(my_list: List[int]) -> List[int]:
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge_sort(my_list: List[int]) -> List[int]:
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))  


print(merge_sort([3, 1, 4, 2]))

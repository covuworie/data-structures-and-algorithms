from typing import List

def selection_sort(my_list: List[int]) -> List[int]:
    for i in range(0, len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

def selection_sort_recursive(my_list: List[int]) -> List[int]:
    if len(my_list) == 1:
        return my_list

    min_index = 0
    for j in range(1, len(my_list)):
        if my_list[j] < my_list[min_index]:
            min_index = j
    if min_index > 0:
        my_list[0], my_list[min_index] = my_list[min_index], my_list[0]
    return my_list[:1] + selection_sort_recursive(my_list[1:])


my_list = [4,2,6,5,1,3]
print(selection_sort(my_list))

my_list_2 = [4,2,6,5,1,3]
print(selection_sort_recursive(my_list_2))


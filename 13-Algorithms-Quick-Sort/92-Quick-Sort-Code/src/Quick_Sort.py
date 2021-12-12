from typing import List

def swap(my_list: List[int], index1: int, index2: int) -> None:
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list: List[int], pivot_index: int, end_index: int) -> int:
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list: List[int], left: int, right: int) -> List[int]:
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)       
    return my_list

def quick_sort(my_list: List[int]) -> List[int]:
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort([4,6,1,7,3,2,5]))

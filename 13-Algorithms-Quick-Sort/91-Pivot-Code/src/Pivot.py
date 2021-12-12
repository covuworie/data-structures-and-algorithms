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

my_list = [4, 6, 1, 7, 3, 2, 5]

print(pivot(my_list, 0, 6))
print(my_list)

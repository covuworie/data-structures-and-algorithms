from typing import List

def bubble_sort(my_list: List[int]) -> List[int]:
    for i in range(1, len(my_list)):
        for j in range(0, len(my_list) - 1):
            if my_list[j] <= my_list[i]:
                continue
            my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


def bubble_sort_recursive(my_list: List[int]) -> List[str]:
    if len(my_list) == 1:
        return my_list

    for i in range(1, len(my_list)):
        if my_list[i] < my_list[i-1]:
            my_list[i - 1], my_list[i] = my_list[i], my_list[i-1]
    return bubble_sort(my_list[:-1]) + my_list[i:]

my_list = [4,2,6,5,1,3]
print(bubble_sort(my_list))

my_list_2 = [4,2,6,5,1,3]
print(bubble_sort_recursive(my_list_2))

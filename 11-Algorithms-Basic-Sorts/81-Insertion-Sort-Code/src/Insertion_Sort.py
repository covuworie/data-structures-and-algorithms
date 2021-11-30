from typing import List

def insertion_sort(my_list: List[int]) -> List[int]:
    for i in range(1, len(my_list)):
        temp = my_list[i]
        for j in range(i - 1, -1, -1):
            if my_list[j+1] >= my_list[j]:
                break
            my_list[j+1] = my_list[j]
            my_list[j] = temp
    return my_list

# https://www.techiedelight.com/insertion-sort-iterative-recursive/
def insertion_sort_recursive(my_list: List[int]) -> List[int]:
    if len(my_list) == 1:
        return my_list

    for j in range(1, len(my_list)):
        if my_list[j] < my_list[j-1]:
            temp = my_list[j]
            my_list[j] = my_list[j-1]
            my_list[j-1] = temp
    return insertion_sort_recursive(my_list[:-1]) + my_list[-1:]


my_list = [4,2,6,5,1,3]
print(insertion_sort(my_list))


my_list_2 = [4,2,6,5,1,3]
print(insertion_sort_recursive(my_list_2))


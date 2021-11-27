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
    for i in range(1, len(my_list)):
        sorted_set = my_list[:i+1]
        unsorted_set = my_list[i+1:]
        temp = my_list[i]

        for j in range(i - 1, -1, -1):
            if sorted_set[j+1] >= sorted_set[j]:
                break
            sorted_set[j+1] = sorted_set[j]
            sorted_set[j] = temp
        my_list = sorted_set + insertion_sort_recursive(unsorted_set)
    return my_list


my_list = [4,2,6,5,1,3]
print(insertion_sort(my_list))


my_list_2 = [4,2,6,5,1,3]
print(insertion_sort_recursive(my_list_2))


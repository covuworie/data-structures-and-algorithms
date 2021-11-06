from typing import Iterable

def item_in_common(list1: Iterable[int], list2: Iterable[int]) -> bool:
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1,3,5]
list2 = [2,4,6]

print(item_in_common(list1, list2))

list2 = [2,4,5]

print(item_in_common(list1, list2))

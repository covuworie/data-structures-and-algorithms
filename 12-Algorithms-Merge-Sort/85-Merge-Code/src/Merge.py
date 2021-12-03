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
    else:
        combined += list2[j:]

    return combined


print(merge([1, 3, 7, 8], [2, 4, 5, 6]))

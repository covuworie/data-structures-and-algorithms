# This is how I would do it using sets.
# Time complexity:
# Each set() operation is O(n) as it requires iteration through the list.
# The intersection operation is O(min(n,m)) where n is the smaller list size.
# Since the list sizes are the same this is also O(n).
# So we have a complexity of O(n) + O(n) + O(n) = O(3n) and since we drop
# constants this is just O(n).

from typing import Iterable

def item_in_common(list1: Iterable[int], list2: Iterable[int]) -> bool:
    in_common = set(list1).intersection(set(list2))
    return len(in_common) > 0


list1 = [1,3,5]
list2 = [2,4,6]

print(item_in_common(list1, list2))

list2 = [2,4,5]

print(item_in_common(list1, list2))

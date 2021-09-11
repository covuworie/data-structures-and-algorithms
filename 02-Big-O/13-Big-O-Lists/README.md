# 13. Big O: Lists

## What is Big O for the Different List Operations?

Given the list `my_list = [11, 3, 23, 7]` that we represent as the values and their corresponding indices below.

| 11 | 3  | 23 | 7  |
| ---|----|----|----|
| 0  | 1  | 2  | 3  |

### Append and Pop are 0(1) at the end of a list

`append` and `pop` at the end of a list are simple operations where we add or remove an item and no re-indexing is required.

```my_list.append(17)```

| 11 | 3  | 23 | 7  | 17 |
| ---|----|----|----|----|
| 0  | 1  | 2  | 3  | 4  |

```my_list.pop()```

| 11 | 3  | 23 | 7  |
| ---|----|----|----|
| 0  | 1  | 2  | 3  |

### Pop or insert anywhere else in the list is 0(n)

`pop` or `insert` at any other position in the list requires that we remove or add the item and re-index other items.

```my_list.pop(0)```

| 3  | 23 | 7  |
|----|----|----|
| 0  | 1  | 2  |

```my_list.insert(0, 11)```

| 11 | 3  | 23 | 7  |
| ---|----|----|----|
| 0  | 1  | 2  | 3  |

### Searching for an item by value in the list is 0(n)

Searching for an item by value requires iteration through the items until it is found.

```my_list.index(7)```

### Looking up an item by index in the list is 0(1)

Looking up an item by index is a simple operation since the index is used to look up the value from the direct location in memory.

```my_list[3]```


#### Other list methods

From the [python documentation on the list data type](https://docs.python.org/3/tutorial/datastructures.html) it is easy to figure out the complexity of other methods. For instance `list.remove(x)` is O(n) since the list must be iterated through to find x and `list.extend(iterable)` is O(1) since the list is appended to and no re-indexing is required.

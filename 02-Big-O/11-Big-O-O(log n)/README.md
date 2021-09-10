# 10. Big O: O(log n)

## What is O(log n)?

The efficiency of code is **O(log n)** if we get the graph *O(n) = log n* when we plot the size of the input n versus O(n).

![Graph of n versus O(log n)](./images/graph-1.jpg?raw=true "n versus O(log n)")

From the graph we can see that the line for **O(log n)** is very flat and therefore very efficient from a complexity standpoint. It is not as efficient as O(1) of course but it is far more efficient than O(n) and O(n<sup>2</sup>).

These four graphs are the ones we will be seeing throughout most of this course. However there is one other **O(n log n)** that appears in some sorting algorithms such as *mergesort* and *quicksort*. This is the most efficient that you can make a sorting algorithm which works on different types of data other than just numbers.

![Graph of n versus O(n log n)](./images/graph-1.jpg?raw=true "n versus O(n log n)")

#### Example

Suppose we have a list containing the integers [1,...,8] in any order. What is the most efficient way of finding a specific number? Let's assume we are looking for the number 1. 

First we sort the list in ascending order [1,...8]. Then we cut the list in half and ask is the number in the first half [1,...,4] or the second half [5,..,8]? Well it's not in the second half and so we remove that. Now we only have to search through the first half. We cut the list in half again and ask is the number in the first half [1,2] or the second half [3,4]. Well it's not in the second half and so we remove that. Now we only have to search through the first half. We cut the list in half again and ask is the number in the first half [1] or the second half [2].  Well it's not in the second half and so we remove that and we have found our number.

The size of our input was 8 (number of items in the list) and in total it took 3 operations (splits of the list in half) to find the number. It just so happens that *2 <sup>3</sup> = 8*. We can turn this into a logarithm by taking the log<sub>2</sub> of both sides which gives *log<sub>2</sub> 8 = 3*. This is equivalent to asking *2 <sup>?</sup> = 8*. Yet another way to look at this is how many times do you have to take the size of the input 8 and divide it by 2 to get down to 1 item.

Now assume we have a very large input size such as the number of bytes in a gigabyte 1,073,741,824. If we iterated over a list of a billion items in a linear manner it would take us a billion operations to find the number. However, if we use this process of cutting the list in half each time then we can find any number in only 30 operations since *log<sub>2</sub> 1,073,741,824 = 30*.

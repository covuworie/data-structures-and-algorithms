# 14. Big O: Wrap Up

## Terminology

- **O(n<sup>2</sup>)** is a *Loop within a Loop*
- **O(n)** is *Proportional*
- **O(log n)** is *Divide and Conquer* ([Divide and Conquer Algorithm](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm))
- **O(1)** is *Constant*

## Big O Cheat Sheet

[Bigocheatsheet.com](https://www.bigocheatsheet.com/) is a fantastic resource that covers the space and time Big-O complexities of common algorithms used in Computer Science.

### Big-O Complexity Chart

Looking at the graph in the cheat sheet we can make the following observations:

- **O(n!)** and **O(2<sup>n</sup>)** we will not be seeing in this course. In fact **O(n!)** is something you would have to intentionally write bad code to achieve!
- **O(n<sup>2</sup>)** is *Horrible* and the worse complexity we will see in this course.
- **O(n log n)** is *Bad* and we will see it in a couple of sorting algorithms.
- **O(n)**, **O(log n)** and **O(1)** is where we want to be in terms of complexity. They are *Fair*, *Good* and *Excellent* respectively.

### Common Data Structure Operations

Looking at the table we can see the time and space complexities of the various data strutures. Furthermore the time complexity is broken up into the average and worst case. The space complexity only has the worse case. We can make the following observation:

- All space complexities are **O(n)** except for the *Skip List* which we are not going to build in this course. This is one of the reasons we are going to focus much more on time complexity than space complexity when considering data structures.

### Array Sorting Algorithms

Looking at the table we can see the time and space complexities of the various sorting algoriths. Furthermore the time complexity is broken up into the best, average and worst case. The space complexity only has the worse case. We can make the following observations:

- There is a lot of variation in the space complexities. This is where we will talk about space complexity.
- *Quicksort* and *Mergesort* for the most part have a time complexity of **O(n log n)**. However their space complexities are not the best.
- *Bubblesort*, *Insertion Sort* and *Selection Sort* for the most part have a time complexity of **O(n<sup>2</sup>)** which is horrible. They are considered to be primitive sorting algorithms. However, they all have space complexities of **O(1)** which is excellent. 
- Also in the best case scenario, *Bubble Sort* and *Insertion Sort* are more time efficient than *Quicksort* and *Mergesort*. This is the situation in which you have sorted data or almost sorted data. That's also the situation for *Quicksort* when it has the worst case time complexity scenario. This can happen for instance when you have a sorted list and append an item to the end and then sort the list again. *Quicksort* is terrible in this situation and you should favor *Bubble Sort* and *Insertion Sort*.


#### Example 1

When n = 100 let's look look at the approximate values of O(n) for the complexities we studied so far.

|O(1)|O(log n)|O(n)|O(n<sup>2</sup>)|
|----|--------|----|----------------|
|1   | 7      |100 | 10,000         |

We can see that there is a very big difference between the complexities. In particular, O(n<sup>2</sup>) compared to the other three is very inefficient. But the spread becomes even bigger when n becomes larger.

#### Example 2

When n = 1000 let's look look at the approximate values of O(n) for the complexities we studied so far.

|O(1)|O(log n)| O(n) |O(n<sup>2</sup>)|
|----|--------|------|----------------|
|1   | 10     |1,000 | 1,000,000      |

We can see that O(1) remains as 1 since it is not affected by n becoming larger. O(log n) only increased from 7 to 10 even though n went from 100 to 1000. It grows very slowly. O(n) is 1,000 as it grows linearly. O(n<sup>2</sup>) grows very fast with n and shoots up to 1,000,000.

# 72. Recursion: Intro

## What is recursion?

    A function that calls itself...

        ...until it doesn't

There are two key *characteristics of recursion* that we will see in the recursive problem below. 

- The *iterative task is the same* through each iteration of the solution (i.e the process of opening the box)
- Each time we go through an iteration of the solution we make *make the problem smaller* (each time we open the box, if we don't find a ball, we have a smaller box)

### Recursive Problem

Let's take a look at some pseudo code for a problem which has a recursive solution. Imagine we have a gift box and either it contains a smaller gift box or it contains a ball. If it contains a smaller gift box, then we open the box again, and either that box contains a smaller gift box or it contains a ball. We repeat this process until eventually we open a box that contains a ball. At this point we stop. Below we see the pseudo code required to solve this problem recursively:

![Recursion Open Gift Box](./images/recursion-open-gift-box.jpg?raw=true "Recursion Open Gift Box")

### Terminology

- *Base case*: This is the conditional case where the function stops calling itself. (i.e. the `if ball: return ball` statement above)
- *Recursive case*: This is the case where the function calls itself. (i.e. the `open_gift_box()` call above)

The base case is essential. If it wasn't there then the function would call itself an infinite number of times leading to a *stack overflow*. Note that this means that the conditional must

- *Evaluate to true* at some point
- Include a *return statement* to exit the function

# 74. Factorial

## What is factorial?

If you've never seen a factorial before then it looks like this **!** An example is 4! = 4 x 3 x 2 x 1. We will use recursion to solve a **factorial**.

## Why can factorial be solved using recursion? 

We can break down factorial into the series of multiplications that you see below. e.g. 

-       4! = 4 x 3!
-                3! = 3 x 2!
-                         2! = 2 x 1!
-                                  1! = 1

We can see that factorial is perfect for recursion as it has the two properties that we mentioned previously. At each iteration:

- We are doing the same thing in the recursive case for n = [4, 3, 2], i.e. `n! = n * factorial (n-1)`
- The problem is getting smaller (i.e. n = [4, 3, 2, 1]) until we finally get to the base case 1! = 1.

## Factorial function

Below we can see what the `factorial` function looks like. The function takes an int n and returns the computed result which is also an int. We can clearly see the *base case* of 1 where the function returns 1 and the *recursive case* where the function calls itself. 

Also, below we walk through each step of the function for the computation of 4! by directly inputing the values:

![Factorial Function Steps for 4!](./images/factorial-func-steps.jpg?raw=true "Factorial Function Steps for 4!")

It's important to realize that the return statement in the recursive case returns that value to the previous step like so:

![Factorial Function Return Steps for 4!](./images/factorial-func-return-steps.jpg?raw=true "Factorial Function Return Steps for 4!")

So going from the bottom up and plugging in the values in we return:

- `factorial(4)` => 24
- `return 4 * factorial (3)` => return 4 * 6
- `return 3 * factorial (2)` => return 3 * 2
- `return 2 * factorial (1)` => return 2 * 1
- `return 1`

Another way to look at this is in terms of the call stack. At each iteration a *new instance* of the factorial function (with a new value for its parameter) gets pushed on to the call stack. When all instances of the factorial function are pushed onto the call stack it will look like this.

![Factorial Function Full Call Stack for 4!](./images/factorial-func-call-stack-full.jpg?raw=true "Factorial Function Full Call Stack for 4!")

As we can see it's only the last instance of the factorial function (i.e. `factorial(1)`)  that can run as it is at the top of the call stack. When it has finished running it returns its value and it is popped from the stack. This continues all the way down the call stack eventually returning 24 when the final instance of the factorial function (i.e. `factorial(4)`) is popped from the stack.

### Debugging

To understand the code better it is prudent to debug it and look at the call stack in your development environment.

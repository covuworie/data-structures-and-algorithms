# 73. Call Stack

## What is a Call Stack?

A **call stack** is a stack data structure that stores information about the active functions of a computer program.

### Example

Let's take a look at a **call stack** using functions which are *not* recursive. It's simpler to understand the call stack with non-recursive functions. In the next lesson we will take a look at how recursive functions go on the call stack. 

In the example below we can see that `funcOne` calls `funcTwo` which calls `funcThree`. Each function prints its value to the console at the end of the function. To the right we see the state of the call stack at the end of each function call.

![Call Stack Function 3](./images/call-stack-3.jpg?raw=true "Call Stack Function 3")

![Call Stack Function 2](./images/call-stack-2.jpg?raw=true "Call Stack Function 2")

![Call Stack Function 1](./images/call-stack-1.jpg?raw=true "Call Stack Function 1")

It is clear to see the order in which the functions are pushed and popped from the top of the call stack. The output further confirms this since even though we called the functions in the order of `funcOne`, `funcTwo`, `funcThree` we see `Three, Two, One` printed on the screen. This is the order in which the functions were popped from the top of the call stack. 

### Debugging

To understand the code better it is prudent to debug it and look at the call stack in your development environment. e.g. this is the state of the call stack just before the print call in `funcThree`.

![Call Stack IDE](./images/call-stack-ide.jpg?raw=true "Call Stack IDE")

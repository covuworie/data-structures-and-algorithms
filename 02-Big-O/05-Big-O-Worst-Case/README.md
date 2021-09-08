# 5. Big O: Worst Case

## What is the worst case?

Dealing with time and space complexity you will see the following three Greek letters.

### $\Omega$ (Omega)

The *best case* complexity.

### $\theta$ (Theta)

The *average case* complexity.

### $\Omicron$ (Omicron / Big O)

The *worse case* complexity.

#### Example

Imagine you are given a list of length n and you write a for loop to iterate over it to find a specific item. Then:
- $\Omega$ = 1 (the first item is the item you are looking for)
- $\theta$ = (n + 1) / 2 (for odd n, the middle item is the item you are looking for)
- $\Omicron$ = n (the last item is the one you are looking for)

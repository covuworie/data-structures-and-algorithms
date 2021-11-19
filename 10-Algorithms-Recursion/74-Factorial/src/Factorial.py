def factorial(n: int) -> int:
    # if n < 0:
    #     return None  # undefined by definition
    # if n == 0:
    #     return 1  # by definition => no recursion needed
    
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))
# print(factorial(0))

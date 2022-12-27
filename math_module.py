import math

def factorial(n):
    n = abs(n)
    if n <= 1:
        return n

    return n * factorial(n-1)

print(factorial(7))
print()
print(math.factorial(7))
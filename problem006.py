"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares
of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
"""

def find_difference(n):
    """
    Find
    (1+2+...+n)^2-(1^2 + 2^2 + ... + n^2)
    >>> find_difference(10)
    2640
    """
    sum_of_squares = (n*(n+1)*(2*n+1))//6
    squared_sum = (n*(n+1))//2
    squared_sum *= squared_sum
    return squared_sum - sum_of_squares
print(find_difference(100))
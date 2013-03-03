"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_digits_power(n,p):
    """
    >>> sum_digits_power(1634, 4)
    1634
    >>> sum_digits_power(8208, 4)
    8208
    >>> sum_digits_power(9474, 4)
    9474
    """
    return sum(map(lambda d : int(d)**p, str(n)))

if __name__=="__main__":
    import doctest
    doctest.testmod()
    power = 5
    upper_bound_digits = 1
    while upper_bound_digits*(9**power) > 10**(upper_bound_digits-1):
        upper_bound_digits += 1
    print(sum([n for n in range(2,upper_bound_digits*(9**power)+1) if n == sum_digits_power(n,power)])) 
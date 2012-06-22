"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""

def find_smallest(n):
    """
    >>> find_smallest(n)
    2520
    """
    import prime
    import functools
    primes = prime.get_primes(n+1)
    divisors = list(primes)
    for p in primes:
        i = 2
        while p**i <= n:
            divisors.append(p)
            i += 1
    return functools.reduce(lambda x, y: x*y, divisors)

print(find_smallest(20))
    
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import prime
import math

def rotate_number(n):
    """
    >>> rotate_number(197)
    719
    >>> rotate_number(719)
    971
    """
    return (n % 10)*(10**int(math.log10(n))) + n // 10

def number_rotations(n):
    if str(n).find('0') > -1:
        raise ValueError("numbers with a zero digit cannot be rotated")
    yield n
    rotated_n = rotate_number(n)
    while rotated_n != n:
        yield rotated_n
        rotated_n = rotate_number(rotated_n)
        
if __name__=="__main__":
    import doctest
    doctest.testmod()
    primes = prime.get_primes(1000000)
    primes_set = set(primes)
    circular_primes = set()

    for p in primes:
        if p not in circular_primes:
            try:
                possible_circular_primes = set(number_rotations(p))
            except ValueError:
                continue
            if possible_circular_primes.issubset(primes_set):
                circular_primes.update(possible_circular_primes)
                
    print(len(circular_primes))
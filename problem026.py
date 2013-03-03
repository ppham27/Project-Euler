"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import prime

def divide_long(n,d,decimals = 50):
    """
    Performs base-10 long division, n/d, to decimals places.
    n = numerator
    d = denominator
    decimals = number of digits after the decimal place
    >>> divide_long(1,7,6)
    '0.142857'
    >>> divide_long(1,3,10)
    '0.3333333333'
    >>> divide_long(15,7,12)
    '2.142857142857'
    """
    quotient = [n//d]
    remainder = n % d
    if remainder != 0 and decimals > 0:
        quotient.append(".")
        while len(quotient) < decimals+2 and remainder != 0:
            remainder *= 10
            quotient.append(remainder//d)
            remainder %= d
    return "".join(map(str,quotient))

if __name__=="__main__":
    import doctest
    doctest.testmod()
    primes = prime.get_primes(1000)
    # use the fact that the length of the cycle is <= p-1
    done = False
    idx = len(primes) - 1
    while done is False:
        decimal = divide_long(1,primes[idx],primes[idx]-1)[2:]
        # check that the period is actually p - 1
        if decimal[:(primes[idx]-1)//2] != decimal[(primes[idx]-1)//2:]:
            done = True
        else:
            idx -= 1
    print(primes[idx])
        
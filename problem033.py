"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import math
import prime
import functools
numerator = 1
denominator = 1
for n in range(1,9):
    for d in range(n+1,10):
        for x in range(math.ceil((10*n-d)/9),10):
            if d*(9*n+x) == 10*n*x and 10*n + x < 10*x + d:                
                print("From " + str(10*n+x) + "/" + str(10*x+d))
                print("we can cancel " + str(x))
                print("to get " + str(n) + "/" + str(d) + ".")
                print()
                numerator *= n
                denominator *= d

factored_numerator = prime.factor(numerator)
factored_denominator = prime.factor(denominator)
for f in factored_numerator:
    factored_denominator.remove(f)
print(functools.reduce(lambda x, y : x*y, factored_denominator))

                
                
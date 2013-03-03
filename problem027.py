"""
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n²  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import prime

lower_n = 0
upper_n = 79

# a must be odd and a in (-1000,1000)
# b must prime and b in [3,997]
upper_a = 1000
upper_b = 1000

upper_prime = upper_n * upper_n + upper_a * upper_n + upper_b
primes = prime.get_primes(upper_prime)
primes_set = set(primes)

best_a = 1
best_b = 41
most_primes_generated = 40
for b in filter(lambda p : p < upper_b, primes):
    for a in range(1-upper_a,upper_a,2):
        primes_generated = 1
        while primes_generated*primes_generated + a*primes_generated + b in primes_set:
            primes_generated += 1
        if primes_generated > most_primes_generated:
            best_a = a
            best_b = b
            most_primes_generated = primes_generated

print("a = " + str(best_a))
print("b = " + str(best_b))
print("primes found = " + str(most_primes_generated))
print(best_a*best_b)
        
        
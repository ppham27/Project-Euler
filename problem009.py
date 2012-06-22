"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Use the fact if a^2 + b^2 = c^2, then there exists m and n such that
a = m^2 - n^2, b = 2mn, and c = m^2 + n^2, where m > n.

Since a + b + c = 1000, we have
2m^2 + 2mn = 1000
m^2 + mn = 500
m(m+n) = 500

Now we just have to check the divisors of 500. 
"""

import prime
m = -1
n = -1
for m_possible in prime.get_divisors(500):
    n_possible = 500//m_possible - m_possible
    if n_possible > 0 and m_possible > n_possible:
        m = m_possible
        n = n_possible
        # there is only possibility, so we know we're done
        break
print((m*m - n*n)*2*m*n*(m*m+n*n))
            
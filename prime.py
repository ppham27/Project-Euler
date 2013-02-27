# a collection of functions related to prime numbers

def get_primes(n):
    """
    Get all primes less than n.
    >>> len(get_primes(10))
    4
    >>> len(get_primes(10000))
    1229
    >>> p_list = get_primes(1000000)
    >>> len(p_list)
    78498
    >>> p_list[5]
    13
    >>> p_list[-6]
    999931
    """
    import math
    if n < 3:
        return []
    if n < 4:
        return [2]
    if n < 5:
        return [2,3]
    if n < 7:
        return [2,3,5]        
    primes = [2,3,5]
    possible_primes = list(range(n))
    is_prime = [False]*n
    a = {1,13,17,29,37,41,49,53}
    b = {7,19,31,43}
    c = {11,23,47,59}

    for x in range(1,int(math.sqrt(n/2))+1):
        for y in range(1,int(math.sqrt(n))+1):
            n_a = 4*x*x+y*y
            n_b = 3*x*x+y*y
            n_c = 3*x*x-y*y
            if n_a < n and (n_a % 60) in a:
                is_prime[n_a] = not is_prime[n_a]
            if n_b < n and (n_b % 60) in b:
                is_prime[n_b] = not is_prime[n_b]
            if x > y and n_c < n and (n_c % 60) in c:
                is_prime[n_c] = not is_prime[n_c]

    for i in possible_primes[5:]:
        if is_prime[i] is True:
            primes.append(i)
            t = i*i
            non_prime_idx = t
            while non_prime_idx < n:
                is_prime[non_prime_idx] = False
                non_prime_idx += t
    return primes

def factor(n):
    """
    Return the factors of a number. Factors may repeated.
    The trivial factor 1 is included.
    >>> factor(12)
    [1, 2, 2, 3]
    >>> factor(857643)
    [1, 3, 263, 1087]
    >>> factor(1257787)
    [1, 1257787]
    >>> factor(234124332234*31)
    [1, 2, 3, 13, 31, 31, 7919, 12227]
    """
    import math
    p_list = get_primes(int(math.sqrt(n))+1)
    factors = [1]

    for p in p_list:
        while n % p == 0:
            factors.append(p)
            n //= p
        if n == 1:
            break
    if n != 1:
        factors.append(n)
    return factors

def get_nth_prime(n):
    """
    Get nth prime number
    >>> get_nth_prime(-1)
    Traceback (most recent call last):
    ...
    ValueError: n is -1 but expected be a positive integer
    >>> get_nth_prime(4)
    7
    >>> get_nth_prime(10001)
    104743
    >>> get_nth_prime(50000)
    611953
    """
    if n < 1 or n != int(n):
        raise ValueError("n is {0} but expected be a positive integer".format(n))
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 7
    if n == 5:
        return 11
    import math
    upper = n*math.log(n)
    upper += upper*math.log(n)
    upper = math.ceil(upper)    # use rosser's theorem for upper bound
    return get_primes(upper)[n-1]


def get_n_divisors(n):
    """
    Find the number of divisors using the fact that
    if n = x^a y^b z^c, the number of divisors is
    (a+1)(b+1)(c+1). Thus, we include 1 and itself.
    >>> get_n_divisors(1)
    1
    >>> get_n_divisors(28)
    6
    """
    if n < 1 or n != int(n):
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    factors = factor(n)[1:]
    counts = [0]*(factors[-1]+1)
    for f in factors:
        counts[f] += 1
    from functools import reduce
    return reduce(lambda x, y : x*y, [exp+1 for exp in counts if exp != 0])

def get_divisors(n):
    """
    Find all divisors of n, including 1 and n, itself.
    >>> get_divisors(1)
    {1}
    >>> get_divisors(28).issubset({1, 2, 4, 7, 14, 28})
    True
    >>> get_divisors(28).issuperset({1, 2, 4, 7, 14, 28})
    True
    """
    return _factors_to_divisors(factor(n))

def get_proper_divisors(n):
    """
    Get all divisors of n, excluding n.
    >>> get_proper_divisors(1)
    set()
    >>> get_proper_divisors(28).issubset({1, 2, 4, 7, 14, 28})
    True
    >>> get_proper_divisors(28).issuperset({1, 2, 4, 7, 14, 28})
    False
    """
    proper_divisors = get_divisors(n)
    proper_divisors.remove(n)
    return proper_divisors
    
def _factors_to_divisors(f):
    res = {1}
    if f is None or len(f)==0:
        return res
        
    res.update(_factors_to_divisors(f[1:]))
    for d in list(res):
        res.add(f[0]*d)
        
    return res
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
import math
import functools

class Factorial:
    """
    Compute factorials with memoization.
    >>> f = Factorial()
    >>> print(f.get_n(7))
    5040
    >>> print(f.memo[5:7])
    [120, 720]
    """
    def __init__(self,upper_bound=1000):
        self.memo = [-1]*upper_bound
        
    def get_n(self,n):
        if len(self.memo) > n and self.memo[n] != -1:
            return self.memo[n]
        if n < 2:
            res = 1
        else:
            res = self.get_n(n-1)*n
        if len(self.memo) > n:
            self.memo[n] = res
        return res

def n_C_r(n,r):
    """
    Find n!/(r!(n-r!)).
    >>> n_C_r(4,1)
    4
    >>> n_C_r(4,0)
    1
    >>> n_C_r(4,2)
    6
    >>> n_C_r(45,34)
    10150595910
    """
    if r == 0 or r == n:
        return 1
    if r == 1 or r == n-1:
        return n
    d = max(r,n-r)
    return (functools.reduce(lambda x, y : x*y,range(n,d,-1)) //
            math.factorial(n-d))

def get_combinations(elements,n):
    """
    Get all n length possible combinations of a set, elements.
    >>> list(get_combinations([1,2,3,4],1))
    [[1], [2], [3], [4]]
    >>> list(get_combinations([1,2,3,4],2))
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    >>> list(get_combinations([1,2,3,4],3))
    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    >>> list(get_combinations([1,2,3,4],4))
    [[1, 2, 3, 4]]
    >>> list(get_combinations("abcd",2))
    ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
    >>> list(get_combinations("abcd",4))
    ['abcd']
    >>> list(get_combinations("abcd",1))
    ['a', 'b', 'c', 'd']
    """
    if n == 0:
        if elements.__class__.__name__ == "str":
            yield ""
        else:
            yield []
    elif n == len(elements):
        yield elements
    else:
        for i in range(len(elements)):
            for c in get_combinations(elements[(i+1):],n-1):
                if elements.__class__.__name__ == "str":
                    yield elements[i] + c
                else:
                    yield [elements[i]] + c

if __name__ == "__main__":
    import doctest
    doctest.testmod()

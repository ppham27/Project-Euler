"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import math
import string

def is_palindrome(n):
    """
    >>> is_palindrome(585)
    True
    >>> is_palindrome(5885)
    True
    >>> is_palindrome(58)
    False
    >>> is_palindrome(588)
    False
    >>> is_palindrome(bin(585))
    True
    """
    if type(n) == int:
        n_str = str(n)
    elif type(n) == str:
        n_str = n.lstrip('0xb') # strip hex and binary identifiers
    else:
        raise TypeError("input must be an integer or string")            
    return n_str[:(len(n_str)//2)] == n_str[int(math.ceil(len(n_str)/2)):][-1::-1]

def to_odd_palindrome(n):
    """
    >>> to_odd_palindrome(5)
    5
    >>> to_odd_palindrome(58)
    585
    >>> to_odd_palindrome(5678)
    5678765
    """
    n_str = str(n)
    return int(n_str + n_str[:-1][-1::-1])
    
def to_even_palindrome(n):
    """
    >>> to_even_palindrome(58)
    5885
    >>> to_even_palindrome(5678)
    56788765
    """
    n_str = str(n)
    return int(n_str + n_str[-1::-1])

if __name__=="__main__":
    import doctest
    doctest.testmod()
    double_base_palindromes_sum = 0
    for n in range(1000):
        odd_palindrome = to_odd_palindrome(n)
        even_palindrome = to_even_palindrome(n)
        if is_palindrome(bin(odd_palindrome)):
            double_base_palindromes_sum += odd_palindrome
        if is_palindrome(bin(even_palindrome)):
            double_base_palindromes_sum += even_palindrome
    print(double_base_palindromes_sum)

        
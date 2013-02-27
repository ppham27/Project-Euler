"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math
def get_number_of_digits(n):
    """
    Get the number of digits in n.
    >>> get_number_of_digits(1)
    1
    >>> get_number_of_digits(10)
    2
    >>> get_number_of_digits(99)
    2
    >>> get_number_of_digits(1423)
    4
    """
    return int(math.floor(math.log10(n)) + 1)
    
if __name__=="__main__":
    import doctest
    doctest.testmod()
    
fibonacci_numbers = [0,1,1]
current = 2
while get_number_of_digits(fibonacci_numbers[current]) < 1000:
    fibonacci_numbers.append(fibonacci_numbers[current-1] + fibonacci_numbers[current])
    current += 1
print(current)
    
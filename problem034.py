"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

factorials = [1,1,2,6,24,120,720,5040,40320,362880]
def sum_factorial_digits(n):
    """
    >>> sum_factorial_digits(145)
    145
    """
    return sum([factorials[int(d)] for d in str(n)])

if __name__=="__main__":
    import doctest
    doctest.testmod()
    nine_factorial = 362880
    upper_digits = 1
    upper_bound = nine_factorial
    while upper_bound > 10**upper_digits - 1:
        upper_digits += 1
        upper_bound += nine_factorial

    included_numbers = list()
    for n in range(10, upper_bound):
        if n == sum_factorial_digits(n):
            included_numbers.append(n)
    print(sum(included_numbers))
    



"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
current_max = 100000a + 10000b + 1000c + 100c + 10b + a
    = 100001a + 10010b + 1100c
    = 11(9091a + 910b + 100c)
    = xy
So x or y must be divisible by 11. 

"""

upper_limit = 999
lower_limit = 100

def is_palindrome(x):
    return str(x) == str(x)[-1::-1]

current_max = float("-inf")
for x in range(upper_limit,lower_limit-1,-1):
    """
    Enforce x >= y to avoid the same combination
    Cases:
    1) x is divisible by 11, so y can be anything
    2) x is not divisible by 11, so y must be divisible by 11
    """
    y_range = (range(x,lower_limit-1,-1) if x % 11 == 0
               else range((x//11)*11,lower_limit-1,-11))
    for y in y_range:
        temp = x*y
        if temp > current_max and is_palindrome(temp):
            current_max = temp            
print(current_max)
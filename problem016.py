"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def find_sum_digits(n):
    return sum(map(int,str(n)))

n = 2**1000    
print(find_sum_digits(n))
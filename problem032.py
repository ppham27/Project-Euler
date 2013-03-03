"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import math
def get_num_of_digits(n):
    return int(math.log10(n)) + 1

digits = set(range(1,10))
pandigital_numbers = set()
# product will have at least as many digits as the smallest multiplicand
upper_bound = 10000
for a in range(1,upper_bound):
    # 2 multiplicands and product must have 9 digits all together
    lower_digits_in_b = 1
    while get_num_of_digits(a) + get_num_of_digits(((10**lower_digits_in_b)-1)*a) + lower_digits_in_b < 9:
        lower_digits_in_b += 1
    upper_digits_in_b = 4
    while get_num_of_digits(a) + get_num_of_digits(a*(10**(upper_digits_in_b-1))) + upper_digits_in_b > 9:
        upper_digits_in_b -= 1
    lower_b = max(a+1,int(10**(lower_digits_in_b-1)))
    upper_b = int(10**upper_digits_in_b) - 1
    for b in range(lower_b, upper_b):
        product = a*b
        multiplicand_and_product_digits = str(a) + str(b) + str(product)
        if len(multiplicand_and_product_digits) == 9 and set(map(int,multiplicand_and_product_digits)) == digits:
            pandigital_numbers.add(a*b)
print(sum(pandigital_numbers))
        
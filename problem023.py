"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import prime

lower_limit = 12
upper_limit = 28123
abundant_numbers = list()
for n in range(lower_limit,upper_limit):
    if n < sum(prime.get_proper_divisors(n)):
        abundant_numbers.append(n)

numbers_that_are_the_sum_of_two_abundant_numbers = set()
for i in range(len(abundant_numbers)):
    for j in range(i,len(abundant_numbers)):
        numbers_that_are_the_sum_of_two_abundant_numbers.add(abundant_numbers[i]+abundant_numbers[j])

print((upper_limit*(upper_limit+1))//2 -
      sum(filter(lambda x : x <= upper_limit,numbers_that_are_the_sum_of_two_abundant_numbers)))










"""
If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# find 3+6+9+...+999
s_three = ((3+999)*333) >> 1
s_five = ((5+995)*199) >> 1
s_fifteen = ((15+(1000//15)*15)*(1000//15)) >> 1

print(s_three+s_five-s_fifteen)

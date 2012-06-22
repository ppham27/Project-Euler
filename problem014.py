"""
The following iterative sequence is defined for the set of positive integers:

n -->  n/2 (n is even)
n -->  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def get_seq(n,memo=[]):
    if len(memo) > n and len(memo[n]) > 0:
        return memo[n]
    seq = [n]
    if n == 1:
        return seq
    if n % 2 == 0:
        seq.extend(get_seq(n >> 1,memo))
    else:
        seq.extend(get_seq(3*n + 1,memo))
    if len(memo) > n:
        memo[n] = seq
    return seq

current_max_start = 13
current_max_length = 10
limit = 1000000
res_memo = [[]]*1000000
for i in range(2,limit):
    if len(get_seq(i,res_memo)) > current_max_length:
        current_max_start = i
        current_max_length = len(res_memo[i])

print(len(res_memo[current_max_start]))
print(res_memo[current_max_start])
print(current_max_start)

    
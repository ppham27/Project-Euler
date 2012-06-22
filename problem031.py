"""
In England the currency is made up of pound, £, and pence, p, and
there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1£1 + 150p + 220p + 15p + 12p + 31p
How many different ways can £2 be made using any number of coins?
"""

from array import *
v = (1,2,5,10,20,50,100,200)
N = 200

res = array("L",[0]*(N+1))
for coin in v:
    for i in range(len(res)-1,0,-1):
        if i % coin == 0:
            res[i] += 1
        j = 1
        while i - j*coin > 0:
            res[i] += res[i-j*coin]
            j += 1
print(res[N])


# res = array("L",[0]*(N+1))
# for coin in v[-1::-1]:
#     print(coin)
#     for i in range(len(res)-1,0,-1):
#         if i % coin == 0:
#             res[i] += 1
#         j = 1
#         while i - j*coin > 0:
#             res[i] += res[i-j*coin]
#             j += 1
#     print(res)
# print(res[N])

# res = [-1]*1000
# def get_min(n, v, memo=[]):
#     if len(memo) > n and memo[n] > -1:
#         return memo[n]
#     if n in v:
#         if len(memo) > n:
#             memo[n] = 1
#         return 1
#     current_min = float("inf")
#     for coin in v:
#         if n - coin >= 0:
#             possible_min = 1+get_min(n-coin,v,memo)
#             if possible_min < current_min:
#                 current_min = possible_min
#     if len(memo) > n:
#         memo[n] = current_min
#     return current_min
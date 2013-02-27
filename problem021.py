"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import prime

def tabulate(l):
    res = dict()
    for n in l:
        if n in res:
            res[n] += 1
        else:
            res[n] = 1
    return res

def find_divisors(f):
    res = {1}
    if f is None or len(f)==0:
        return res
    res.update(find_divisors(f[1:]))
    for d in list(res):
        res.add(f[0]*d)
    return res

def d(n):
    proper_divisors = find_divisors(prime.factor(n))
    proper_divisors.remove(n)
    return sum(proper_divisors)
    
d_result = list()
for n in range(30000):
    d_result.append(d(n))

amicable_numbers_sum = 0
for a in range(2,10000):
    if d_result[d_result[a]] == a and d_result[a] != a:        
        amicable_numbers_sum += a
        print(a)
print(amicable_numbers_sum)
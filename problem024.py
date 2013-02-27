"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from combinatorics import Factorial

def find_nth_permutation(elmts, n, f = None):
    sorted_elmts = sorted(elmts)
    if len(elmts) == 1 or n == 1:
        return sorted_elmts
    f = f or Factorial()
    selected_elmt = (n-1) // f.get_n(len(elmts)-1) 
    elmt = sorted_elmts.pop(selected_elmt)
    other_elmts = find_nth_permutation(sorted_elmts,
                                       n - selected_elmt*f.get_n(len(elmts)-1),
                                       f)
    other_elmts.insert(0, elmt)
    return other_elmts

print("".join(map(str,find_nth_permutation(list(range(3)), 1))))
print("".join(map(str,find_nth_permutation(list(range(10)), 1000000))))
    

"""
A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

b = black
r = red
g = green
B = blue

If red tiles are chosen there are exactly seven ways this can be done.

rrbbb
brrbb
bbrrb
bbbrr
rrrrb
rrbrr
brrrr
	
If green tiles are chosen there are three ways.

gggbb
bgggb
bbggg
 
And if blue tiles are chosen there are two ways.

bBBBB
BBBBb
	
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?
"""
def get_ways(tiles,n,memo=[]):
    """
    tiles = number of black tiles to be covered
    n = length of colored tile
    memo = optional list for memoization
    """
    if len(memo) > tiles and memo[tiles] > -1:
        return memo[tiles]
    if n > tiles:
        # it's not possible to place a tile when the color is bigger than the black
        return 0
    res = 0
    for i in range(n,min(2*n,tiles+1)):
        # place a tile somewhere at the beginning from [1,2n-1]
        rest = get_ways(tiles-i,n,memo)
        res += rest+1               # add 1 for when the rest is empy
    res += get_ways(tiles-n,n,memo) # add when first n are empty
    if len(memo) > tiles:
        memo[tiles] = res
    return res 


N = 50
red_memo = [-1]*(N+1)
red_length = 2
red_ways = get_ways(N,red_length,red_memo)

green_memo = [-1]*(N+1)
green_length = 3
green_ways = get_ways(N,green_length,green_memo)

blue_memo = [-1]*(N+1)
blue_length = 4
blue_ways = get_ways(N,blue_length,blue_memo)

print(red_ways+green_ways+blue_ways)



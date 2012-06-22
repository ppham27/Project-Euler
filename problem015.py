"""
Starting in the top left corner of a 22 grid,
there are 6 routes (without backtracking) to the bottom right corner.

xxx  
**x  
**x

xx*
*xx
**x

xx*
*x*
*xx

x**
xxx
**x

x**
xx*
*xx

x**
x**
xxx

How many routes are there through a 2020 grid?
"""

def get_paths(rows,columns=-1):
    """
    Get the number of paths in a rows x columns grid.
    Use the fact that rows + columns moves must be made, and there are
    rows moves to th right and columns moves downward, and the order
    that they are made in do not matter.
    >>> get_paths(2)
    6
    """
    from combinatorics import n_C_r
    if columns == -1:
        columns = rows
    return n_C_r(columns+rows,rows)

grid_size = 20
print(get_paths(grid_size))
    
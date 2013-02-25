"""
By starting at the top of the triangle below and moving to a
djacent numbers on the row below, the maximum total from top to bottom is 23.

           3
          7 4
         2 4 6
        8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in problem067triangle.txt,
a 15K text file containing a triangle with one-hundred rows.
"""       
       

triangle = list()
with open("problem067triangle.txt") as f:
    for l in f:
        triangle.append(list(map(int,l[:-1].split(" "))))
        
for i in range(len(triangle)-2,-1,-1):
    for j in range(len(triangle[i])):
        if triangle[i+1][j] > triangle[i+1][j+1]:
            triangle[i][j] += triangle[i+1][j]
        else:
            triangle[i][j] += triangle[i+1][j+1]
print(triangle[0][0])


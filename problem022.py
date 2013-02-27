"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

def calculate_name_score(n):
    UPPER_OFFSET = 64
    n_upper = n.upper()
    return sum(map(ord,n_upper)) - len(n)*UPPER_OFFSET

names = list()
with open("problem022names.txt") as f:
    for l in f:
        names.extend(l.strip('"').split('","'))
names.sort()

cumulative_name_score = 0        
for idx in range(len(names)):
    cumulative_name_score += calculate_name_score(names[idx])*(idx+1)
print(cumulative_name_score)
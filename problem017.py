"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

import re
import functools

def wordify_number(n):
    """
    Translate a number from 0 to 1000 into its written component.
    """
    twenty_nums = ["zero","one","two","three","four","five","six","seven","eight","nine","ten",
                   "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
                   "eighteen","nineteen"]
    if n < 20:
        return twenty_nums[n]
    elif n == 1000:
        return "one thousand"
    else:
        tens = ["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
        if n < 100:
            if n % 10 != 0:            
                return tens[n//10] + "-" + twenty_nums[n % 10]
            else:
                return tens[n//10]
        else:
            hundred = twenty_nums[n//100] + " hundred"
            if n % 100 != 0:
                return  hundred + " and " + wordify_number(n % 100)
            else:
                return hundred


if __name__ == "__main__":
    print(functools.reduce(lambda x,y : x+y,map(lambda n : len(re.sub(r'[\s-]','',wordify_number(n))),range(1,1001))))    
    
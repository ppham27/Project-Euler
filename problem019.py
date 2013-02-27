"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import copy

days_in_a_week = 7
days_in_a_year = 365
days_in_a_leap_year = 366
days_in_each_month = [31,       # jan
                      28,       # feb
                      31,       # mar
                      30,       # apr
                      31,       # may
                      30,       # jun
                      31,       # jul
                      31,       # aug
                      30,       # sep
                      31,       # oct
                      30,       # nov
                      31]       # dec
days_in_each_month_leap_year = copy.copy(days_in_each_month)
days_in_each_month_leap_year[1] = 29
def is_leap_year(yr):
    if yr % 400 == 0:
        return True
    elif yr % 100 == 0:
        return False
    elif yr % 4 == 0:
        return True
    else:
        return False

current_year = 1900    
current_weekday = 1             # days are 0,1,2,3,4,5,6
if is_leap_year(current_year) is True:
    current_weekday += days_in_a_leap_year
else:
    current_weekday += days_in_a_year
current_weekday %= 7
current_year += 1

n_sundays = 0
for yr in range(1901,2001):
    current_year = yr
    for month in range(12):
        if current_weekday == 0:
            n_sundays += 1
        if is_leap_year(yr) is True:
            current_weekday += days_in_each_month_leap_year[month]
        else:
            current_weekday += days_in_each_month[month]
        current_weekday %= 7

print(n_sundays)

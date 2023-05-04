"""
1 Jan 1900 was a Monday. Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.A leap year occurs on any year evenly divisible by 4, 
but not on a century unless it is divisible by 400.

-> How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

"""
# Solution 1: using the whole "poem."
"""
import datetime
import time
start_time = time.time()


def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        # cheking if it's a leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31


day_of_week = 1  # Tuesday, 1 January 1901
number_of_sundays = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if day_of_week == 6:  # Sunday
            number_of_sundays += 1
        days = days_in_month(month, year)
        day_of_week = (day_of_week + days) % 7

end_time = time.time()

elapsed_time_one = end_time - start_time

print(
    f'The total number of such Sundays turns out to be... (drumroll please)... {number_of_sundays}!')
print(f'Solution 1 took {elapsed_time_one:.10f} seconds to run.')


"""
#Solution 2: clean solution using datetime:
- https://docs.python.org/3/library/datetime.html
- https://www.youtube.com/watch?v=eirjjyP2qcQ&ab_channel=CoreySchafer
"""

start_time = time.time()

number_of_sundays = 0

# loop through each month
for year in range(1901, 2001):
    for month in range(1, 13):
        # date object for the first day of the month
        date_obj = datetime.date(year, month, 1)
        # check if Sunday falls in the first day of the month
        if date_obj.weekday() == 6:
            number_of_sundays += 1

end_time = time.time()

elapsed_time_two = end_time - start_time

print(
    f'The total number of such Sundays turns out to be... (drumroll please)... {number_of_sundays}!')
print(f'Solution 2 took {elapsed_time_two:.10f} seconds to run.')


if elapsed_time_one > elapsed_time_two:
    winner = "Solution 2"
else:
    winner = "Solution 1"

print(f'The fastest code is... {winner}')

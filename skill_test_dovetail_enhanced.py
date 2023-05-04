"""
Alternative code providing the number of Tuesdays (or any other day of the week) fell on the 
first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)
"""

"""
# Solution 1: using the whole "poem."
"""


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


target_day_name = ""
days_of_week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

while True:
    target_day_name = input("type a day of the week:").capitalize()
    if target_day_name in days_of_week:
        target_day = days_of_week.index(target_day_name)
        break
    else:
        print("Well, this day name is a bit of a fish out of water... in English at least! It's like trying to use a typewriter to fight climate change. Let's stick to the days we know and use technology to save the planet, shall we?")

day_of_week = 1  # Tuesday, 1 January 1901
number_of_chosen_day = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if day_of_week == target_day:  # Target day
            number_of_chosen_day += 1
        days = days_in_month(month, year)
        day_of_week = (day_of_week + days) % 7

print(
    f'The total number of such {target_day_name}s turns out to be... (drumroll please)... {number_of_chosen_day}!')

#Project Euler Problem  19
#https://projecteuler.net/problem=19

days_per_month = { #dictionary containing how many days are in each month
    1:31,
    2:28.25, #every 4 years, the number of days in February is 29. (for the sake of the scope of this problem)
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
    }

sundays = 0
years = 0
day = 2 #initial day of 20th century
year = 0 #call 1901 year 0, and run until 2000.

while year < 100:
    for month in range(1,13):
        day += days_per_month[month] #add the number of days in the given month
        if int(day % 7) == 0: #evaluates to True if it is a Sunday
            sundays += 1
    year += 1
print(sundays)

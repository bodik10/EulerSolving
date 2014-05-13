import datetime

sundays = 0

for year in range(1901, 2001):
    for month in range(1,13):
        d = datetime.date(year, month, 1)
        if d.isoweekday() == 7:
            sundays += 1
            print(d.isoformat())

print("%d Sundays fell on the first of the month during the twentieth century" % sundays)

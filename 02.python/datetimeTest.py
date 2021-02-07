import datetime
now = datetime.datetime.now()

print(now)
print(now.day)
print(now.month)
print(now.year)
print(now.tzinfo)
print(datetime.MINYEAR)

test = datetime.date(2020, 2, 14)

print(test.year)

test2 = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
print(test2.minute)

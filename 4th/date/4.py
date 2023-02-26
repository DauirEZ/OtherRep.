import datetime
n = int(input())

date1 = datetime.datetime.now()
date2 = datetime.datetime.now() - datetime.timedelta(days = n)
delta = abs(date2 - date1)
print(delta)
print(delta.total_seconds())
import datetime

dt = datetime.datetime.now()
dt1 = dt.replace(microsecond=0)

print("Original time:", dt)
print("Datetime without micrseconds:", dt1)
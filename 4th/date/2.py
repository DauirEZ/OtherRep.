import datetime 

cd = datetime.date.today()
s = datetime.timedelta(days=1)
y = cd - s
t = cd + s
print("Current Date:", cd)
print("Yesterday: ", y)
print("Tomorrow: ", t)
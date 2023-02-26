import datetime

cd = datetime.date.today()
d = datetime.timedelta(days=5)
nd = cd - d

print("Current Date:", cd)
print("New Date:", nd)
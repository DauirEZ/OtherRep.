import re
text = input()

ok = re.sub("[., ]", ";", text)

print(ok)
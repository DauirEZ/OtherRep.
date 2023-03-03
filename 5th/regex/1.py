import re

text = input()
ok = "ab*"
m = re.findall(ok, text)
print(m)
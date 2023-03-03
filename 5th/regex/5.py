import re
text = input()

ok = re.findall(r"a.+b$", text)

print(ok)
import re
text = input()

ok = re.findall(r"[A-Z][a-z]+", text)

print(ok)
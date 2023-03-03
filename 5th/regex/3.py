import re
text = input()

ok = re.findall(r"[a-z]+\_", text)
print(ok)
import re
text = input()

ok = re.findall("[A-Z][a-z]*", text)
print(" ".join(ok))
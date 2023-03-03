import re
text = input()

ok = re.findall("ab{2,3}", text)

print(ok)


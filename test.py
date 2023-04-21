import re
pattern1 = r"[0-9]*"
pattern2 = r"([a-z]*) or ([A-Z]*"

# print(re.search(pattern1, "efknwefn23kjnn"))

if re.search(pattern1, "efknwefnkjnn"):
    print(1)
else:
    print(0)
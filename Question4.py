import re

numbers = []
total = 0

with open("regex_sum_259427.txt") as file:
    for txt in file:
        numbers += re.findall(r"[0-9]+", txt)
for num in numbers:
    total+=int(num)
print("Sum =", total)

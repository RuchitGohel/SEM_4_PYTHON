# program - 23
# date - 11-02-2025

text="Hello There this is Python. ? Python is good"

sep_text = " "

for i in sep_text:
    if i.isalnum() or i.isspace():
        sep_text = sep_text + i
    else:
        sep_text = sep_text + " "

words = sep_text.split()

counts = {}

for i in words:
    if i in counts:
        counts[i] = counts[i] + 1
    else:
        counts[i] = 1

sort_count = sorted(counts.keys(), key = str.lower)
for i in sort_count:
    print(f"{i} : { counts[i] }")

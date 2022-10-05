l = [10, 20, 30]

idx = 0
for v in l:
    print(idx, v)      # made in enumerate
    idx += 1

for v in enumerate(l):
    print(v)                     # ready made function enumerate

for idx, value in enumerate(l, start=1):
    print(idx, value)                             # assigning values for enumerate
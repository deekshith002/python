#accept a string and display how many unique digits are present

st = input("Enter a string :")
count = 0
seen = ""
for c in st:
    if c.isdigit():                                          # if c.isdigit() and c not in seen:
        if c not in seen:        # If not already seen
           count += 1
           seen = seen + c    # Concatenate to string as it is counted

print(count)
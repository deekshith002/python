#accept two strings of same length and display where the characters dont match in strings

a = input('enter the sentences:')
b = input('enter the sentence:')
for i in range(0, len(a)):
    if a[i] != b[i]:
        print(f"mismatch at {i}  that is {a[i]} {b[i]}")
else:
        print(f"perfectly matched")
#accept a string and check whether it starts with 'a' and ends '0'(zero)

s = input("enter a sentence:")

if s[0] == 'a' and s[-1] == '0':
    print(f"valid")
else:
    print(f"invalid")
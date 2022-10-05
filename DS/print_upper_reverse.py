# accept a string and display all upper case letters present in the string in reverse order
st = input("enter the string:")
for c in st[::-1]:
    if c.isupper():
        print(c)

#largest of 3
a = input("enter the number:")
b = input("enter the number:")
c = input("enter the number:")
a = int(a)
b = int(b)
c = int(c)

if a>b and a>c:
    print(f" largest = {a}")
elif b>c:
    print(f"largest = {b}")
else:
    print(f"largest = {c} ")
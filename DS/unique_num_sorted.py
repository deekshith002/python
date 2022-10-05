# accept numbers until user gives zero and display unique numbers in sorted order
s = set()
while True:
    n = int(input("enter the number[0 to stop]:"))
    if n == 0:
        break
    s.add(n)
for i in sorted(s):
    print(i)
# largest of 10 numbers
g = 0
for i in range(1, 11): #range(10)
    n = int(input("enter the number:"))
    if n > g:
        g = n
print(f" greatest number is {g}")

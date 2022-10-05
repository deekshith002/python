# create a function that takes a number and prints a table for that
def table(num: int):
    for i in range(1, 11):
        print(f"{num:5d} * {i:5d}  = {num * i:5d}")


n = int(input("enter the number:"))
table(num=n)

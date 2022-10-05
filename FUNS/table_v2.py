
def table(num: int, len=10):
    print(end='\n\n')
    for i in range(1, len+1):
        print(f"{num:5d} * {i:5d}  = {num * i:5d}")


n = int(input("enter the number:"))
l = int(input("enter the length:"))
table(num=n, len=l)
table(num=n)

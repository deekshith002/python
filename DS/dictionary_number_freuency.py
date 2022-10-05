# accept numbers from user and until zero is given and create a dictionary that stores how many times each number is given
dt = {}
ls = []
while True:
    n = int(input("enter the number:"))
    if n == 0:
        break
    ls.append(n)
for i in ls:
    if i not in dt:
        id, value = i, ls.count(i)
        dt[id] = value
for c, d in dt.items():
    print(f"{c} occurs {d} time")

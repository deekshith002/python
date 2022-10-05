# accept numbers from users until 0 is given and display all number in reverse order
ls = []
while True:
    n = int(input("enter the number:"))
    if n == 0:
        break
    ls.append(n)
for c in ls[::-1]:                            # for c in ls[::]:
   print(c)                                   # print(ls.pop())
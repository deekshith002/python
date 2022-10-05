# common_factors

a = int(input('enter the number:'))
b = int(input('enter the number:'))
i = 2
smallest = a if a < b else b
for i in range(2, smallest // 2 + 1):
    if a % i == 0 and b % i == 0:
        print(i)

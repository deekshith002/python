#prime_number_v1
num = int(input("Enter number : "))
prime = True
for n in range(2, num // 2 + 1):
    if num % n == 0:
        prime = False
        break   #terminates the loops when it finds a factor

if prime:
    print("Prime number")
else:
    print("Not a prime")
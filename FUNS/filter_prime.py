# use filter to select prime numbers from a list of number
def prime(num):
    for c in ls:
        for i in range(2, c//2+1):
            if num % i == 0:
                return False
            else:
                return True


ls = [1, 50, 46, 84, 13, 7, 11]
for n in filter(prime, ls):
    print(n)

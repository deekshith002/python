# create a fucntion that takes  a number and returns true if it is prime else it returns false
def prime(num: int):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
        else:
            return True


print(prime(5))
print(prime(20))
print(prime(13))

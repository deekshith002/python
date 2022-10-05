#sum of the digits of the number

n = int(input("enter the number:"))
r=0
sum=0
while n>0:
    r = n % 10
    sum += r
    n //= 10
print(sum)
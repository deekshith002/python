# display the avg of even numbers

total = 0
count = 0
while True:
    n = int(input("enter the number[ to stop]:") )
    if n == 0:
        break
    else:
        if n % 2 == 0:
            total += n
            count +=1
print(f"sum of even numbers = {total/count}")

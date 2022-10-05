#create a function that takes a number and returns true if it is even otherwise false
def even(num: int):
    if num % 2 == 0:
        return True
    else:
        return False


print(even(num=20))
print(even(num=15))
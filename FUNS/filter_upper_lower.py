# create a function that takes a string and returns a tuple that contains the number of upper and lowercase.

def alpha(st1: str):
    upper = 0
    lower = 0
    for i in st1:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return lower, upper


print(alpha("How Do You Do"))

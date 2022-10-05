# create a function that takes multiple strings using varying arguments and then return the string with largest length
def largest(*st: str):
    big = ''
    for i in st:
        if len(big) < len(i):
            big = i
    return big


print(largest("fhefhbehf", "fhbfhbeferf", "edfdd", "riuweifbwfbvfegfef"))

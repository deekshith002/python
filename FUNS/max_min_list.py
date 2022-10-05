# create a function that takes a list and returns the largest and smallest value
def num(ls: list):
    return max(ls), min(ls)


print(num([1, 2, 3, 88, 5, 66666, 2, 1, 0]))

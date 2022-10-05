# create a function that takes a set of strings and prints all common char
def common(*st: str):
    chars = set(st[0])
    for i in st:
        chars &= set(i)  # chars = chars | set(i)
    chars = "".join(sorted(chars))
    print(chars)


print(common("Pavo2.10", "Python2.10", "Python2.10"))

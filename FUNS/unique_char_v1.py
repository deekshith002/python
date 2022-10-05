# create a function that takes a set of strings and prints all unique char
def common(*st: str):
    chars = set()
    for i in st:
        chars |= set(i)  # chars = chars | set(i)
    chars = "".join(sorted(chars))
    print(chars)


print(common("Python", "java", "javaSE"))
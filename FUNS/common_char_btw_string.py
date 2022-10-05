# create a function that takes two strings and displays the common characters between the string in the
# order they appear in 1st string
def compare(st1: str, st2: str):
    pos = -1
    for i in st2:
        pos = st1.find(i, pos + 1)
        if pos == -1:
            break
        print(f"{st1[pos]}", end=' ')


s1 = "how do you do"
s2 = "you do"
compare(s1, s2)

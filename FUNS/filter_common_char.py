# create a function that takes two strings and returns the position where strings dont match and return -1 if both of them match
def common(s, t):
    smallest = len(s) if len(s) < len(t) else len(t)
    for i in range(0, smallest):
        if s[i] != t[i]:
            print(i)


common(s="how are you", t="how do you do")

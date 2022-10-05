# use map to extract all special character from given string
def is_special(c):
    seen = ''
    for s in c:
        if not s.isalnum() and not s.isspace(): #if not (c.isalnum() or c.isspace()):
            seen += s
    return seen

values = ["ABC,23", "AB7-87,8", "383A;BC3;3 3"]
for i in map(is_special, values):
    print(i)
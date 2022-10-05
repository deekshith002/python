# create a function that takes a string and display characters vertically in reverse order
def revchar(st: str):
    for i in st[::-1]:
        print(i)


revchar("how do you do")

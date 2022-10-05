#to count the words in a string

st = input("enter the string:")
a = 1
for i in st:
    if i.count(" "):
        a +=1

print(a)
# create a list with ASCII codes for all uppercase letters in a string
st = 'HOW do You Do'
l = []
for i in st:
    if i.isupper():
        print(f" {i},{ord(i)}") #ord is used for ascii code

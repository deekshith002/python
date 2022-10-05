#To count the number of digits in a string
st = input("enter a sentence:")
count = 0
for i in st:
    if i.isdigit():
        count +=1
print(count)
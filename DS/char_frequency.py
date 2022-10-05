# Accept a string and display unique characters.
st = 'how do you do'
l = list(st)
seen = ''
for i in l:
    if i not in seen:
        print(f"{i} occured {l.count(i)} times \n")
        seen += i
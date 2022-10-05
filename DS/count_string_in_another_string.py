# accept two strings and display the postions where substring is found in main string

st1 = 'how are you boi you'
ss = 'ou'
pos = -1
while True:
    pos = st1.find(ss, pos+1)
    if pos == -1:     # -1 indicates not found(or false)
        break
    print(pos)
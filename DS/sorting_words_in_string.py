# create a program to take a string and display words in the string in sorted order
st = "I hope you are having fun with Python"
l = st.split()
for w in sorted(l):
    print(w)    # print(''.join(sorted(i))) to sort each word internally
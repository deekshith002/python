# take a string {70,80,50,30} and display total in them

st = '70, 80, 50, 30'
st = st.split(",")
total = 0
for i in st:   # for i in st.split[',']
    total += int(i)   # as i is a string so it is being converted to int
print(total)
# accept a string and store each character and how many times it occurs in a dictionary

st = 'covid third wave is about to dip'
dt = {}
for i in st:
    id, value = st.count(i), i
    dt[id] = i
print(dt)

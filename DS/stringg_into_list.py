# accept a string names separated by column and display each name along with their length
st = 'my:self:deekshith:katari'
st = st.split(':')
for a in st[::]:
    print(f"{a} and {len(a)}")
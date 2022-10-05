# accept 10 numbers from user then display all even numbers 1st and odd numbers next.
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = []
for c in ls:
    if c % 2 == 0:
        st.append(c)
for c in ls:
    if c % 2 != 0:
        st.append(c)
ls = st.copy()
print(ls)
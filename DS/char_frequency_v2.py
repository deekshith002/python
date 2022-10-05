# Accept a string and display unique characters.
st = "how do you do"
for c in set(st):
   print(f"{c} occurs {st.count(c)} times")
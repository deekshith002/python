# if their are combination of numbers and characters in a string extract numbers and display their total
st = '10,20,,30,abc,100,,,ihsdf'
sum = 0
for i in st.split(','):
    if i.isdigit():
        sum += int(i)
print(sum)
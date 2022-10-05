# print names and phone numbers
names = ['ram', 'hem', 'jack', 'roa', 'raja']
phone = [1455, 7889, 112]
while len(names) > len(phone):
    phone.append('unknown')
for i, j in zip(names, phone):
    print(f" {i}  {j}")
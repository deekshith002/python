def sign(n):
    return 1 if n >= 0 else 2


nums = [10, 11, 30, 45, -10, -30]

for n in sorted(nums, key=abs):  # this returns the negative value as positive but it prints it as the same -ve value
    print(n)
def prepend(ls,value):
    l.insert(0,value)

# for n in sorted(nums, key=sign):
#     print(n)

for n in sorted(nums, key=lambda v: 1 if v >= 0 else 2): #can even  use lamda rather then sign fucntion
    print(n)

l = [1,2]
prepend(l,10)
print(l)

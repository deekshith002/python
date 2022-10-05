#inches to millimeter and centimeter
data = input("enter the length(in inches) :")
length = int(data)
mm = length*25.4
cm = length*2.54
print(f"length = {mm:10.2f}mm")
print(f'length = {cm:10.2f}cm')
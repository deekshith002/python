# net_price_v3

data = input("enter the price:")
price = int(data)
if price>5000:
    discount = price*0.2
else:
    discount = price*0.1
net_price = price - discount
print(f" price =    {price:8.2f}")
print(f"discount = -{discount:8.2f}")
print(f"net price = {net_price:8.2f}")
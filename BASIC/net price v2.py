#net_price_v2
data = input("enter the price :")
price = int(data)
discount = price*0.1
net_price= price - discount
print(f" price=      {price:10.2f}")
print(f"-discount=   {discount:10.2f}")
print(f" net price=  {net_price:10.2f}")
#netprice

price = input("enter the price:")
price = int(price)  #coversion of string into a integer data type so that it can be used for numeric calculations
                    # in line 6 and 7 string cant be used for numeric calculations so thats the reason it is converted
discount = price * 0.1
net_price = price - discount
print("net price = ",net_price)
# create a class that stores details regarding a product . the details are product id,product name,price and discount rate
class product:
    disrates = {'iphone11': 15, 'macbook': 15, 'FZ-5': 30}

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_details(self):
        print(f"product id     :   {self.id}")
        print(f"name           :   {self.name}")
        print(f"price          :   {self.price}")

    def get_net_price(self):
        baseprice = self.price
        discount = baseprice * product.disrates[self.name] / 100
        return baseprice - discount

    def discount(self):
        return product.disrates[self.name]


p1 = product(544, 'macbook', 50000)
p1.print_details()
print(f"disount        :   {p1.discount()}% \nnet price:{p1.get_net_price()}")

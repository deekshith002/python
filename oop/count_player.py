class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


players = [Player("A", 20), Player("C", 30), Player("B", 28), Player("DHONI", 56)]
count = 0
for p in players:
    count += 1
print(count)

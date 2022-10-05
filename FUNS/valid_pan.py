# use filter to select a valid pan
def pan(s):
        return len(s) == 10 and s[0:5].isalpha() and s[5:9].isdigit() and s[-1].isalpha()


user = ["SDJKA5464A", "JHADS6513Q", "GAVCJH5455", "ADKHBSDHBSD1541165"]
for s in filter(pan, user):
    print(s)

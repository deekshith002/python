class A:
    def process(self):
        print("Process in A")


class B(A):
    pass


class C:
    def process(self):
        print("Process in C")


class D(B, C): #B Is mentioned 1st so it is given preference if process is found in b or super class of b it is printed
               # else c is printed
    pass


obj = D()
obj.process()

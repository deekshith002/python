# print both pos and kw args
def details(*arg, **kwargs):
    print(arg)
    for i in kwargs.items():
        print(i)


details(a=10, b=20)
details(name='abc', age=20)
details(10, 20, a=10)

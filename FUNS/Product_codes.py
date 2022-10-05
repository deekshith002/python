# extract product code
def code(st):
    return st[:-5:-1] if st[:-5:-1].isdigit() else -1


ls = ['as2632', 'gd5562', 'ua5496', 'sd8522']
for i in map(code, ls):
    print(i)

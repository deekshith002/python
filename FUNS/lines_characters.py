def line(ch='-', len=30):
    print('\n')
    for i in range(0, len):
        print(f"{ch}", end='')


line(ch='*', len=20)
line(ch='*')
line(len=100)
line()
import marshal

x1 = 30
x2 = 5.0
x3 = [1, 2, 3]
x4 = (4, 5, 6)
x5 = {'a':1, 'b':2, 'c':3}
x6 = {8, 10, 9}

x = [eval('x'+str(i)) for i in range(1, 7)]

x

with open('test.dat', 'wb') as fp:
    marshal.dump(len(x), fp)
    for item in x:
        marshal.dump(item, fp)

with open('test.dat', 'rb') as fp:
    n = marshal.load(fp)
    for i in range(n):
        print(marshal.load(fp))
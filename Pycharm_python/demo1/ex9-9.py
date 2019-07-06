import shelve

zhangsan = {'age':38,'sex':'Male','address':'SDIBT'}
lisi = {'age':40,'sex':'Male','qq':'1234567','tel':'7654321'}

with shelve.open('shelve_test.dat') as fp:
    fp['zhangsan'] = zhangsan
    fp['lisi'] = lisi
    for i in range(5):
        fp[str(i)] = str(i)

with shelve.open('shelve_test.dat') as fp:
    print(fp['zhangsan'])
    print(fp['zhangsan']['age'])
    print(fp['lisi']['qq'])
    print(fp['3'])
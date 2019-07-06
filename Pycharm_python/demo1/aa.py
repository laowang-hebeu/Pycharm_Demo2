class Person2(object):
    # def __init__(self):
    #     print('create Person')
    pass
class Person1(object):
#    name='lili'
#    age=0
    __num=0
    def __init__(self,name='',age=20,sex='male'):
        self.name=name
        self.age=age
        self.__sex=sex
        print('create Person')
        print(self)
    pass
def f():

    for i in range(5):
        print(i)

class SingleInstance(object):
    num=5
    def __init__(self,zead=0):
        self.__zead=zead
        if self.__zead>0:
            raise Exception('只能创建一个对象')
        self.num=+1
        print(self.num)


t1=SingleInstance()
t2=SingleInstance()
#f();
class Root:
    __total = 11
    def __init__(self,v):
        self.__value = v
        Root.__total += 1

    def show(self):
        print('self.__value:',self.__value)
        print('Root.__total:',Root.__total)

    @classmethod
    def classShowTotal(cls):
        print(cls.__total)

    @staticmethod
    def staticShowTotal():
        print(Root.__total)

r=Root(3)
r.classShowTotal()
r.staticShowTotal()

rr=Root(5)
Root.staticShowTotal()
Root.classShowTotal()

Root.show(r)
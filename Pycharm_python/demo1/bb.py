class Test:
    def __init__(self,value):
        self.__value = value

    def __get(self):
        return self.__value
    def __set(self,v):
        self.__value = v


    value = property(__get,__set)

    # @property
    # def avalue1(self):
    #     return self.__value
    def show(self):
        print(self.__value)


t=Test(3)

print(t.value)
t.value=5
print(t.value)
t.show()


#t.avalue1=5
#del t.value1



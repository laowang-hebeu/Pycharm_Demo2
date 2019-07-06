from sys import argv

class Demo:
    def __init__(self,value):
        self.__value = value

    def __add__(self, other):
        return self.__value + other

d = Demo(5)

print(d + 3)

script,first,second,third = argv

print('the script is called:',script)
print('the first parameter is called:',first)
print('the second parameter is called:',second)
print('the third parameter is called:',third)
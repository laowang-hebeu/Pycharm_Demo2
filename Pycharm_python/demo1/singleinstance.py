#author:Lao Wang ：2019/5/3
#coding=utf-8
from time import sleep

class SingleInstance():
    num=0
    def __init__(self):
        if SingleInstance.num>0:
            raise Exception('只能创建一个对象')
        SingleInstance.num += 1


t1 = SingleInstance()
#t2=SingleInstance()



s = '中国山东烟台ABCDE'
print(len(s))

ss = 'Python是个好语言'
print(type(ss))
print(type(ss.encode('gbk')))
print(type(ss))
print(ss.encode())
print(type(ss.encode()))
print(ss.encode().decode())
print(type(ss.encode().decode()))




# for i in range(10):
#     print(i,end='\n')
#     sleep(1)

path1 = R"C:\vwindows\notepad.ex"
print(path1)
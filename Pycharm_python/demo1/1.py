#define a class
#instance an object

from aa import Person2
from aa import Person1
#import aa.py
from datetime import datetime

if __name__ == '__main__':
    Lily = Person2()
    print(type(Person2))
    print(type(Lily))

    Lilei=Person1('laowang',21)
    print(type(Person1))
    print(type(Lilei))
    print(Lilei.name,Lilei.age)
    #print(Person1.name)
    print(Person1.__num)
    #为啥不报错
    #print(Lilei.__sex)


#print(datetime.now())

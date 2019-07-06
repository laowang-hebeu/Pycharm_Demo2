class Vector3:
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z

    def add(self,anotherPoint):
        x = self.__x + anotherPoint.__x
        y = self.__y + anotherPoint.__y
        z = self.__z + anotherPoint.__z

        return Vector3(x,y,z)

    def sub(self,another):
        x = self.__x - another.__x
        y = self.__y - another.__y
        z = self.__z - another.__z

        return Vector3(x, y, z)

    def mul(self,n):
        x,y,z = self.__x*n,self.__y*n,self.__z*n
        return Vector3(x, y, z)

    def div(self,n):
        x, y, z = self.__x / n, self.__y / n, self.__z / n
        return Vector3(x, y, z)

    def show(self):
        print('X:{0},Y:{1},Z:{2}'.format(self.__x,self.__y,self.__z))

    @property
    def length(self):
        return(self.__x**2+self.__y**2+self.__z**2)**0.5

v = Vector3(3,4,5)
v1 = v.mul(3)

v.show()
v1.show()

v2 = v1.add(v)
v2.show()

print(v2.length)









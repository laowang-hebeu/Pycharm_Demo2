class Person(object):
    def __init__(self,name='',age=20,sex='male'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self,name):
        if not isinstance(name,str):
            raise Exception('name must be string')
        self.__name = name

    def setAge(self,age):
        if type(age) != int:
            raise Exception('age must be integer')
        self.__age = age

    def setSex(self,sex):
        if sex not in ('male','female'):
            raise Exception("sex must be 'male' or 'female'")
        self.__sex = sex

    def show(self):
        print(self.__name,self.__age,self.__sex,sep='\n')


class Teacher(Person):
    def __init__(self,name='',age=30,sex='male',department='Computer'):
        super(Teacher, self).__init__(name,age,sex)
        #Person.__init__(self,name,age,sex)
        self.setDepartment(department)

    def setDepartment(self,department):
        if type(department) != str:
            raise Exception('department must be a string.')
        self.__department = department

    def show(self):
        super(Teacher,self).show()
        print(self.__department)


if __name__ == '__main__':
    zhangsan = Person('Zhang San',19,'male')
    zhangsan.show()
    print('=' * 90)

    lisi = Teacher('Li Si',32,'male','Math')
    lisi.show()

    lisi.setAge(40)
    lisi.show()


# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/4 13:29"

# 《byte of python》 中的 Inheritance类的继承 和多态
# 此处有疑问
# 新类和旧类  多态在新类中的实现
# 基类、超类，子类、派生类
# 继承时，在类名后跟一个包含基类名的元组？？？
# 注意，这里我们定义了子类的 __init__方法
# 因此必须要初始化对象的基类部分，即显示的调用 基类的构造函数
# 这里有新类和旧类的区别
# 如果我们没有定义子类的__init__方法，python会自动调用基类的
# __init__方法，不用再显示声明
# 还要注意一点，多重继承！


class SchoolMember:
    '''代表任何学校里的成员的共有属性'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我所有的细节'''
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    '''一位老师'''
    def __init__(self,name,age,salary):
        super(Teacher, self).__init__(name,age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        super(Teacher, self).tell()
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''一位学生'''
    def __init__(self,name,age,marks):
        super(Student, self).__init__(name,age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        super().tell()
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya',40,30000)
s = Student('Swaroop',25,75)

print()

members = [t,s]
for member in members:
    member.tell()



# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/4 12:39"

# 《byte of python》
# 类与对象的数据部分，即字段filed，亦即类变量或实例变量
# 类变量是共享的，且只有一份
# 实例变量仅属于实例所有
# python是动态语言，可以自由的条件变量或方法
# 当 类变量和 实例变量同名时，类变量被隐藏

# 记住，只能使用 self 来引用同一对象的变量与方法，被称为 属性引用。
# 所有的类成员都是公开的。有一个例外：用双下划线作为前缀，没有后缀，
# python 会用名称调整 来使其成为一个私有变量（实际上只是名称改了一下，
# 还是公开的）

class Robot:
    '''表示一个带有名字的机器人'''
    # 一个用来计数机器人数量的变量
    population = 0

    def __init__(self,name):  # name是一个实例变量，因此，由 self 分配
        self.name = name
        print('(Initializing {})'.format(self.name))
        # 机器人被创建时，计数加1
        Robot.population +=1    # 此变量属于类，因此是类变量，引用时需写 类.变量
        # 这里还可以用 self.__class__.population
        # 因为每个对象可以通过 self.__class__引用它的类
        # 所以，这里 self.__class__ 等同于 Robot

    def die(self):
        '''我挂了'''
        print('{} is being destroyed!.'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working.'.format(Robot.population))

    def say_hi(self):
        '''来自机器人的诚挚问候

        没问题，你做得到！'''
        print('Greetings, my masters call me {}.'.format(self.name))

    # 这里是一个属于 类的方法，不属于实例
    # 装饰器Decorator 将how_many标记为类方法
    # 将装饰器想象为调用一个包装器(Wrapper)函数的快捷方式
    # 所以，以下一句等同于 how_many = classmethod(how_many)
    @classmethod
    def how_many(cls):
        '''打印出当前机器人数量'''
        print('We have {:d} robots.'.format(cls.population))
        # 这里用 Robot. 也可以

r1 = Robot('R1-D1')
r1.say_hi()
Robot.how_many()

r2 = Robot('R2-D2')
r2.say_hi()
Robot.how_many()

print('\nRobots can do some work here.\n')

print("Robots have finished their work. So let's destory them.")
r1.die()
r2.die()

Robot.how_many()

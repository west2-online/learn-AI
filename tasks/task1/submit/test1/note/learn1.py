# class Money:
#     age=11
#     num=666
#     pass
# one=Money()
# Money.count=1
# print(Money.count)
# print(Money.__dict__)
# Money.age=22
# print(Money.age)
# del Money.age
# one.__dict__={"sex":1}
# print(one.__dict__)
# print(one.count)
# class Person:
#     ag=18
#     num=6
#     # __slots__={"age"}
# one=Person()
# two=Person()
# one.age=1
# one.num=2
# # one.age+=2
# print(one.age)
# print(one.num)
# two.age+=1
# print(two.age)
#方法（实例，类，静态）
# class Person:
#     @classmethod
#     def leifangdfa(cls):
#         print("类方法")
#     @staticmethod
#     def jingtai():
#         print("静态方法")
#     def eat(self,food):
#
#         print("实例方法")
#         print(self,food)
# p=Person()
#
# print(p.eat("土豆"),Person.jingtai(),Person.leifangdfa())
# print(Person.eat('abc',"在吃饭"))
#类方法
# class Person:
#     age=10
#     def shili(self):
#         print(self.age,self.num)
#     @classmethod
#     def leifangfa(cls):
#         print("类方法",cls.age,cls.num)
#     @staticmethod
#     def jingtai():
#         print(Person.age)
#
# one=Person()
# one.num=1
# one.age=5
# # print(one.leifangfa(666))
# one.shili()
# # one.leifangfa()
# one.jingtai()
#元类(type)
# class A:
#     pass
# print(A.__class__)
# def run(self):
#     print("函数")
# Dog=type('Dog',(),{'count':0,"run":run})
# print(Dog.__dict__)
# d=Dog()
# d.run()
# class Dog(object):
#     """This is a dog class as example"""
#
#     animal_kind = 'dog'  # 基本属性
#     animal_legs = 4  # 基本属性也建议写到初始化构造函数中去
#
#     def __init__(self, name, age, params):
#         ''' This is initial funciton'''
#         self.name = name
#         self.age = age
#     # 还可以定义各种其他的属性，作为实例初始化时候将传进来的参数进行赋值
#         self.__gender = 'male'  # 两个下划线开头是私有内部属性，只能在类内访问
#
#     def __privateGender(self):
#         """This is pravate method"""
#         print('This dog gender is %s', self.__gender)
#
#
#     def voice(self):
#         """Dog will speak as wangwang """
#         print('WangWangWang')
#         print(self.__privateGender(self))
#
#
#     def run(self):
#         """runing with legs"""
#         print("This dog has %d legs to run" % self.animal_legs)
#
# # 定义一大堆各种各样的方法
class Dog(object):
    """
    This is a class for Dog

    Dog class is the parents class of all dog, this class contain
    general attributes of dog and some common function of dogs, such as
    num legs, the voice fucntion, the runing functions.

    Attributes:
        name: 	A string of dog's name
        kind: 	A string of dog's family
        age:  	A integer of dog years
        gender: A boolean gender of dog, male=1 of famle=0
        legs    A integer if dog's legs
        weight: A float of dogs weight
        size:   A string of dogs, one of big, middle, smal
    """

    def __init__(self, args, gender, size):
        """initialize dog class, all attributes pass in with args, which is a dict or indepent params

        Input contain dict and str params, also there is private attribute

        Args:
            args.name(str): dog name
            args.kind(str): dog family
            args.age(int) : dog age
            gender(bool)  : dog gender, male=1,famale=0
        args.weight(float): dog weight
            size(str)     : dog size
        """
        self.name = args.name
        self.kind = args.kind
        self.age = args.age
        self.weight = args.weight

        # __legs(int) : dog legs,privite attribute, not the inputs params,写在前面用#做注释，不属于输入的参数的初始化
        self.__legs = 4
        """写在后面用三引号__legs(int)   : dog legs,privite attribute"""

        self.size = size
        self.gender = gender

    def voice(self, size):
        """This is dog speak fucntion

        Different dog with different voice
        which related to the size,age and kind

        Args:
            size(str): dog size
            age(int) : dog age
            kind(srt): dog kind

        Returns:
            None, just print the voice
        """
        if size == 'big':
            print('Big WangWang')
        elif size == 'middle':
            print('M wang')
        elif size == 'small':
            print('Miao')

    # 附注：return 可从任意深度跳出函数，None


class Husky(Dog):
    """Husky inherent the Dog attris and method"""

    def __init__(self, name, age, color, params):
        Dog.__init__(self, name, age)  # 利用Dog这个父类的初始化
        self.color = color  # 子类中特定属性的初始化

    def jump(self):
        """Husky special jump function"""
        print('This dog could jump jump')

    def voice(self):
        """重写覆盖父类的函数，实现自己的特殊的方法"""
        print('AoAoAoWu~~~~~~')
help(Dog)

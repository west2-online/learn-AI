'''类属性'''
class Car:
    # 类属性
    wheels = 4

    def __init__(self, make, model):
        self.make = make  # 实例属性make
        self.model = model  # 实例属性model

        # 创建Car实例
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# 访问类属性
print(car1.wheels)  # 输出: 4
print(car2.wheels)  # 输出: 4

'''公有属性x'''
class Animal:
    x=10
    def test(self):
        print(Animal.x)
        print(self.x)
class Dog(Animal):
    def test2(self):
        print(Dog.x)
        print(Animal.x)
#测试代码
animal1=Animal()
animal1.test()#10 10
print(animal1.x)
dog1=Dog()
dog1.test2()#10 10
print(dog1.x)


'''受保护的属性'''

''' 属性访问器（Getter）和修改器（Setter）是用来访问和修改属性的特殊方法。使用它们可以在访问属性时进行额外的逻辑处理。'''
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 私有属性，约定使用下划线开头

    # 属性访问器（Getter）
    @property
    def radius(self):
        return self._radius

    # 属性修改器（Setter）
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("半径不能为负数")

# 创建Circle实例
circle = Circle(5)

# 使用属性访问器获取半径
print(circle.radius)  # 输出: 5

# 使用属性修改器设置半径
circle.radius = 10
print(circle.radius)  # 输出: 10

# 尝试设置负数半径，将会引发ValueError
circle.radius = -1
''' 在上述代码中，使用@property装饰器定义了一个名为radius的属性访问器，用于获取_radius的值。
同时，使用@radius.setter装饰器定义了属性修改器，用于设置_radius的值。
这样，我们可以像访问普通属性一样使用circle.radius来获取和设置_radius的值。  '''



#特殊的类属性
'''特殊的类属性：对于所有的类，都有一组特殊的属性

_ _ name_ _     # 类的名字（字符串）
_ _ doc _ _     # 类的文档字符串
_ _ bases _ _   # 类的所有父类组成的元组
_ _ dict _ _    # 类的属性组成的字典
_ _ module _ _  # 类所属的模块
_ _ class _ _   # 类对象的类型
'''
class object_example:
    def __init__(self) -> None:
        pass

class person(object_example):
    '''there is doc'''
    tall = 180
    hobbies = []
    def __init__(self, name, age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def infoma(self):
        print('%s is %s weights %s'%(self.name,self.age,self.weight))

print(person.__name__)      # person
print(person.__doc__)       # there is doc
print(person.__bases__)     # (<class '__main__.object_example'>,)
print(person.__dir__)       # <method '__dir__' of 'object' objects>
print(person.__module__)    # __main__
print(person.__class__)     # <class 'type'>
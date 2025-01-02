'''实例方法'''

class Dog:
    def __init__(self, name):
        self.name = name

        # 实例方法
    def bark(self):
        return "汪汪！我是" + self.name

        # 创建Dog实例
dog = Dog("小白")

# 调用实例方法
print(dog.bark())  # 输出: "汪汪！我是小白"


'''类方法是使用@classmethod装饰器定义的方法，在调用时，Python会将类本身传递给第一个参数（通常命名为cls），表示对类进行操作。'''
class MathUtils:
    PI = 3.1415926

    # 类方法
    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius * radius

# 调用类方法
area = MathUtils.circle_area(5)
print(area)  # 输出: 78.539815
'''在上述代码中，我们使用类方法circle_area计算圆的面积，注意我们在类方法中可以使用类的属性cls.PI'''

'''静态方法是使用@staticmethod装饰器定义的方法，它不需要特殊的参数（如self或cls）。静态方法与类和实例无关，通常用于执行与类相关的实用函数'''
class StringUtils:
    # 静态方法
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

# 调用静态方法
result = StringUtils.is_palindrome("level")
print(result)  # 输出: True



#特殊方法
'''特殊方法（魔术方法）
特殊方法，也被称为魔术方法，以双下划线__开头和结尾。它们是Python中用于实现类的特殊行为的方法。'''
#__str__方法
#__str__方法返回对象的字符串表示，可用于自定义对象在print函数中的输出。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 自定义__str__方法
    def __str__(self):
        return f"{self.name}，{self.age}岁"

        # 创建Person实例
person = Person("Alice", 30)

# 调用print函数输出对象
print(person)  # 输出: "Alice，30岁"


# __repr__方法返回对象的“官方”字符串表示，可用于在交互式环境中直接输出对象。
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # 自定义__repr__方法
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

        # 创建Point实例
point = Point(1, 2)

# 在交互式环境中输出对象
point  # 输出: Point(1, 2)


'''属性和方法的装饰器是Python中用于对属性和方法进行额外操作的特殊注解。
装饰器能够简化代码、提高代码的复用性，并使代码更加优雅。'''

#@property装饰器
'''@property装饰器用于将一个方法转换为只读属性，使得我们可以像访问属性一样访问这个方法，而无需使用括号。'''

'''在下述代码中，我们定义了一个Circle类，
其中area方法用于计算圆的面积，
@property装饰器将radius方法转换为只读属性。
使用@property装饰器后，我们可以像访问属性一样访问circle.radius获取圆的半径。'''

class Circle:
    def __init__(self, radius):
        self._radius = radius  # 私有属性，约定使用下划线开头

    # 属性访问器（Getter）
    @property
    def radius(self):
        return self._radius

    # 计算圆的面积
    def area(self):
        return 3.14159 * self._radius * self._radius

# 创建Circle实例
circle = Circle(5)

# 使用属性访问器获取半径
print(circle.radius)  # 输出: 5

# 使用方法计算圆的面积
print(circle.area())  # 输出: 78.53975

# 使用属性访问器获取面积（注意：这里不需要加括号）
print(circle.area)  # 输出: <bound method Circle.area of <__main__.Circle object at 0x...>>

#@classmethod装饰器
'''@classmethod装饰器用于定义类方法，类方法的第一个参数通常命名为cls，表示对类本身进行操作。'''

'''在下述代码中，我们定义了一个MathUtils类，
其中的circle_area方法是一个类方法，用于计算圆的面积。
在类方法内部，我们可以通过cls访问类的属性和方法。'''
class MathUtils:
    PI = 3.1415926

    # 类方法
    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius * radius

# 调用类方法
area = MathUtils.circle_area(5)
print(area)  # 输出: 78.539815

 #@staticmethod装饰器
'''@staticmethod装饰器用于定义静态方法，静态方法与类和实例无关，通常用于执行与类相关的实用函数。'''
class StringUtils:
    # 静态方法
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

# 调用静态方法
result = StringUtils.is_palindrome("level")
print(result)  # 输出: True

'''Python支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数。'''
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在调用原始函数之前/之后执行的代码
        result = self.func(*args, **kwargs)
        # 在调用原始函数之后执行的代码
        return result


@DecoratorClass
def my_function():
    pass
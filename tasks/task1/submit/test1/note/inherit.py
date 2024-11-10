#属性和方法的继承
'''在Python中，子类可以继承父类的属性和方法。子类可以在继承的基础上进行扩展和修改，或者覆盖父类的方法。'''
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "吱吱"  # 默认动物叫声

class Dog(Animal):
    def __init__(self, name):
        super().__init__("犬科")#调用父类的属性，并初始化为犬科
        self.name = name
    # 重写make_sound方法
    def make_sound(self):
        return "汪汪！我是" + self.name
# 创建Dog实例
dog = Dog("小白")
# 调用继承的方法
print(dog.species)   # 输出: "犬科"
# 调用子类的方法（覆盖了父类的方法）
print(dog.make_sound())  # 输出: "汪汪！我是小白"


# 父类
class Person:
    def __init__(mysillyobject, firstname, lastname):
        mysillyobject.name = firstname
        mysillyobject.family = lastname

    def myfunc(abc):
        print("Hello my name is " + abc.name)

# 子类，继承
class Student(Person):
    def __init__(self, fname, year, lname):#添加 __init__() 函数
        super().__init__(fname, lname)  # 调用父类的属性赋值方法，super() 函数，使子类自动从其父继承所有方法和属性
        self.graduationyear = year  # 子类自己的属性

    def welcome(self):
        # 子类自己的方法
        print("Welcome", self.name, self.family, "to the class of", self.graduationyear)

#创建student实例
x = Student("Elon", 2019, "Musk")
x.welcome()#输出: Welcome Elon Musk to the class of 2019


#扩展： 覆盖(or重写) /重载 (override/ reload)
'''如果在开发中，子类的方法中包含父类的方法，父类原本的方法是子类方法的一部分，就可以采用扩展的方式。

扩展的方式步骤：

 1.在子类中重写父类的方法
 2.在需要的位置使用 super().父类方法 来调用父类方法的执行
 3.代码其他的位置针对子类的需求，编写子类特有的代码实现

第2点.关于super：
 在python中super是一个特殊的类,super()就是使用super类创建出来的对象
 最常使用的场景就是，在重写父类方法时，让super().调用在父类中封装的方法'''
# 单继承， 子类对父类扩展：新增方法、重写方法、子类中使用super().调用父类方法
class Animal():
    def eat(self):
        print("吃")

    def run(self):
        print("跑")

    def drink(self):
        print("喝")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("会飞")

    def bark(self):
        # 1. 针对子类特有的需求，编写代码
        print("天籁之音")

        # 2. 使用super(). 调用原本在父类中封装的方法
        super().bark()

        # 3. 增加其他子类的代码
        print("OKOK")


# 创建一个哮天犬对象
xtq = XiaoTianQuan()

xtq.bark()
xtq.drink()
xtq.sleep()



'''覆盖（Override）：指在继承中，父类的有些方法在子类中不适用，子类重新定义。
注意：
若子类中被“覆盖”方法的参数类型不同，返回类型不一致，这不是覆盖，而是重载。覆盖要求参数类型必须一样，且返回类型必须兼容。总之，子类对象得保证能够执行父类的一切。
不能降低覆盖方法的存取权限，如public变成private。
若不希望父类的某个方法被子类覆盖，可以用final修饰该方法。甚至可以扩展到将类用final修饰，则其中所有的方法均不可覆盖，但不影响成员变量的赋值。

子类如何重写父类的方法?
前提:
规则一：重写方法不能比被重写方法限制有更严格的访问级别。
（但是可以更广泛，比如父类方法是保护访问权限，子类的重写方法是public访问权限。）

规则二：参数列表必须与被重写方法的相同。
(需要注意的是如果子类方法的参数和父类对应的方法不一样,那就不是重写,而是重载)

规则三：返回类型必须与被重写方法的返回类型相同。

规则四：重写方法不能抛出新的异常或者比被重写方法声明的检查异常更广的检查异常。但是可以抛出更少，更有限或者不抛出异常。

规则五：不能重写被标识为final的方法。

规则六：如果一个方法不能被继承，则不能重写它。比如父类的私有方法就不能被重写。

如果子类能够继承父类的某个方法, 那么子类就能够重写这个方法。
'''


# 如果子类中重写了父类方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
class XiaoTianQuan(Dog):

    def fly(self):
        print("会飞")

    def bark(self):
        print("OKOK")


class TuDog(Dog):
    def fly(self):
        pass

    def bark(self):
        print("小土狗")


# 创建对象1
xtq = XiaoTianQuan()
xtq.bark()
xtq.drink()
xtq.sleep()

# 创建对象2
tg = TuDog()
tg.bark()
tg.fly()


#多态
'''多态就是“具有多种形态”，它指的是：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量的调用方法，
在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法。
当子类和父类存在相同的方法的时候，子类的方法会覆盖父类的方法，这样代码在运行时总会调用子类的方法，这就是多态。
判断一个实例是不是某个对象，可以使用isinstance()函数，是则输出True，反之输出False。
'''
print('---------------------多态------------------------')
class Animal:
    def say(self):
        print('Animal')
class Dog(Animal):
    def say(self):
        print('Dog')
class Cat(Animal):
    def say(self):
        print('Cat')
animal = Animal()
animal.say()
dog = Dog()
dog.say()
cat = Cat()
cat.say()
print('-------------------------isinstance()----------------------')
print(isinstance(dog, Dog))#True
print(isinstance(dog, Cat))#False
print(isinstance(dog, Animal))#True
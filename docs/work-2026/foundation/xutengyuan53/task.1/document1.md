# Python 进阶语法与技巧笔记

## 1. 基础容器：List（列表）与 Dict（字典）

*   **List（列表）**：就像超市的购物车，里面有顺序，可以随时往里塞或者拿东西
    ```python
    my_list = [1, 2, 3]
    my_list.append(4)

*   **Dict（字典）**：就像查字典，左边是“词”（Key），右边是“解释”（Value）
    ```python
    my_dict = {"name": "长门", "hp": 115}
    print(my_dict["name"])

## 2. 函数：Lambda 与 装饰器（Decorator）

*   **Lambda（匿名函数）**：就一用完就扔的临时工，适合写一行就能搞定的小逻辑，不需要专门 def 给个名字（简单一点：自己整一个函数出来用）
    ```python
    add = lambda x, y: x + y
    print(add(2, 3))

*   **Decorator（装饰器）**：就像给手机套个外壳，再比如喊你的工号就是喊你一样
    ```python
    import time

    def calculate_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"函数 {func.__name__} 运行耗时: {end - start:.4f} 秒")
            return result
        return wrapper

    @calculate_time
    def do_battle():
        time.sleep(0.5)
        print("战斗结束")

    do_battle()

## 3. 面向对象（OOP）与魔法方法（Magic Methods）

*   **Class（类）与 OOP 思想**：类就像是“造汽车的设计图纸”，而对象就是“按图纸造出来的一辆辆真车”;OOP 思想就是“把数据（车的颜色）和功能（车的加速）打包在一起”
    ```python
    class Character:
        def __init__(self, name: str, hp: int):
            self.name = name
            self.hp = hp

        def attack(self, target):
            print(f"{self.name} 攻击了 {target.name}！")
            target.hp -= 10
            print(f"{target.name} 剩余血量：{target.hp}")

    nagato = Character("长门", 115)
    nabiya = Character("娜比娅", 105)

    nagato.attack(nabiya) 

*   **Magic Methods（魔法方法）**：满足特定条件时会自动触发,比如 __init__ 是在创建对象时自动执行的初始化操作

## 4. 文本处理：re 正则表达式

*   **作用**：这段话里要什么自己捞
    ```python
    import re
    text = "我的电话是 13812345678"
    match = re.search(r"\d+", text) 
    print(match.group())

## 5. 代码格式：列表推导式与 Type Hint（类型提示）

*   **列表推导式**：直接把循环和条件塞进列表里做
    ```python
    squares = [x**2 for x in range(1, 6)] # 输出 [1, 4, 9, 16, 25]

*   **Type Hint**：直接告诉你要什么类型的，然后生成什么类型的
    ```python
    def greet(name: str) -> str:
        return "Hello " + name

## 进阶技巧：Generator 生成器（yield 关键字）

*   **作用**：如果要塞一大堆东西在列表里就用这玩意，一次只一个
    ```python
    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1
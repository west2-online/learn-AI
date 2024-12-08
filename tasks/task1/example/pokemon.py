from __future__ import annotations
import skills
from skills import Skill
from effects import Effect
import random


class Pokemon:
    name: str
    type: str

    def __init__(self, hp: int, attack: int, defense: int, dodgerate : int) -> None:
        # 初始化 Pokemon 的属性
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.dodgerate = dodgerate # 躲闪率
        self.skills = self.initialize_skills()
        self.alive = True
        self.statuses = []
        # self.protect_active = False
        self.protect_passive = False
        self.paralysis = False # 麻痹状态

    def initialize_skills(self):
        # 抽象方法，子类应实现具体技能初始化
        raise NotImplementedError

    def use_skill(self, skill: Skill, opponent: Pokemon):
        # 使用技能
        if self.paralysis and self.type != "Electricity":
            if random.randint(1, 100) <= 25:
                print("Oops, unable to move in a paralyzed state!")
        else :
            print(f"{self.name} uses {skill.name}")
            if skill.name =="Shield":# 杰尼龟是护盾防御，不是攻击手段，
                skill.execute(self, opponent)
            # skill.execute(self, opponent)
            elif random.randint(1, 100) <= opponent.dodgerate:
                print("Oh, what a pity, the attack was dodged!")
                print(f"{opponent.name} receive no damage! Remaining HP: {opponent.hp}/{opponent.max_hp}")
                if opponent.name == PikaChu:  ## bug
                    print("PikaChu成功躲闪，可以立即使用一次技能")
                    opponent.use_skill(opponent.skills[random.randint(0,1)], self)##################

            else :skill.execute(self, opponent)
        print("~" * 10+f"{self.name}'s skill is finished!"+"~" * 10)

    def heal_self(self, amount):
        # 为自身恢复生命值
        if not isinstance(amount, int):
            amount = int(amount)

        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} heals {amount} HP! Current HP: {self.hp}/{self.max_hp}")


    def vampire_self(self, amount):
        if not isinstance(amount, int):
            amount = int(amount)

        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        print(f"{self.name} is vampired {amount} HP! Current HP: {self.hp}/{self.max_hp}")

    # def judge_protecct(self):
    #     for status in self.statuses[:]:
    #         if status.name == "Protect":
    #             self.protect_active = True


    def receive_damage(self, damage):
        # 计算伤害并减去防御力，更新 HP
        value = 1 #添加全局引用词
        if not isinstance(damage, int):
            damage = int(damage) # 使用切片防止列表在遍历时被修改
        #护盾状态起效
        if "Protect" in self.statuses:
            # value -=0.5
            # self.protect_active = False
            for status in self.statuses[:]:
                if status.name == "Protect" :
                    self.statuses.remove(status)
                    value -= status.apply(self)
                    break
        #属性被动 #同一时间内一方面保护起作用
        elif self.protect_passive:
            value -=0.3
            self.protect_passive = False

        damage = damage * value - self.defense
        if damage <= 0:
            print(f"{self.name}'s defense absorbed the attack! Remaining HP: {self.hp}/{self.max_hp}")
            return

        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        print(
            f"{self.name} received {damage} damage! Remaining HP: {self.hp}/{self.max_hp}"
        )
        if self.hp <= 0:
            self.alive = False
            print(f"{self.name} has fainted!")

    def add_status_effect(self, effect: Effect):
        # 添加状态效果
        self.statuses.append(effect)

    def apply_status_effect(self):
        # 计数
        # 应用所有当前的状态效果，并移除持续时间结束的效果
        for status in self.statuses[:]:  # 使用切片防止列表在遍历时被修改
            if status.name =="Protect" :
                continue
            status.apply(self)
            status.decrease_duration()
            if status.duration <= 0:
                print(f"{self.name}'s {status.name} effect has worn off.")
                self.statuses.remove(status)
            print(f"   {self.name}'s {status.name} is over this round !")

    def type_effectiveness(self, opponent: Pokemon):
        # 计算属性克制的抽象方法，具体实现由子类提供
        raise NotImplementedError

    def begin(self):
        # 新回合开始时触发的方法
        pass

    def __str__(self) -> str:
        return f"{self.name} type: {self.type}"


# GlassPokemon 类
class GlassPokemon(Pokemon):
    type = "Glass"

    def type_effectiveness(self, opponent: Pokemon):
        # 针对敌方 Pokemon 的类型，调整效果倍率
        effectiveness = 1.0
        opponent_type = opponent.type

        if opponent_type == "Water":
            effectiveness = 2.0
        elif opponent_type == "Fire":
            effectiveness = 0.5
        return effectiveness

    def begin(self):# 被动属性
        # 每个回合开始时执行玻璃属性特性
        self.glass_attribute()

    def glass_attribute(self):
        # 玻璃属性特性：每回合恢复最大 HP 的 10%
        amount = self.max_hp * 0.1
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(
            f"{self.name} heals {amount} HP at the start of the turn! Current HP: {self.hp}/{self.max_hp}"
        )


# Bulbasaur 类，继承自 GlassPokemon
class Bulbasaur(GlassPokemon):
    name = "Bulbasaur"

    def __init__(self, hp=100, attack=30, defense=10, dodgerate=10) -> None:
        # 初始化 Bulbasaur 的属性
        super().__init__(hp, attack, defense,dodgerate)

    def initialize_skills(self):
        # 初始化技能，具体技能是 SeedBomb 和 ParasiticSeeds
        return [skills.SeedBomb(damage=35), skills.ParasiticSeeds()]


class WaterPokemon(Pokemon):
    type = "Water"
    def type_effectiveness(self, opponent: Pokemon):
        # 针对敌方 Pokemon 的类型，调整效果倍率
        effectiveness = 1.0
        opponent_type = opponent.type

        if opponent_type == "Fire":
            effectiveness = 2.0
        elif opponent_type == "Electricity":
            effectiveness = 0.5
        return effectiveness

    def begin(self):
        # 每个回合开始时执行水属性特性
        self.water_attribute()

    def water_attribute(self):#受到伤害时，有50%的几率减免30%的伤害（属性被动）
        if random.randint(1, 100) <= 50:
            self.protect_passive = True
            print(f"{self.name} turns on passive defense")
        #print(f"{self.name} didn't turn on passive defense")
        # amount = self.max_hp * 0.1
        # self.hp += amount
        # if self.hp > self.max_hp:
        #     self.hp = self.max_hp
        # print(
        #     f"{self.name} heals {amount} HP at the start of the turn! Current HP: {self.hp}/{self.max_hp}"
        # )


class Squirtle(WaterPokemon):
    name = "Squirtle"
    def __init__(self, hp=80, attack=25, defense=20, dodgerate=20 ) -> None:
        super().__init__(hp, attack, defense,dodgerate)
        # self.ability = 0.5
    def initialize_skills(self):
        # 初始化技能，具体技能是 SeedBomb 和 ParasiticSeeds
        # damage_modifier =  self.attack * self.type_effectiveness()
        return [skills.AquaJet(damage = self.attack), skills.Shield(ability = 0.5)]



class ElectricityPokemon(Pokemon):
    type = "Electricity"

    def type_effectiveness(self, opponent: Pokemon):
        # 针对敌方 Pokemon 的类型，调整效果倍率
        effectiveness = 1.0
        opponent_type = opponent.type

        if opponent_type == "Water":
            effectiveness = 2.0
        elif opponent_type == "Glass":
            effectiveness = 0.5
        return effectiveness

    def begin(self):
        # 每个回合开始时执行水属性特性
        self.electricity_attribute()

    def electricity_attribute(self):
        pass


class PikaChu(ElectricityPokemon):
    name = "PikaChu"

    def __init__(self, hp=80, attack=35, defense=5,dodgerate=30) -> None:
        super().__init__(hp, attack, defense,dodgerate)

    def initialize_skills(self):
        return [skills.Thunderbolt(damage = int (1.4 * self.attack ),activation_chance = 10), skills.QuickAttack(damage = self.attack , activation_chance = 10)]

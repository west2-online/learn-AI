from __future__ import annotations
import skills
from skills import Skill
from effects import Effect
from random import randint
import play

class Pokemon:
    name: str
    type: str

    def __init__(self, hp: int, attack: int, defense: int,evade:int) -> None:
        # 初始化 Pokemon 的属性
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.skills = self.initialize_skills()
        self.evade=evade  #初始化闪避率
        self.alive = True
        self.statuses = []

    def initialize_skills(self):
        # 抽象方法，子类应实现具体技能初始化
        raise NotImplementedError

    def use_skill(self, skill: Skill, opponent: Pokemon):
        # 使用技能
        print(f"{self.name} uses {skill.name}")
        skill.execute(self, opponent)

    def heal_self(self, amount):
        # 为自身恢复生命值
        if not isinstance(amount, int):
            amount = int(amount)

        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} heals {amount} HP! Current HP: {self.hp}/{self.max_hp}")

    def receive_damage(self, damage):
        # 计算伤害并减去防御力，更新 HP
        if not isinstance(damage, int):
            damage = int(damage)

        damage -= self.defense
        if damage <= 0:
            print(f"{self.name}'s defense absorbed the attack!")
            return

        self.hp -= damage
        print(
            f"{self.name} received {damage} damage! Remaining HP: {self.hp}/{self.max_hp}"
        )
        if self.hp <= 0:
            self.alive = False
            print(f"{self.name} has fainted!")

    def evade_damage(self) -> bool:
        # 判断是否成功躲避敌方属性伤害,躲避成功为True
       return randint(1, 100) <= self.evade


    def cause_damage(self, opponent:"Pokemon"):
        # 判断自己是否对敌方造成属性伤害,造成属性伤害为True
        return not opponent.evade_damage()

    def add_status_effect(self, effect: Effect):
        # 添加状态效果
        self.statuses.append(effect)

    def apply_status_effect(self):
        # 应用所有当前的状态效果，并移除持续时间结束的效果
        for status in self.statuses[:]:  # 使用切片防止列表在遍历时被修改
            status.apply(self)
            status.decrease_duration()
            if status.duration <= 0:
                print(f"{self.name}'s {status.name} effect has worn off.")
                self.statuses.remove(status)

    def type_effectiveness(self, opponent: Pokemon):
        # 计算属性克制的抽象方法，具体实现由子类提供
        raise NotImplementedError

    def begin(self):
        # 新回合开始时触发的方法,print("A new round begins......")
        pass


    def __str__(self) -> str:
        return f"{self.name} type: {self.type}"


# GrassPokemon 类
class GrassPokemon(Pokemon):
    type = "Grass"

    def type_effectiveness(self, opponent: Pokemon):
        # 针对敌方 Pokemon 的类型，调整效果倍率
        effectiveness = 1.0
        opponent_type = opponent.type

        if opponent_type == "Water":
            effectiveness = 2.0
        elif opponent_type == "Fire":
            effectiveness = 0.5
        return effectiveness

    def begin(self):
        # 每个回合开始时执行草属性特性
        self.grass_attribute()

    def grass_attribute(self):
        # 草属性特性：每回合恢复最大 HP 的 10%
        amount = self.max_hp * 0.1
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(
            f"{self.name} heals {amount} HP at the start of the turn! Current HP: {self.hp}/{self.max_hp}"
        )


class FirePokemon(Pokemon):
    type = "Fire"
    def begin(self):
        # 每个回合开始时执行火属性特性
        self.fire_attribute()

    def type_effectiveness(self, opponent: Pokemon):
        # 针对敌方 Pokemon 的类型，调整效果倍率
        effectiveness = 1.0
        opponent_type = opponent.type
        if opponent_type == "Glass":
            effectiveness = 2.0
        elif opponent_type == "Water":
            effectiveness = 0.5
        return effectiveness

    def fire_attribute(self):
        #火属性特性，每次造成伤害，叠加10%攻击力，最多4层

        if self.cause_damage(play.play1.current_computer_pokemon):
            max_attack=self.attack*(1+10/100)**2
            while self.attack<=max_attack:
                self.attack*=(1+10/100)






# Bulbasaur 类，继承自 GlassPokemon
class Bulbasaur(GrassPokemon):
    name = "Bulbasaur"

    def __init__(self, hp=100, attack=50, defense=10 , evade=10) -> None:
        # 初始化 Bulbasaur 的属性
        super().__init__(hp, attack, defense,evade)

    def initialize_skills(self):
        # 初始化技能，具体技能是 SeedBomb 和 ParasiticSeeds
        return [skills.SeedBomb(damage=60), skills.ParasiticSeeds(amount=10)]


# Charmande 类，继承自 GlassPokemon
class Charmander(FirePokemon):
    name = "Charmander"
    def __init__(self, hp=80, attack=35, defense=15, evade=10) -> None:
        # 初始化 Bulbasaur 的属性
        super().__init__(hp, attack, defense , evade)

    def initialize_skills(self):
        # 初始化技能，具体技能是 Ember 和 Flamecharge
        return [skills.Ember(damage=10), skills.Flamecharge(damage=10)]

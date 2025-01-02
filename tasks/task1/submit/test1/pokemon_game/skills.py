import random
from typing import TYPE_CHECKING
import effects

if TYPE_CHECKING:
    from pokemon import Pokemon

1
class Skill:
    name: str

    def __init__(self) -> None:
        pass

    def execute(self, user: "Pokemon", opponent: "Pokemon"):
        raise NotImplementedError





    def __str__(self) -> str:
        return f"{self.name}"


class SeedBomb(Skill):
    name = "Seed Bomb"

    def __init__(self, damage: int, activation_chance: int = 15) -> None:
        super().__init__()
        self.damage = damage
        self.activation_chance = activation_chance  # 确保激活几率被正确初始化

    def execute(self, user: "Pokemon", opponent: "Pokemon") -> None:

        # 判断是否造成伤害
        if opponent.evade_damage():
            print(
                f"{user.name} used {self.name}, but {opponent.name} dodged this damage.This attack did not cause any damage."
            )
        else:
            opponent.receive_damage(self.damage)
            print(
                f"{user.name} used {self.name}, dealing {self.damage} damage to {opponent.name}"
            )

            # 判断是否触发状态效果
            if random.randint(1, 100) <= self.activation_chance:
                opponent.add_status_effect(effects.PoisonEffect())
                print(f"{opponent.name} is poisoned by {self.name}!")
            else:
                print(f"{self.name} did not poison {opponent.name} this time.")




class ParasiticSeeds(Skill):
    name = "Parasitic Seeds"

    def __init__(self, amount: int) -> None:
        super().__init__()
        self.amount = amount

    def execute(self, user: "Pokemon", opponent: "Pokemon") -> None:
        # 给使用者添加治疗效果
        user.add_status_effect(effects.HealEffect(self.amount))
        print(f"{user.name} heals {self.amount} HP with {self.name}")

        # 给对手添加中毒效果
        opponent.add_status_effect(effects.PoisonEffect())
        print(f"{opponent.name} is poisoned by {self.name}!")

'''**火花 (Ember)：**小火龙发射出一团小火焰，对敌人造成 100% 火属性伤害，并有10%的几率使目标陷入“烧伤”状态（每回合受到10额外伤害， 持续2回合）
'''
class Ember(Skill):
    name = "Ember"

    def __init__(self, damage:int,activation_chance: int = 10) -> None:
        super().__init__()
        self.damage = damage
        self.activation_chance=activation_chance

    def execute(self, user: "Pokemon", opponent: "Pokemon") -> None:
        # 判断是否造成伤害
        if opponent.evade_damage():
            print(
                f"{user.name} used {self.name}, but {opponent.name} dodged this damage.This attack did not cause any damage."
            )
        else:
            opponent.receive_damage(self.damage)
            print(
                f"{user.name} used {self.name}, dealing {self.damage} damage to {opponent.name}"
            )

            # 判断是否触发状态效果
            if random.randint(1, 100) <= self.activation_chance:
                opponent.add_status_effect(effects.BurnEffect())
                print(f"{opponent.name} is burned by {self.name}!")
            else:
                print(f"{self.name} did not burn {opponent.name} this time.")


class Flamecharge(Skill):
    name = "Flame Charge"
    is_charging = True  # 标记是否正在蓄能
    '''蓄能爆炎 (Flame Charge )：**小火龙召唤出强大的火焰，对敌人造成 300% 火属性伤害，并有80%的几率使敌人陷入“烧伤”状态，
    这个技能需要1个回合的蓄力，并且在面对该技能时敌方闪避率增加 20%'''
    def __init__(self, damage: int, activation_chance: int = 80,opponent_dodge_rate : int = 20) -> None:

        super().__init__()
        self.damage = damage
        self.activation_chance = activation_chance
        self.opponent_dodge_rate = opponent_dodge_rate


    def execute(self, user: "Pokemon", opponent: "Pokemon",play:"Play") -> None:
    # 造成伤害
        last_exe_turn=0  #记录最近一次使用该技能的游戏轮次
        if play.turn - last_exe_turn >= 2:
            self.is_charging = False

        if self.is_charging:
            print("Charmander is charging for Flame Charge...")

        else:
            opponent.evade+=self.opponent_dodge_rate

            if opponent.evade_damage(user, opponent):
                print(
                    f"{user.name} used {self.name}, but {opponent.name} dodged this damage.This attack did not cause any damage."
                )
            else:
                opponent.receive_damage(self.damage)
                print(
                    f"{user.name} used {self.name}, dealing {self.damage} damage to {opponent.name}"
                )

                # 判断是否触发状态效果
                if random.randint(1, 100) <= self.activation_chance:
                    opponent.add_status_effect(effects.BurnEffect())
                    print(f"{opponent.name} is burned by {self.name}!")
                    last_exe_turn=play.turn   #更新最近一次使用该技能的游戏轮次
                    self.is_charging = True    # 重新开始蓄能

import random

class Attribute:
    def __init__(self, name, weakness, resistance, passive_description):
        self.name = name
        self.weakness = weakness
        self.resistance = resistance
        self.passive_description = passive_description

class Pokemon:
    def __init__(self, name, hp, attack, defense, dodge_rate, attribute):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.dodge_rate = dodge_rate
        self.attribute = attribute
        self.skills = []
        self.passive_active = False
        self.status_effects = []
    
    def add_skill(self, skill):
        self.skills.append(skill)
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} 昏厥了！")
        return self.hp

    def apply_passive(self):
        pass

    def apply_status_effects(self):
        new_status_effects = []
        for effect in self.status_effects:
            if effect['type'] == 'burn':
                self.take_damage(10)
                print(f"{self.name} 受到了 10 点烧伤伤害！")
            elif effect['type'] == 'parasitic_seeds':
                self.take_damage(self.max_hp * 0.1)
                print(f"{self.name} 受到了 10% 最大生命值的伤害！")
            effect['duration'] -= 1
            if effect['duration'] > 0:
                new_status_effects.append(effect)
        self.status_effects = new_status_effects

    def attack_opponent(self, skill, opponent):
        print(f"{self.name} 使用了 {skill.name}!")
        if random.randint(1, 100) <= opponent.dodge_rate:
            print(f"{opponent.name} 躲闪成功！")
            if opponent.attribute.name == "电":
                print(f"{opponent.name} 的被动触发，可以立即使用技能!")
                return False
        else:
            damage = skill.use(self, opponent)
            print(f"{opponent.name} 受到了 {damage} 点伤害！剩余 HP: {opponent.hp}")
        return True

class Skill:
    def __init__(self, name, power, multiplier, special_effect=None):
        self.name = name
        self.power = power
        self.multiplier = multiplier
        self.special_effect = special_effect

    def use(self, attacker, opponent):
        damage = (attacker.attack * self.multiplier) - opponent.defense
        damage = max(damage, 0)
        
        # 属性克制效果
        if attacker.attribute.weakness == opponent.attribute.name:
            damage *= 2
        elif attacker.attribute.resistance == opponent.attribute.name:
            damage /= 2
        
        # 处理特殊效果
        if self.special_effect:
            self.special_effect(attacker, opponent)
        
        opponent.take_damage(damage)
        return damage

# 特殊效果函数
def paralysis_effect(attacker, opponent):
    if random.random() <= 0.1:
        print(f"{opponent.name} 被麻痹了！")

def poison_effect(attacker, opponent):
    if random.random() <= 0.15:
        print(f"{opponent.name} 中毒了！每回合将损失10%最大生命值！")

def water_effect(attacker, opponent):
    if random.random() <= 0.1:
        print(f"{opponent.name} 被水流困住了！")

def quick_attack_effect(attacker, opponent):
    if random.random() <= 0.1:
        print(f"{attacker.name} 的电光一闪触发了第二次攻击！")
        damage = (attacker.attack * 1.0) - opponent.defense
        damage = max(damage, 0)
        opponent.take_damage(damage)
        print(f"{opponent.name} 受到了 {damage} 点伤害！剩余 HP: {opponent.hp}")

def parasitic_seeds_effect(attacker, opponent):
    opponent.status_effects.append({'type': 'parasitic_seeds', 'duration': 3})
    print(f"{opponent.name} 被寄生种子击中！每回合将损失10%最大生命值，持续3回合！")

def shield_effect(attacker, opponent):
    attacker.defense *= 2
    print(f"{attacker.name} 使用了护盾，防御力提升50%！")

def burn_effect(attacker, opponent):
    if random.random() <= 0.1:
        opponent.status_effects.append({'type': 'burn', 'duration': 2})
        print(f"{opponent.name} 被烧伤了！每回合将受到10点额外伤害，持续2回合！")

def flame_charge_effect(attacker, opponent):
    if random.random() <= 0.8:
        opponent.status_effects.append({'type': 'burn', 'duration': 2})
        print(f"{opponent.name} 被烧伤了！每回合将受到10点额外伤害，持续2回合！")

# 定义宝可梦及其技能
class ElectricPokemon(Pokemon):
    def apply_passive(self):
        # 如果闪避成功，触发被动
        pass

class GrassPokemon(Pokemon):
    def apply_passive(self):
        # 每回合恢复最大生命值的10%
        recovery = self.max_hp * 0.1
        self.hp = min(self.hp + recovery, self.max_hp)
        print(f"{self.name} 回了 {int(recovery)} 点 HP！")

class WaterPokemon(Pokemon):
    def apply_passive(self):
        # 受到伤害时，有50%的几率减免30%的伤害
        pass

class FirePokemon(Pokemon):
    def apply_passive(self):
        # 每次造成伤害，叠加10%攻击力，最多4层
        pass

class SoilPokemon(Pokemon):
    def apply_passive(self):
        # 每回合回复10%最大HP
        recovery = self.max_hp * 0.1
        self.hp = min(self.hp + recovery, self.max_hp)
        print(f"{self.name} 回了 {int(recovery)} 点 HP！")

# 宝可梦及其属性
electric_attr = Attribute("电", "水", "草", "成功闪避时可以立即使用一次技能")
grass_attr = Attribute("草", "水", "火", "每回合回复10%最大HP")
water_attr = Attribute("水", "火", "电", "受到伤害时，有50%的几率减免30%的伤害")
fire_attr = Attribute("火", "草", "水", "每次造成伤害，叠加10%攻击力，最多4层")
soil_attr = Attribute("土", "电", "水", "每回合回复10%最大HP")

# 定义宝可梦
pikachu = ElectricPokemon("皮卡丘", 80, 35, 5, 30, electric_attr)
pikachu.add_skill(Skill("十万伏特", 35, 1.4, paralysis_effect))
pikachu.add_skill(Skill("电光一闪", 35, 1.0, quick_attack_effect))

bulbasaur = GrassPokemon("妙蛙种子", 100, 35, 10, 10, grass_attr)
bulbasaur.add_skill(Skill("种子炸弹", 35, 1.0, poison_effect))
bulbasaur.add_skill(Skill("寄生种子", 0, 0.0, parasitic_seeds_effect))

Squirtle = WaterPokemon("杰尼龟", 80, 25, 20, 20, water_attr)
Squirtle.add_skill(Skill("水枪", 25, 1.4, water_effect))
Squirtle.add_skill(Skill("护盾", 0, 0.0, shield_effect))

Charmander = FirePokemon("小火龙", 80, 35, 15, 10, fire_attr)
Charmander.add_skill(Skill("火花", 35, 1.0, burn_effect))
Charmander.add_skill(Skill("蓄能爆炎", 35, 3.0, flame_charge_effect))

karbi = SoilPokemon("可拉比", 80, 25, 20, 10, soil_attr)
karbi.add_skill(Skill("土冻拳", 25, 1.4))
karbi.add_skill(Skill("土冻之息", 25, 1.0, poison_effect))

# 游戏逻辑
def choose_pokemon(pokemon_list):
    print("请选择3个宝可梦用于组成你的队伍：")
    for i, pokemon in enumerate(pokemon_list):
        print(f"{i+1}.{pokemon.name}({pokemon.attribute.name}属性)")
    choices = input("输入数字选择你的宝可梦(用空格分隔): ").split()
    player_team = [pokemon_list[int(choice)-1] for choice in choices]
    return player_team

def choose_opponent(pokemon_list, player_team):
    available_pokemon = [p for p in pokemon_list]
    if len(available_pokemon) < 3:
        raise ValueError("选择的宝可梦数量不足3个，请重新选择你的队伍。")
    opponent_team = random.sample(available_pokemon, 3)
    return opponent_team

def choose_battle_pokemon(team):
    print("请选择你的宝可梦：")
    for i, pokemon in enumerate(team):
        print(f"{i+1}.{pokemon.name}({pokemon.attribute.name}属性)")
    choice = int(input("输入数字选择你的宝可梦: "))
    return team[choice-1]

def battle(player_pokemon, opponent_pokemon):
    while player_pokemon.hp > 0 and opponent_pokemon.hp > 0:
        player_pokemon.apply_status_effects()
        opponent_pokemon.apply_status_effects()
        
        print(f"你的 {player_pokemon.name} 的技能:")
        for i, skill in enumerate(player_pokemon.skills):
            print(f"{i+1}. {skill.name}")
        choice = int(input("选择一个技能进行攻击: "))
        player_pokemon.attack_opponent(player_pokemon.skills[choice-1], opponent_pokemon)
        
        if opponent_pokemon.hp > 0:
            opponent_skill = random.choice(opponent_pokemon.skills)
            opponent_pokemon.attack_opponent(opponent_skill, player_pokemon)

def main():
    pokemon_list = [pikachu, bulbasaur, Squirtle, Charmander, karbi]
    while True:
        player_team = choose_pokemon(pokemon_list)
        try:
            opponent_team = choose_opponent(pokemon_list, player_team)
            break
        except ValueError as e:
            print(e)
    
    player_pokemon = choose_battle_pokemon(player_team)
    opponent_pokemon = random.choice(opponent_team)
    
    print(f"你选择了 {player_pokemon.name}!")
    print(f"电脑选择了 {opponent_pokemon.name}!")
    
    battle(player_pokemon, opponent_pokemon)

if __name__ == "__main__":
    main()

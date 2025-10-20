# answer.py

import random
import time

# --- 战斗设定 (这些是预设好的值，不需要修改哦) ---
NAGATO_MAX_HP = 120
NABIYA_MAX_HP = 100
NAGATO_ATTACK_DICE = 4
NAGATO_DEFEND_DICE = 3
NABIYA_ATTACK_DICE = 4
NABIYA_DEFEND_DICE = 3
SPECIAL_ATTACK_DAMAGE = 30
CRITICAL_HIT_THRESHOLD = 18


# 任务一：显示角色状态
def display_status(character_name, current_hp, max_hp):
    """打印格式: 【角色名】HP: 当前血量 / 最大血量"""
    # 使用f-string可以很方便地将变量嵌入到字符串中
    print(f"【{character_name}】HP: {current_hp} / {max_hp}")


# 任务二：掷骰子
def roll_dice(num_dice):
    """用while循环，模拟掷N个骰子，返回总点数"""
    total_points = 0
    count = 0
    # 当count小于需要掷的次数时，循环就会继续
    while count < num_dice:
        # 模拟掷一次骰子，并将点数加到总和上
        roll = random.randint(1, 6)
        total_points = total_points + roll
        # 记得要增加count的值，否则循环不会停止哦！
        count = count + 1
    return total_points


# 任务三：选择长门的行动
def choose_nagato_action(nagato_hp, nabiya_hp):
    """用if/elif/else，根据血量返回 'attack', 'defend', 或 'special'"""
    # if/elif/else的顺序很重要，程序会从上到下检查第一个满足的条件
    if nagato_hp < 30:
        return 'defend'
    elif nabiya_hp < 20:
        return 'special'
    else:
        return 'attack'


# 任务四：计算攻击伤害
def calculate_attack_damage(num_dice):
    """调用 roll_dice() 函数来计算伤害"""
    # 直接将另一个函数的结果返回，这是一种很常见的做法
    return roll_dice(num_dice)


# 任务五：计算防御值
def calculate_defense_value(num_dice):
    """调用 roll_dice() 函数来计算防御值"""
    return roll_dice(num_dice)


# 任务六：检查是否暴击 (BIG SEVEN)
def check_critical_hit(base_damage):
    """如果伤害 >= 18，返回 True，否则返回 False"""
    if base_damage >= CRITICAL_HIT_THRESHOLD:
        return True
    else:
        return False


# 任务七：娜比娅的AI行动
def nabiya_ai_action(nabiya_hp):
    """如果娜比娅HP <= 40，返回 'defend'，否则返回 'attack'"""
    # 对于简单的二选一逻辑，一个if/else就足够了
    if nabiya_hp <= 40:
        return 'defend'
    else:
        return 'attack'


# 任务八：核心战斗循环
def main_battle_loop():
    """
    这是最重要的部分！将所有零件组装成一台可以运转的战斗引擎！
    """
    # 1. 初始化长门和娜比娅的HP，以及双方的防御值
    nagato_hp = NAGATO_MAX_HP
    nabiya_hp = NABIYA_MAX_HP
    nagato_defense_bonus = 0
    nabiya_defense_bonus = 0
    turn = 1

    # 2. 编写 while 循环，在双方都存活时继续战斗
    while nagato_hp > 0 and nabiya_hp > 0:

        print(f"\n======== 回合 {turn} ========")
        display_status("长门", nagato_hp, NAGATO_MAX_HP)
        display_status("娜比娅", nabiya_hp, NABIYA_MAX_HP)
        time.sleep(1)

        # 3. --- 长门的回合 ---
        print("\n>>> 长门的回合")
        action = choose_nagato_action(nagato_hp, nabiya_hp)
        
        if action == 'attack':
            print("长门：「感受BIG SEVEN的威力吧！」")
            base_damage = calculate_attack_damage(NAGATO_ATTACK_DICE)
            if check_critical_hit(base_damage):
                print("💥「BIG SEVEN」触发！伤害翻倍！")
                base_damage = base_damage * 2
            
            # 伤害需要减去对方的防御值
            final_damage = base_damage - nabiya_defense_bonus
            if final_damage < 0:
                final_damage = 0
            
            print(f"长门的主炮对娜比娅造成了 {final_damage} 点伤害！")
            nabiya_hp -= final_damage
            nabiya_defense_bonus = 0 # 对方的防御值在本回合被消耗掉了
        
        elif action == 'defend':
            print("长门：「神子的威仪，汝岂能冒犯！」")
            nagato_defense_bonus = calculate_defense_value(NAGATO_DEFEND_DICE)
            print(f"长门进入防御姿态，获得了 {nagato_defense_bonus} 点威仪值。")
            
        else: # 'special'
            print("长门：「「四万神的守护」！」")
            if random.random() < 0.5: # 50%的成功率
                print("守护之力成功降临！")
                final_damage = SPECIAL_ATTACK_DAMAGE - nabiya_defense_bonus
                if final_damage < 0:
                    final_damage = 0
                print(f"对娜比娅造成了固定的 {final_damage} 点伤害！")
                nabiya_hp -= final_damage
                nabiya_defense_bonus = 0
            else:
                print("唔…失手了…本次攻击没有造成伤害。")
        
        # 4. 检查娜比娅是否被击败
        if nabiya_hp <= 0:
            print("\n娜比娅的HP归零！")
            display_status("娜比娅", 0, NABIYA_MAX_HP)
            print("\n长门获得了胜利！成功守护了港区的军粮！")
            break
        
        time.sleep(2) # 增加回合间的停顿

        # 5. --- 娜比娅的回合 ---
        print("\n>>> 娜比娅的回合")
        enemy_action = nabiya_ai_action(nabiya_hp)

        if enemy_action == 'attack':
            print("娜比娅：「嘿咻~尝尝这个！」")
            enemy_damage = calculate_attack_damage(NABIYA_ATTACK_DICE)
            final_damage = enemy_damage - nagato_defense_bonus
            if final_damage < 0:
                final_damage = 0
            
            print(f"娜比娅的攻击对长门造成了 {final_damage} 点伤害！")
            nagato_hp -= final_damage
            nagato_defense_bonus = 0
        
        else: # 'defend'
            print("娜比娅：「先、先躲起来…」")
            nabiya_defense_bonus = calculate_defense_value(NABIYA_DEFEND_DICE)
            print(f"娜比娅进入防御姿态，获得了 {nabiya_defense_bonus} 点防御值。")
        
        # 6. 检查长门是否被击败
        if nagato_hp <= 0:
            print("\n长门的HP归零！")
            display_status("长门", 0, NAGATO_MAX_HP)
            print("\n战斗失败…看来娜比娅把偷吃的力气都用上了…")
            break

        turn = turn + 1
        time.sleep(2)


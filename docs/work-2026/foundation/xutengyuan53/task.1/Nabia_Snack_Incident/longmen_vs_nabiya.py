"""娜比娅偷吃事件：回合制战斗练习。"""

from __future__ import annotations

import random
import time
from typing import Literal

Action = Literal["attack", "defend", "special"]
NabiyaAction = Literal["attack", "defend"]
BattleResult = Literal["nagato", "nabiya", "draw"]

# 这些数值可以让战斗持续数个回合，同时让防御有用但不会抵消大多数普通攻击。
NAGATO_MAX_HP = 115
NABIYA_MAX_HP = 105
NAGATO_ATTACK_DICE = 3
NAGATO_DEFEND_DICE = 2
NABIYA_ATTACK_DICE = 3
NABIYA_DEFEND_DICE = 2
SPECIAL_ATTACK_DAMAGE = 24
SPECIAL_ATTACK_SUCCESS_RATE = 0.45
CRITICAL_HIT_THRESHOLD = 15

NAGATO_LOW_HP_THRESHOLD = 30
NABIYA_SPECIAL_HP_THRESHOLD = 20
NABIYA_DEFEND_HP_THRESHOLD = 40
MAX_BATTLE_TURNS = 50


def display_status(character_name: str, current_hp: int, max_hp: int) -> None:
    """输出角色状态，格式为：[角色名]HP: 当前生命值 / 最大生命值。"""
    if max_hp <= 0:
        raise ValueError("最大生命值必须大于 0")
    print(f"[{character_name}]HP: {current_hp} / {max_hp}")


def roll_dice(num_dice: int) -> int:
    """投掷指定数量的六面骰子并返回点数总和。"""
    # TODO：先处理非法骰子数量，再用 while 循环调用 random.randint(1, 6)。
    if num_dice <= 0:
        raise ValueError("骰子数量必须大于 0")
    total = 0
    count = 0
    while count < num_dice:
        total += random.randint(1, 6)
        count += 1
    return total


def choose_nagato_action(nagato_hp: int, nabiya_hp: int) -> Action:
    """根据双方生命值选择长门的行动。"""
    # TODO：长门生命值低于 30 时防御，娜比娅生命值低于 20 时使用特殊攻击，
    # TODO：其余情况进行普通攻击；注意使用 if/elif/else 保持判断顺序。
    if nagato_hp < NAGATO_LOW_HP_THRESHOLD:
        return "defend"
    elif nabiya_hp < NABIYA_SPECIAL_HP_THRESHOLD:
        return "special"
    else:
        return "attack"


def calculate_attack_damage(num_dice: int) -> int:
    """调用 roll_dice() 计算基础攻击伤害。"""
    # TODO：把骰子数量传给 roll_dice()，并返回它的结果。
    return roll_dice(num_dice)


def calculate_defense_value(num_dice: int) -> int:
    """调用 roll_dice() 计算本回合的防御值。"""
    # TODO：把骰子数量传给 roll_dice()，并返回它的结果。
    return roll_dice(num_dice)


def check_critical_hit(base_damage: int) -> bool:
    """判断基础伤害是否达到暴击阈值。"""
    # TODO：当基础伤害大于等于 CRITICAL_HIT_THRESHOLD 时返回 True。
    if base_damage >= CRITICAL_HIT_THRESHOLD:
        return True
    return False


def nabiya_ai_action(nabiya_hp: int) -> NabiyaAction:
    """根据娜比娅生命值选择她的行动。"""
    # TODO：娜比娅生命值小于等于 40 时防御，否则攻击。
    if nabiya_hp <= NABIYA_DEFEND_HP_THRESHOLD:
        return "defend"
    else:
        return "attack"


def calculate_final_damage(base_damage: int, defense_bonus: int) -> int:
    """用防御值抵消基础伤害，并返回不会小于零的最终伤害。"""
    # TODO：拒绝负数伤害或防御值，再计算 max(0, 基础伤害 - 防御值)。
    if base_damage < 0 or defense_bonus < 0:
        raise ValueError("伤害或防御值不能为负数")
    final_damage = base_damage - defense_bonus
    return max(0, final_damage)


def apply_damage(current_hp: int, base_damage: int, defense_bonus: int = 0) -> int:
    """结算一次攻击并返回不会小于零的剩余生命值。"""
    # TODO：调用 calculate_final_damage()，再从当前生命值中扣除最终伤害。
    final_damage = calculate_final_damage(base_damage, defense_bonus)
    remaining_hp = current_hp - final_damage
    return max(0, remaining_hp)


def is_battle_over(nagato_hp: int, nabiya_hp: int) -> bool:
    """判断是否至少有一名角色的生命值归零。"""
    # TODO：只要任意一方 HP 小于等于 0，就返回 True。
    return nagato_hp <= 0 or nabiya_hp <= 0


def get_battle_result(nagato_hp: int, nabiya_hp: int) -> BattleResult:
    """根据双方剩余生命值返回胜者或平局。"""
    # TODO：仅一方存活时返回对应结果；双方同时归零或都存活时返回 draw。
    if nagato_hp > 0 and nabiya_hp <= 0:
        return "nagato"
    elif nabiya_hp > 0 and nagato_hp <= 0:
        return "nabiya"
    else:
        return "draw"


def main_battle_loop(
    pause_seconds: float = 0.0,
    max_turns: int = MAX_BATTLE_TURNS,
) -> BattleResult:
    """运行完整战斗，并返回 nagato、nabiya 或 draw。"""
    # TODO：先检查 pause_seconds 和 max_turns 是否合理，不合理时抛出 ValueError。
    # TODO：初始化 nagato_hp、nabiya_hp、nagato_defense_bonus、
    # TODO：nabiya_defense_bonus，以及从 1 开始的 turn。
    if pause_seconds < 0 or max_turns <= 0:
        raise ValueError("暂停时间不能为负,回合数必须大于0")
    nagato_hp = NAGATO_MAX_HP
    nabiya_hp = NABIYA_MAX_HP
    nagato_defense_bonus = 0
    nabiya_defense_bonus = 0
    turn = 1
    # TODO：战斗循环可以按照下面的结构开始：
    while nagato_hp > 0 and nabiya_hp > 0 and turn <= max_turns:
        print(f"\n--- 第 {turn} 回合 ---")
        display_status("长门", nagato_hp, NAGATO_MAX_HP)
        display_status("娜比娅", nabiya_hp, NABIYA_MAX_HP)
    #     输出当前回合和双方状态。
    #
    # TODO：长门回合：
    # 1. 调用 choose_nagato_action(nagato_hp, nabiya_hp) 获取 action。
    # 2. action == "attack" 时，调用 calculate_attack_damage()；
    #    如果 check_critical_hit() 返回 True，就把基础伤害翻倍。
    # 3. action == "defend" 时，调用 calculate_defense_value()，
    #    把结果保存到 nagato_defense_bonus。
    # 4. action == "special" 时，用 random.random() 判断是否小于
    #    SPECIAL_ATTACK_SUCCESS_RATE；成功时使用 SPECIAL_ATTACK_DAMAGE。
    # 5. 造成伤害时统一调用 apply_damage()，并在攻击后清零对方的防御值。
    # 6. 长门行动后，如果 is_battle_over() 返回 True，使用 break 结束循环。
        action = choose_nagato_action(nagato_hp, nabiya_hp)
        if action == "attack":
            base_damage = calculate_attack_damage(NAGATO_ATTACK_DICE)
            if check_critical_hit(base_damage):
                    print("触发暴击！")
                    base_damage *= 2
            nabiya_hp = apply_damage(nabiya_hp, base_damage, nabiya_defense_bonus)
            print(f"长门攻击，造成 {base_damage} 点伤害！")
        elif action == "defend":
                nagato_defense_bonus = calculate_defense_value(NAGATO_DEFEND_DICE)
                print(f"长门防御，获得 {nagato_defense_bonus} 点护盾！")
        elif action == "special":
            if random.random() < SPECIAL_ATTACK_SUCCESS_RATE:
                nabiya_hp = apply_damage(nabiya_hp, SPECIAL_ATTACK_DAMAGE, nabiya_defense_bonus)
                print(f"长门使用特殊攻击，造成 {SPECIAL_ATTACK_DAMAGE} 点伤害！")
            else:
                print("长门的特殊攻击失败了！")
        if is_battle_over(nagato_hp, nabiya_hp):
            break
    # TODO：娜比娅回合：
    # 1. 调用 nabiya_ai_action(nabiya_hp) 获取 enemy_action。
    # 2. attack 时调用 calculate_attack_damage()，再用 apply_damage()
    #    扣除长门生命值；defend 时保存娜比娅的防御值。
    # 3. 娜比娅的攻击或防御结束后，清零已经消耗的长门防御值。
        enemy_action = nabiya_ai_action(nabiya_hp)

        if enemy_action == "attack":
            enemy_damage = calculate_attack_damage(NABIYA_ATTACK_DICE)
            nagato_hp = apply_damage(
                base_damage=enemy_damage,
                current_hp=nagato_hp,
                defense_bonus=nagato_defense_bonus,
            )
            nagato_defense_bonus = 0
            print(f"娜比娅发起攻击，长门剩余 {nagato_hp} 点生命值。")
        else:
            nabiya_defense_bonus = calculate_defense_value(NABIYA_DEFEND_DICE)
            print(f"娜比娅进入防御姿态，获得 {nabiya_defense_bonus} 点防御值。")
        if is_battle_over(nagato_hp, nabiya_hp):
            break
    # TODO：双方回合完成后让 turn 增加 1，并根据 pause_seconds 调用 time.sleep()。
    # TODO：循环结束后调用 get_battle_result()，输出中文结果并返回 result。
        turn += 1
        if pause_seconds > 0:
            time.sleep(pause_seconds)
    result = get_battle_result(nagato_hp, nabiya_hp)
    if result == "nagato":
        print("\n长门获得胜利!")
    elif result == "nabiya":
        print("\n娜比娅获得胜利!")
    else:
        print("\n战斗在达到回合上限后以平局结束。")
    return result

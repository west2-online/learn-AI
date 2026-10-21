"""一个支持确定性测试的回合制战斗练习。"""

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
    """按照固定格式输出角色的生命值。"""
    if max_hp <= 0:
        raise ValueError("最大生命值必须大于零")

    shown_hp = max(0, min(current_hp, max_hp))
    print(f"[{character_name}]HP: {shown_hp} / {max_hp}")


def roll_dice(num_dice: int) -> int:
    """投掷 ``num_dice`` 个六面骰子并返回点数总和。"""
    if num_dice < 0:
        raise ValueError("骰子数量不能为负数")

    total_points = 0
    count = 0
    while count < num_dice:
        total_points += random.randint(1, 6)
        count += 1
    return total_points


def choose_nagato_action(nagato_hp: int, nabiya_hp: int) -> Action:
    """根据当前生命值选择长门的行动。"""
    if nagato_hp < NAGATO_LOW_HP_THRESHOLD:
        return "defend"
    if nabiya_hp < NABIYA_SPECIAL_HP_THRESHOLD:
        return "special"
    return "attack"


def calculate_attack_damage(num_dice: int) -> int:
    """投掷攻击骰子并返回基础伤害。"""
    return roll_dice(num_dice)


def calculate_defense_value(num_dice: int) -> int:
    """投掷防御骰子并返回本回合的防御值。"""
    return roll_dice(num_dice)


def check_critical_hit(base_damage: int) -> bool:
    """判断基础伤害是否达到暴击阈值。"""
    return base_damage >= CRITICAL_HIT_THRESHOLD


def nabiya_ai_action(nabiya_hp: int) -> NabiyaAction:
    """娜比娅生命值较低时防御，否则攻击。"""
    if nabiya_hp <= NABIYA_DEFEND_HP_THRESHOLD:
        return "defend"
    return "attack"


def calculate_final_damage(base_damage: int, defense_bonus: int) -> int:
    """用防御值抵消伤害，并保证最终伤害不会小于零。"""
    if base_damage < 0:
        raise ValueError("基础伤害不能为负数")
    if defense_bonus < 0:
        raise ValueError("防御值不能为负数")
    return max(0, base_damage - defense_bonus)


def apply_damage(current_hp: int, base_damage: int, defense_bonus: int = 0) -> int:
    """结算一次攻击并返回剩余生命值，生命值最低为零。"""
    damage = calculate_final_damage(base_damage, defense_bonus)
    return max(0, current_hp - damage)


def is_battle_over(nagato_hp: int, nabiya_hp: int) -> bool:
    """判断是否至少有一名角色的生命值归零。"""
    return nagato_hp <= 0 or nabiya_hp <= 0


def get_battle_result(nagato_hp: int, nabiya_hp: int) -> BattleResult:
    """返回胜者；如果无法唯一判断，则返回平局。"""
    if nagato_hp > 0 and nabiya_hp <= 0:
        return "nagato"
    if nabiya_hp > 0 and nagato_hp <= 0:
        return "nabiya"
    return "draw"


def _pause(seconds: float) -> None:
    """只有调用者要求展示战斗动画时才暂停。"""
    if seconds > 0:
        time.sleep(seconds)


def main_battle_loop(
    pause_seconds: float = 0.0,
    max_turns: int = MAX_BATTLE_TURNS,
) -> BattleResult:
    """运行战斗，并返回 ``nagato``、``nabiya`` 或 ``draw``。"""
    if pause_seconds < 0:
        raise ValueError("暂停时间不能为负数")
    if max_turns <= 0:
        raise ValueError("最大回合数必须大于零")

    nagato_hp = NAGATO_MAX_HP
    nabiya_hp = NABIYA_MAX_HP
    nagato_defense_bonus = 0
    nabiya_defense_bonus = 0
    turn = 1

    while not is_battle_over(nagato_hp, nabiya_hp) and turn <= max_turns:
        print(f"\n======== 第 {turn} 回合 ========")
        display_status("长门", nagato_hp, NAGATO_MAX_HP)
        display_status("娜比娅", nabiya_hp, NABIYA_MAX_HP)

        print("\n>>> 长门的回合")
        action = choose_nagato_action(nagato_hp, nabiya_hp)

        if action == "attack":
            base_damage = calculate_attack_damage(NAGATO_ATTACK_DICE)
            if check_critical_hit(base_damage):
                base_damage *= 2
                print("触发 BIG SEVEN：造成暴击伤害！")
            nabiya_hp = apply_damage(base_damage=base_damage,
                                      current_hp=nabiya_hp,
                                      defense_bonus=nabiya_defense_bonus)
            nabiya_defense_bonus = 0
            print(f"长门造成了伤害，娜比娅剩余 {nabiya_hp} 点生命值。")
        elif action == "defend":
            nagato_defense_bonus = calculate_defense_value(NAGATO_DEFEND_DICE)
            print(f"长门进入防御姿态，获得 {nagato_defense_bonus} 点防御值。")
        else:
            if random.random() < SPECIAL_ATTACK_SUCCESS_RATE:
                nabiya_hp = apply_damage(
                    base_damage=SPECIAL_ATTACK_DAMAGE,
                    current_hp=nabiya_hp,
                    defense_bonus=nabiya_defense_bonus,
                )
                print(f"长门的特殊攻击成功，娜比娅剩余 {nabiya_hp} 点生命值。")
            else:
                print("长门的特殊攻击失败了，没有造成伤害。")
            nabiya_defense_bonus = 0

        if is_battle_over(nagato_hp, nabiya_hp):
            break

        _pause(pause_seconds)
        print("\n>>> 娜比娅的回合")
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

        turn += 1
        _pause(pause_seconds)

    result = get_battle_result(nagato_hp, nabiya_hp)
    if result == "nagato":
        print("\n长门获得胜利！")
    elif result == "nabiya":
        print("\n娜比娅获得胜利！")
    else:
        print("\n战斗在达到回合上限后以平局结束。")
    return result

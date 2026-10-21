"""针对 longmen_vs_nabiya.py 的运行行为检查。"""

import io
import sys
from contextlib import redirect_stdout
from unittest.mock import patch


def print_check(name, success):
    """输出一项检查的结果。"""
    status = "通过" if success else "失败"
    print(f"[{status}] {name}")
    return success


def print_info(message):
    """输出检查提示。"""
    print(f"    提示：{message}")


def expect_cases(name, cases):
    """运行一组测试数据，并报告每组测试的汇总结果。"""
    results = []
    for case_name, case in cases:
        try:
            result = case()
        except Exception as error:
            result = False
            print_info(f"{case_name}：出现 {type(error).__name__}：{error}")
        results.append(result)
        if not result:
            print_info(f"{case_name}：未通过")
    return print_check(name, all(results))


def raises_value_error(function):
    """检查函数是否抛出 ValueError。"""
    try:
        function()
    except ValueError:
        return True
    except Exception:
        return False
    return False


try:
    import longmen_vs_nabiya as battle
except (ImportError, SyntaxError) as error:
    print("[失败] 无法导入 longmen_vs_nabiya.py")
    print_info(f"请先检查文件中的语法或导入问题：{error}")
    sys.exit(1)


passed_checks = 0
total_checks = 0


print("--- 战斗代码检查开始 ---\n")

try:
    status_output = io.StringIO()
    with redirect_stdout(status_output):
        battle.display_status("长门", 100, battle.NAGATO_MAX_HP)
    status_text = status_output.getvalue().strip()
    status_ok = status_text == f"[长门]HP: 100 / {battle.NAGATO_MAX_HP}"
except Exception as error:
    status_ok = False
    print_info(f"display_status：出现 {type(error).__name__}：{error}")
if print_check("display_status 按要求输出格式", status_ok):
    passed_checks += 1
total_checks += 1


random_module = getattr(battle, "random", None)
if random_module is None:
    dice_ok = False
    print_info("roll_dice：请先在 longmen_vs_nabiya.py 中导入 random")
else:
    with patch.object(random_module, "randint", side_effect=[1, 6, 3]) as randint:
        dice_cases = [
            ("固定骰子点数之和为 10", lambda: battle.roll_dice(3) == 10),
            ("每个骰子调用一次随机函数", lambda: randint.call_count == 3),
        ]
        dice_ok = expect_cases("roll_dice 使用指定数量的骰子", dice_cases)
if dice_ok:
    passed_checks += 1
total_checks += 1

invalid_dice = raises_value_error(lambda: battle.roll_dice(-1))
if print_check("roll_dice 拒绝负数骰子数量", invalid_dice):
    passed_checks += 1
total_checks += 1


action_cases = [
    ("长门生命值较低", lambda: battle.choose_nagato_action(29, 100) == "defend"),
    ("长门生命值边界", lambda: battle.choose_nagato_action(30, 19) == "special"),
    ("娜比娅生命值较低", lambda: battle.choose_nagato_action(80, 19) == "special"),
    ("普通回合", lambda: battle.choose_nagato_action(80, 80) == "attack"),
    ("长门生命值低时优先防御", lambda: battle.choose_nagato_action(29, 19) == "defend"),
]
if expect_cases("choose_nagato_action 处理边界数据", action_cases):
    passed_checks += 1
total_checks += 1


with patch.object(battle, "roll_dice", return_value=10) as roll:
    calculation_cases = [
        ("攻击函数调用 roll_dice", lambda: battle.calculate_attack_damage(3) == 10),
        ("防御函数调用 roll_dice", lambda: battle.calculate_defense_value(2) == 10),
        (
            "两个函数都传递了参数",
            lambda: roll.call_args_list[-2].args == (3,)
            and roll.call_args_list[-1].args == (2,),
        ),
    ]
    calculation_ok = expect_cases("攻击与防御数值计算", calculation_cases)
if calculation_ok:
    passed_checks += 1
total_checks += 1


critical_cases = [
    (
        "低于阈值一点",
        lambda: battle.check_critical_hit(battle.CRITICAL_HIT_THRESHOLD - 1)
        is False,
    ),
    (
        "正好达到阈值",
        lambda: battle.check_critical_hit(battle.CRITICAL_HIT_THRESHOLD) is True,
    ),
    ("远高于阈值", lambda: battle.check_critical_hit(100) is True),
]
if expect_cases("check_critical_hit 处理阈值数据", critical_cases):
    passed_checks += 1
total_checks += 1


ai_cases = [
    ("生命值为零", lambda: battle.nabiya_ai_action(0) == "defend"),
    ("正好达到防御阈值", lambda: battle.nabiya_ai_action(40) == "defend"),
    ("高于阈值一点", lambda: battle.nabiya_ai_action(41) == "attack"),
]
if expect_cases("nabiya_ai_action 处理生命值边界", ai_cases):
    passed_checks += 1
total_checks += 1


damage_cases = [
    ("普通攻击", lambda: battle.calculate_final_damage(20, 7) == 13),
    ("防御抵消全部伤害", lambda: battle.calculate_final_damage(7, 10) == 0),
    ("零伤害", lambda: battle.calculate_final_damage(0, 0) == 0),
    ("过量伤害将生命值归零", lambda: battle.apply_damage(10, 20) == 0),
    ("先计算防御再扣除生命值", lambda: battle.apply_damage(100, 20, 5) == 85),
    ("伤害不能变成治疗", lambda: battle.apply_damage(100, 5, 10) == 100),
]
if expect_cases("伤害函数处理代表性数据", damage_cases):
    passed_checks += 1
total_checks += 1

invalid_damage = [
    (
        "负数基础伤害",
        lambda: raises_value_error(
            lambda: battle.calculate_final_damage(-1, 0)
        ),
    ),
    (
        "负数防御值",
        lambda: raises_value_error(
            lambda: battle.calculate_final_damage(1, -1)
        ),
    ),
]
if expect_cases("伤害函数拒绝非法数据", invalid_damage):
    passed_checks += 1
total_checks += 1


state_cases = [
    ("双方存活", lambda: battle.is_battle_over(1, 1) is False),
    ("长门被击败", lambda: battle.is_battle_over(0, 1) is True),
    ("娜比娅被击败", lambda: battle.is_battle_over(1, 0) is True),
    ("长门胜利", lambda: battle.get_battle_result(1, 0) == "nagato"),
    ("娜比娅胜利", lambda: battle.get_battle_result(0, 1) == "nabiya"),
    ("同时被击败为平局", lambda: battle.get_battle_result(0, 0) == "draw"),
]
if expect_cases("战斗状态函数", state_cases):
    passed_checks += 1
total_checks += 1


main_ok = False
main_error = None
try:
    if random_module is None:
        raise AttributeError("longmen_vs_nabiya.py 没有导入 random")
    with patch.object(random_module, "randint", return_value=6), patch.object(
        random_module, "random", return_value=0.0
    ):
        output = io.StringIO()
        with redirect_stdout(output):
            result = battle.main_battle_loop(max_turns=10)
    main_ok = True
except Exception as error:
    main_error = error

if not main_ok:
    print_info(f"main_battle_loop：出现 {type(main_error).__name__}：{main_error}")
    result = None
    output = io.StringIO()
main_cases = [
    ("确定性战斗可以产生胜者", lambda: result == "nagato"),
    ("战斗输出包含回合信息", lambda: "第 1 回合" in output.getvalue()),
    ("战斗输出不包含错误回溯", lambda: "Traceback" not in output.getvalue()),
]
if expect_cases("main_battle_loop 可以确定性结束", main_cases):
    passed_checks += 1
total_checks += 1


print("\n--- 检查结束 ---")
print(f"通过：{passed_checks} / {total_checks}")
if passed_checks != total_checks:
    sys.exit(1)
print("全部检查通过。")

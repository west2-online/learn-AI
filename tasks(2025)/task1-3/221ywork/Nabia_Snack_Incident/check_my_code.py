# check_my_code.py
# 每当你完成 longmen_vs_nabiya.py 里的一个函数，就运行我来检查一下吧！

import sys

def print_check(name, success):
    status = "✅ 通过" if success else "❌ 失败"
    print(f"[{status}] {name}")
    return success

def print_info(message): print(f"    ➡️  {message}")
def print_skip(name): print(f"[...跳过] {name} (函数尚未完成或存在语法错误)")

print("--- 代码检查程序 启动！---\n")

try:
    from longmen_vs_nabiya import (
        display_status, roll_dice, choose_nagato_action,
        calculate_attack_damage, calculate_defense_value,
        check_critical_hit, nabiya_ai_action, main_battle_loop
    )
except (ImportError, SyntaxError) as e:
    print("❌ 严重错误：无法导入 longmen_vs_nabiya.py！")
    print_info(f"这通常意味着你的代码里有语法错误。请检查一下。错误提示: {e}")
    sys.exit()

passed_checks = 0

# --- 任务一 ---
try:
    print("--- 正在测试 任务一：display_status ---")
    print_info("请人工检查下面的输出是否为：【长门】HP: 100 / 120")
    display_status("长门", 100, 120)
    if print_check("display_status 的基本调用", True): passed_checks += 1
except Exception: print_skip("display_status")

# --- 任务二 ---
try:
    print("\n--- 正在测试 任务二：roll_dice ---")
    result = roll_dice(3)
    success = (3 <= result <= 18) and isinstance(result, int)
    if print_check("roll_dice(3) 的返回值在3-18之间", success): passed_checks += 1
    else: print_info("提示：请检查while循环次数是否正确，以及是否返回了整数总和。")
except Exception: print_skip("roll_dice")

# --- 任务三 ---
try:
    print("\n--- 正在测试 任务三：choose_nagato_action ---")
    s1 = print_check("长门HP<30时('defend')", choose_nagato_action(29, 100) == 'defend')
    s2 = print_check("娜比娅HP<20时('special')", choose_nagato_action(50, 19) == 'special')
    s3 = print_check("一般情况('attack')", choose_nagato_action(80, 80) == 'attack')
    if s1 and s2 and s3: passed_checks += 1
except Exception: print_skip("choose_nagato_action")

# --- 任务四 & 五 ---
try:
    print("\n--- 正在测试 任务四&五：计算函数 ---")
    s4 = print_check("calculate_attack_damage(4) 能返回整数", isinstance(calculate_attack_damage(4), int))
    s5 = print_check("calculate_defense_value(3) 能返回整数", isinstance(calculate_defense_value(3), int))
    if s4 and s5: passed_checks += 1
except Exception: print_skip("计算函数")

# --- 任务六 ---
try:
    print("\n--- 正在测试 任务六：check_critical_hit ---")
    s6_1 = print_check("伤害为18时暴击(True)", check_critical_hit(18) is True)
    s6_2 = print_check("伤害为17时不暴击(False)", check_critical_hit(17) is False)
    if s6_1 and s6_2: passed_checks += 1
except Exception: print_skip("check_critical_hit")

# --- 任务七 ---
try:
    print("\n--- 正在测试 任务七：nabiya_ai_action ---")
    s7_1 = print_check("娜比娅HP为40时('defend')", nabiya_ai_action(40) == 'defend')
    s7_2 = print_check("娜比娅HP为41时('attack')", nabiya_ai_action(41) == 'attack')
    if s7_1 and s7_2: passed_checks += 1
except Exception: print_skip("nabiya_ai_action")

# --- 总结 ---
print("\n--- 检查完毕 ---")
total_checks = 6 # 基础函数共6组测试
print(f"基础函数检查结果：{passed_checks} / {total_checks} 项通过。")
if passed_checks == total_checks:
    print("\n🎉 恭喜！所有基础函数都通过了！现在去挑战最后的 main_battle_loop 吧！")
    print("完成后，请直接运行 start_the_battle.py 来进行最终的实战检验！")
else:
    print("\n看起来还有一些函数需要修正哦。根据上面的提示修改，然后再次运行我吧！")

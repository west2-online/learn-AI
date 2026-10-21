"""运行娜比娅偷吃事件的完整战斗。"""

from longmen_vs_nabiya import main_battle_loop

if __name__ == "__main__":
    print("「嗯？有塞壬的气息……就在前方！」\n")
    try:
        # 传入暂停时间，让终端输出更像一场正在进行的战斗。
        result = main_battle_loop(pause_seconds=0.2)
        if result == "nagato":
            print("\n「哼，知道余的厉害就好！港区的和平，由余来守护！」")
        elif result == "nabiya":
            print("\n「这次先放过你，娜比娅！」")
        elif result == "draw":
            print("\n战斗暂时没有分出胜负，请检查回合上限和战斗逻辑。")
        else:
            print("\n主函数尚未完成，请先补全 longmen_vs_nabiya.py。")
    except (TypeError, ValueError) as error:
        print("\n程序遇到输入或参数问题。")
        print(f"错误信息：{error}")
        print("请检查 longmen_vs_nabiya.py 中的函数参数和数值处理。")
    except Exception as error:  # noqa: BLE001
        print("\n程序运行时遇到未处理的问题。")
        print(f"错误信息：{error}")
        print("请检查 longmen_vs_nabiya.py 中的战斗循环逻辑。")

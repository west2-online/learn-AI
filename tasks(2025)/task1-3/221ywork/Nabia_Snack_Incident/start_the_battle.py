# start_the_battle.py
# 完成所有代码后，运行此文件，观看长门与娜比亚的对决！

import sys
from longmen_vs_nabiya import main_battle_loop

if __name__ == "__main__":
    print("「嗯？有塞壬的气息…就在前方！」\n")
    try:
        # 调用学生需要实现的主函数
        main_battle_loop()
        print("\n「哼，知道余的厉害就好！港区的和平，由余来守护！」")
    except Exception as e:
        # 如果学生的程序因为任何原因崩溃了，给出友好的提示
        print(f"\n程序出现了一点小问题... T_T")
        print(f"错误信息: {e}")
        print("请检查一下 longmen_vs_nabiya.py 里的代码逻辑是不是哪里写错啦~")

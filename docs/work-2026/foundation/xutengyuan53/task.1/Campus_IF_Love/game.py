# game.py
import sys
from manage import Character

class Game:
    def __init__(self) -> None:
        self.characters: dict[str, Character] = {
            "学姐": Character("学姐", "社团里的艺术少女"),
            "小白": Character("小白", "课堂上的元气同学"),
            "姐姐": Character("姐姐", "食堂里的温柔姐姐"),
            "None": Character("None", "无")
        }
        self.current_target: Character = self.characters["None"]

    def start(self) -> None:
        # （保留你原本的 print 语句）
        print("========== 游戏开始：校园 if·恋 ==========")
        # ... 省略中间的 print ...
        
        if not self.scene_senpai():
            if not self.scene_xiaobai():
                if not self.scene_jiejie():
                    print("\n唉！眼前三妹子都不要？死现充别玩 galgame")

    def scene_senpai(self) -> bool:
        # （保留原样，已经写好了）
        pass 

    def scene_xiaobai(self) -> bool:
        print("\n【场景二：小白】")
        print("你走进图书馆，发现小白正在奋笔疾书，却被一道算法题难住了。")
        print("小白：「呜呜...这题到底该怎么写呀？」")
        
        choice = input("1. 主动帮她解题\n2. 敷衍几句，转身离开\n请选择：")
        if choice == "1":
            print("\n你拉开椅子坐下，指着屏幕讲解了动态规划的核心思想。小白眼中闪烁着崇拜的光芒。你进入【小白线】！")
            self.current_target = self.characters["小白"]
            self.story_loop()
            return True
        else:
            print("你借口说还有事，头也不回地走了。")
            return False

    def scene_jiejie(self) -> bool:
        print("\n【场景三：姐姐】")
        print("你偶然在校外的咖啡店敲代码，一位看起来成熟知性的姐姐似乎对你感兴趣，缓缓朝你走了过来...")
        print("姐姐：「你的代码思路很有趣呢，能给我讲讲你的实现方法吗？」")
        
        choice = input("1. 缓缓低眉，毫不在意的开始解释\n2. 头也不抬，保持敲代码的状态\n请选择：")
        if choice == "1":
            print("\n你合上电脑，耐心又绅士地和她交流起来。姐姐被你的才华和温柔打动。你进入【姐姐线】！")
            self.current_target = self.characters["姐姐"]
            self.story_loop()
            return True
        else:
            print("你敲击键盘的速度更快了，姐姐觉得没趣便离开了。")
            return False

    def story_loop(self) -> None:
        while True:
            print("\n你要做什么？")
            print("1. 和她聊天")
            print("2. 送她礼物")
            print("3. 查看好感度")
            print("4. 离开 (退出游戏)")
            
            choice = input("请输入选项: ").strip()
            
            if choice == "1":
                self.current_target.talk()
            elif choice == "2":
                gift = input("你想送什么礼物？(鲜花/编程笔记/奶茶/奇怪的石头/精致的钢笔/可爱玩偶/夜宵外卖): ").strip()
                self.current_target.give_gift(gift)
            elif choice == "3":
                print(f"当前 {self.current_target.name} 的好感度为: {self.current_target.affinity}")
            elif choice == "4":
                print("你选择离开，游戏结束。")
                sys.exit(0)
            else:
                print("无效输入，请重新选择。")
                
            # 检查是否达到结局线
            if self.current_target == self.characters["None"] or self.current_target.check_ending():
                break

if __name__ == "__main__":
    # 实例化游戏并启动
    game = Game()
    game.start()
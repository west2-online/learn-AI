# manage.py
import random
from typing import List, Dict
from story import DIALOGUES, GIFT_EFFECTS

class Character:
    def __init__(self, name: str, role: str, affinity: int = 0) -> None:
        self.name: str = name
        self.role: str = role
        self.affinity: int = affinity

    def talk(self) -> None:
        print(f"\n你正在和{self.name}对话...")
        # 获取该角色的对话列表
        dialogues: List[Dict[str, str]] = DIALOGUES.get(self.name, [])
        if not dialogues:
            print("她似乎不想和你说话。")
            return
            
        # 随机挑一句对话
        current_dialogue = random.choice(dialogues)
        print(f"{self.name}：「{current_dialogue['text']}」")
        print(f"A: {current_dialogue['optionA']}")
        print(f"B: {current_dialogue['optionB']}")
        
        choice = input("请选择你的回答 (输入 A 或 B): ").strip().upper()
        
        if choice == "A":
            print(f"{self.name}对你的回答很满意。")
            self.change_affinity(5)
        elif choice == "B":
            print(f"{self.name}似乎有些无语...")
            self.change_affinity(-5)
        else:
            print("你没有说话。")

    def give_gift(self, gift: str) -> None:
        print(f"你送给{self.name}一份{gift}。")
        # 获取礼物对各个角色的好感度加成
        gift_effect: Dict[str, int] = GIFT_EFFECTS.get(gift, {})
        
        # 如果没有这个礼物，或者列表里没写该角色，就默认按 "default" 算
        value: int = gift_effect.get(self.name, gift_effect.get("default", 0))
        
        self.change_affinity(value)

    def change_affinity(self, value: int) -> None:
        self.affinity += value
        print(f"{self.name}的好感度变化 {value} -> 当前好感度: {self.affinity}")

    def check_ending(self) -> bool:
        if self.affinity >= 100:
            print(f"恭喜！你和 {self.name} 的故事进入了结局线！")
            return True
        return False
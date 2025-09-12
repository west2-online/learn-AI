#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
角色系统 - 管理游戏中的角色数据和好感度
Character System - Manage character data and affinity
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from config_loader import get_config_loader

@dataclass
class Character:
    """角色类"""
    name: str                          # 角色名称
    display_name: str                  # 显示名称
    role: str                         # 角色身份
    affinity: int = 0                 # 好感度
    personality_traits: Dict[str, int] = field(default_factory=dict)  # 性格特征
    relationship_stage: str = "stranger"  # 关系阶段
    met: bool = False                 # 是否已见面
    current_route: bool = False       # 是否为当前路线
    
    # 特殊标记
    flags: Dict[str, bool] = field(default_factory=dict)
    
    # 互动记录
    interactions: List[str] = field(default_factory=list)
    gifts_received: List[str] = field(default_factory=list)
    dialogues_seen: List[str] = field(default_factory=list)
    
    def add_affinity(self, amount: int, reason: str = ""):
        """增加好感度"""
        old_affinity = self.affinity
        self.affinity = max(0, min(100, self.affinity + amount))
        
        if reason:
            self.interactions.append(f"好感度{'+' if amount > 0 else ''}{amount}: {reason}")
        
        # 检查关系阶段变化
        self._update_relationship_stage()
        
        return self.affinity - old_affinity
    
    def _update_relationship_stage(self):
        """根据好感度更新关系阶段"""
        if self.affinity >= 85:
            self.relationship_stage = "romance"
        elif self.affinity >= 60:
            self.relationship_stage = "close_friend"
        elif self.affinity >= 30:
            self.relationship_stage = "friend"
        elif self.affinity >= 10:
            self.relationship_stage = "acquaintance"
        else:
            self.relationship_stage = "stranger"
    
    def add_personality_trait(self, trait: str, amount: int):
        """增加性格特征"""
        if trait not in self.personality_traits:
            self.personality_traits[trait] = 0
        self.personality_traits[trait] += amount
    
    def set_flag(self, flag_name: str, value: bool = True):
        """设置特殊标记"""
        self.flags[flag_name] = value
    
    def has_flag(self, flag_name: str) -> bool:
        """检查是否有特殊标记"""
        return self.flags.get(flag_name, False)
    
    def add_dialogue(self, dialogue_id: str):
        """记录已看过的对话"""
        if dialogue_id not in self.dialogues_seen:
            self.dialogues_seen.append(dialogue_id)
    
    def give_gift(self, gift_name: str) -> int:
        """给角色送礼物，返回好感度变化"""
        config_loader = get_config_loader()
        gift_effects = config_loader.get_gift_effects()
        
        if gift_name not in gift_effects:
            return 0
        
        gift_config = gift_effects[gift_name]
        
        # 计算好感度变化
        affinity_change = 0
        if self.name in gift_config:
            affinity_change = gift_config[self.name]
        elif "default" in gift_config:
            affinity_change = gift_config["default"]
        
        # 记录礼物
        self.gifts_received.append(gift_name)
        
        # 应用好感度变化
        actual_change = self.add_affinity(affinity_change, f"收到礼物: {gift_name}")
        
        return actual_change
    
    def get_status_summary(self) -> str:
        """获取角色状态摘要"""
        return f"{self.display_name} | 好感度: {self.affinity}/100 | 关系: {self.relationship_stage}"

class CharacterManager:
    """角色管理器"""
    
    def __init__(self):
        """初始化角色管理器"""
        self.characters: Dict[str, Character] = {}
        self.current_target: Optional[str] = None
        self._initialize_characters()
    
    def _initialize_characters(self):
        """初始化所有角色"""
        config_loader = get_config_loader()
        game_config = config_loader.get_game_config()
        heroines = game_config.get("heroines", {})
        
        for char_id, char_config in heroines.items():
            character = Character(
                name=char_id,
                display_name=char_config.get("default_name", char_config.get("name", char_id)),
                role=char_config.get("role", "未知"),
            )
            self.characters[char_id] = character
    
    def get_character(self, name: str) -> Optional[Character]:
        """获取角色"""
        return self.characters.get(name)
    
    def get_all_characters(self) -> Dict[str, Character]:
        """获取所有角色"""
        return self.characters.copy()
    
    def get_met_characters(self) -> Dict[str, Character]:
        """获取已见面的角色"""
        return {name: char for name, char in self.characters.items() if char.met}
    
    def set_current_target(self, character_name: str):
        """设置当前攻略目标"""
        # 重置所有角色的当前路线状态
        for char in self.characters.values():
            char.current_route = False
        
        # 设置新的攻略目标
        if character_name in self.characters:
            self.characters[character_name].current_route = True
            self.current_target = character_name
    
    def get_current_target(self) -> Optional[Character]:
        """获取当前攻略目标"""
        if self.current_target:
            return self.characters.get(self.current_target)
        return None
    
    def meet_character(self, character_name: str):
        """标记角色为已见面"""
        if character_name in self.characters:
            self.characters[character_name].met = True
    
    def add_affinity_to_current(self, amount: int, reason: str = "") -> int:
        """给当前攻略目标增加好感度"""
        current = self.get_current_target()
        if current:
            return current.add_affinity(amount, reason)
        return 0
    
    def give_gift_to_current(self, gift_name: str) -> tuple[int, str]:
        """给当前攻略目标送礼物"""
        current = self.get_current_target()
        if current:
            change = current.give_gift(gift_name)
            return change, current.display_name
        return 0, ""
    
    def check_ending_conditions(self, character_name: str) -> str:
        """检查角色的结局条件"""
        character = self.get_character(character_name)
        if not character:
            return "friend_ending"
        
        # 基于好感度和特殊标记判断结局类型
        if character.affinity >= 100:
            # 检查真结局的特殊条件
            if character_name == "senpai":
                if (character.has_flag("crisis_helped") and 
                    character.has_flag("collaboration_success")):
                    return "true_ending"
            elif character_name == "xiaobai":
                if (character.has_flag("crisis_helped") and 
                    character.has_flag("emotional_support") and
                    len([d for d in character.interactions if "教学" in d]) >= 8):
                    return "true_ending"
            elif character_name == "jiejie":
                if (character.has_flag("emotional_support_given") and 
                    character.has_flag("crisis_helped") and
                    character.has_flag("collaboration_success")):
                    return "true_ending"
            
            return "good_ending"
        elif character.affinity >= 80:
            return "good_ending"
        elif character.affinity >= 60:
            return "normal_ending"
        else:
            return "friend_ending"
    
    def get_affinity_display(self) -> str:
        """获取好感度显示信息"""
        lines = ["=== 角色好感度 ==="]
        for name, char in self.characters.items():
            if char.met:
                status = "💖" if char.current_route else "😊"
                lines.append(f"{status} {char.get_status_summary()}")
        return "\n".join(lines)
    
    def save_data(self) -> Dict[str, Any]:
        """保存角色数据"""
        data = {
            "current_target": self.current_target,
            "characters": {}
        }
        
        for name, char in self.characters.items():
            data["characters"][name] = {
                "name": char.name,
                "display_name": char.display_name,
                "role": char.role,
                "affinity": char.affinity,
                "personality_traits": char.personality_traits,
                "relationship_stage": char.relationship_stage,
                "met": char.met,
                "current_route": char.current_route,
                "flags": char.flags,
                "interactions": char.interactions,
                "gifts_received": char.gifts_received,
                "dialogues_seen": char.dialogues_seen
            }
        
        return data
    
    def load_data(self, data: Dict[str, Any]):
        """加载角色数据"""
        self.current_target = data.get("current_target")
        
        characters_data = data.get("characters", {})
        for name, char_data in characters_data.items():
            if name in self.characters:
                char = self.characters[name]
                char.affinity = char_data.get("affinity", 0)
                char.personality_traits = char_data.get("personality_traits", {})
                char.relationship_stage = char_data.get("relationship_stage", "stranger")
                char.met = char_data.get("met", False)
                char.current_route = char_data.get("current_route", False)
                char.flags = char_data.get("flags", {})
                char.interactions = char_data.get("interactions", [])
                char.gifts_received = char_data.get("gifts_received", [])
                char.dialogues_seen = char_data.get("dialogues_seen", [])

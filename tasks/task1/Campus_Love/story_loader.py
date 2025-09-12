#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
剧情加载器 - 负责加载和管理剧情帧数据
Story Loader - Load and manage story frame data
"""

from typing import Dict, Any, List, Optional
from config_loader import get_config_loader

class StoryFrame:
    """剧情帧类"""
    
    def __init__(self, frame_id: str, frame_data: Dict[str, Any]):
        """
        初始化剧情帧
        
        Args:
            frame_id: 剧情帧ID
            frame_data: 剧情帧数据
        """
        self.frame_id = frame_id
        self.type = frame_data.get("type", "narrative")
        self.category = frame_data.get("category", "unknown")
        self.title = frame_data.get("title", "")
        self.scene = frame_data.get("scene", "")
        self.content = frame_data.get("content", "")
        
        # 选择相关
        self.choices = frame_data.get("choices", {})
        
        # 对话相关
        self.speaker = frame_data.get("speaker", "")
        self.dialogue_options = frame_data.get("dialogue_options", {})
        
        # 条件和效果
        self.unlock_condition = frame_data.get("unlock_condition", "")
        self.effects = frame_data.get("effects", {})
        
        # 转场
        self.transitions = frame_data.get("transitions", {})
        
        # 音效和视觉效果
        self.audio = frame_data.get("audio", {})
        self.images = frame_data.get("images", {})
        
        # 角色相关
        self.character_stats = frame_data.get("character_stats", {})
        self.character_development = frame_data.get("character_development", {})
        
        # 结局相关
        self.ending_description = frame_data.get("ending_description", "")
        self.unlock_content = frame_data.get("unlock_content", [])
    
    def get_next_frame(self, choice: str = "") -> Optional[str]:
        """
        获取下一个剧情帧ID
        
        Args:
            choice: 用户选择
            
        Returns:
            下一个剧情帧ID
        """
        # 如果有选择，根据选择决定下一帧
        if choice and self.choices:
            choice_key = f"choice_{choice.lower()}"
            if choice_key in self.choices:
                return self.choices[choice_key].get("next_frame")
        
        # 如果有对话选项，根据选择决定下一帧
        if choice and self.dialogue_options:
            option_key = f"option_{choice.lower()}"
            if option_key in self.dialogue_options:
                return self.dialogue_options[option_key].get("next_frame")
        
        # 默认转场
        return self.transitions.get("next")
    
    def get_choice_effect(self, choice: str) -> Dict[str, Any]:
        """
        获取选择的效果
        
        Args:
            choice: 用户选择
            
        Returns:
            选择效果
        """
        if self.choices:
            choice_key = f"choice_{choice.lower()}"
            if choice_key in self.choices:
                return self.choices[choice_key].get("effect", {})
        
        if self.dialogue_options:
            option_key = f"option_{choice.lower()}"
            if option_key in self.dialogue_options:
                return self.dialogue_options[option_key]
        
        return {}
    
    def has_choices(self) -> bool:
        """检查是否有选择项"""
        return bool(self.choices or self.dialogue_options)
    
    def get_choice_list(self) -> List[Dict[str, Any]]:
        """获取选择列表"""
        choices = []
        
        if self.choices:
            for key, choice_data in self.choices.items():
                if key.startswith("choice_"):
                    choice_letter = key.split("_")[1].upper()
                    choices.append({
                        "key": choice_letter,
                        "text": choice_data.get("text", ""),
                        "description": choice_data.get("description", "")
                    })
        
        if self.dialogue_options:
            for key, option_data in self.dialogue_options.items():
                if key.startswith("option_"):
                    option_letter = key.split("_")[1].upper()
                    choices.append({
                        "key": option_letter,
                        "text": option_data.get("text", ""),
                        "affinity": option_data.get("affinity", "")
                    })
        
        return choices

class StoryLoader:
    """剧情加载器"""
    
    def __init__(self):
        """初始化剧情加载器"""
        self.config_loader = get_config_loader()
        self._story_cache = {}
        self._load_all_stories()
    
    def _load_all_stories(self):
        """加载所有剧情数据"""
        # 加载序章
        prologue_data = self.config_loader.get_prologue_frames()
        if "prologue" in prologue_data:
            for frame_id, frame_data in prologue_data["prologue"].items():
                self._story_cache[frame_id] = StoryFrame(frame_id, frame_data)
        
        # 加载学姐路线
        senpai_data = self.config_loader.get_senpai_route_frames()
        if "senpai_route" in senpai_data:
            for frame_id, frame_data in senpai_data["senpai_route"].items():
                self._story_cache[frame_id] = StoryFrame(frame_id, frame_data)
        
        # 加载小白路线
        xiaobai_data = self.config_loader.get_xiaobai_route_frames()
        if "xiaobai_route" in xiaobai_data:
            for frame_id, frame_data in xiaobai_data["xiaobai_route"].items():
                self._story_cache[frame_id] = StoryFrame(frame_id, frame_data)
        
        # 加载姐姐路线
        jiejie_data = self.config_loader.get_jiejie_route_frames()
        if "jiejie_route" in jiejie_data:
            for frame_id, frame_data in jiejie_data["jiejie_route"].items():
                self._story_cache[frame_id] = StoryFrame(frame_id, frame_data)
        
        # 加载结局
        ending_data = self.config_loader.get_ending_frames()
        if "endings" in ending_data:
            for route_name, route_endings in ending_data["endings"].items():
                for ending_type, ending_frames in route_endings.items():
                    for frame_id, frame_data in ending_frames.items():
                        full_frame_id = f"{route_name}_{ending_type}_{frame_id}"
                        self._story_cache[full_frame_id] = StoryFrame(full_frame_id, frame_data)
    
    def get_frame(self, frame_id: str) -> Optional[StoryFrame]:
        """
        获取指定的剧情帧
        
        Args:
            frame_id: 剧情帧ID
            
        Returns:
            剧情帧对象
        """
        return self._story_cache.get(frame_id)
    
    def get_dialogue(self, character_name: str, dialogue_id: str) -> Optional[Dict[str, Any]]:
        """
        获取指定角色的对话
        
        Args:
            character_name: 角色名称
            dialogue_id: 对话ID
            
        Returns:
            对话数据
        """
        dialogue_system = self.config_loader.get_dialogue_system()
        dialogue_data = dialogue_system.get("dialogue_system", {})
        
        character_dialogues = dialogue_data.get(f"{character_name}_dialogues", {})
        
        # 在各个阶段中查找对话
        for stage_name, stage_dialogues in character_dialogues.items():
            if dialogue_id in stage_dialogues:
                return stage_dialogues[dialogue_id]
        
        return None
    
    def get_random_dialogue(self, character_name: str, stage: str = "development") -> Optional[Dict[str, Any]]:
        """
        获取指定角色和阶段的随机对话
        
        Args:
            character_name: 角色名称
            stage: 剧情阶段
            
        Returns:
            对话数据
        """
        dialogue_system = self.config_loader.get_dialogue_system()
        dialogue_data = dialogue_system.get("dialogue_system", {})
        
        character_dialogues = dialogue_data.get(f"{character_name}_dialogues", {})
        stage_dialogues = character_dialogues.get(stage, {})
        
        if stage_dialogues:
            import random
            dialogue_id = random.choice(list(stage_dialogues.keys()))
            return stage_dialogues[dialogue_id]
        
        return None
    
    def check_frame_condition(self, frame: StoryFrame, game_state: Dict[str, Any]) -> bool:
        """
        检查剧情帧的解锁条件
        
        Args:
            frame: 剧情帧
            game_state: 游戏状态
            
        Returns:
            是否满足条件
        """
        if not frame.unlock_condition:
            return True
        
        condition = frame.unlock_condition
        
        # 简单的条件解析（可以扩展为更复杂的表达式解析）
        try:
            # 获取角色数据
            characters = game_state.get("characters", {})
            flags = game_state.get("flags", {})
            
            # 替换条件中的变量
            for char_name, char_data in characters.items():
                condition = condition.replace(f"{char_name}_affinity", str(char_data.get("affinity", 0)))
            
            for flag_name, flag_value in flags.items():
                condition = condition.replace(flag_name, str(flag_value).lower())
            
            # 安全的条件评估
            condition = condition.replace("AND", "and").replace("OR", "or")
            return eval(condition)
            
        except:
            return True  # 如果条件解析失败，默认允许访问
    
    def get_available_frames(self, game_state: Dict[str, Any]) -> List[str]:
        """
        获取当前可用的剧情帧列表
        
        Args:
            game_state: 游戏状态
            
        Returns:
            可用的剧情帧ID列表
        """
        available_frames = []
        
        for frame_id, frame in self._story_cache.items():
            if self.check_frame_condition(frame, game_state):
                available_frames.append(frame_id)
        
        return available_frames
    
    def get_ending_frame(self, character_name: str, ending_type: str) -> Optional[StoryFrame]:
        """
        获取指定角色和类型的结局帧
        
        Args:
            character_name: 角色名称 (senpai/xiaobai/jiejie)
            ending_type: 结局类型 (true_ending/good_ending/normal_ending/friend_ending)
            
        Returns:
            结局帧对象
        """
        # 构造结局帧ID
        if character_name in ["senpai", "xiaobai", "jiejie"]:
            frame_id = f"{character_name}_endings_{ending_type}_frame_001"
        else:
            frame_id = f"special_endings_{ending_type}_frame_001"
        
        return self.get_frame(frame_id)
    
    def reload_stories(self):
        """重新加载所有剧情数据"""
        self._story_cache.clear()
        self.config_loader.clear_cache()
        self._load_all_stories()
    
    def get_story_progress(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        获取剧情进度信息
        
        Args:
            game_state: 游戏状态
            
        Returns:
            进度信息
        """
        completed_frames = game_state.get("completed_frames", set())
        total_frames = len(self._story_cache)
        completion_rate = len(completed_frames) / total_frames if total_frames > 0 else 0
        
        return {
            "completed_frames": len(completed_frames),
            "total_frames": total_frames,
            "completion_rate": completion_rate,
            "current_frame": game_state.get("current_frame", "")
        }

# 全局剧情加载器实例
story_loader = StoryLoader()

def get_story_loader() -> StoryLoader:
    """获取全局剧情加载器实例"""
    return story_loader

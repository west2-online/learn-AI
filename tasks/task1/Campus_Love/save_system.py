#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
存档系统 - 管理游戏存档、读档和即时存档
Save System - Manage game save, load and quicksave
"""

import json
import os
import time
from datetime import datetime
from typing import Dict, Any, List, Optional
from dataclasses import asdict

class SaveSystem:
    """存档系统"""
    
    def __init__(self, save_dir: str = "saves"):
        """
        初始化存档系统
        
        Args:
            save_dir: 存档目录
        """
        self.save_dir = save_dir
        self.quicksave_file = "quicksave.json"
        self.autosave_file = "autosave.json"
        
        # 确保存档目录存在
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
    
    def create_save_data(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        创建存档数据
        
        Args:
            game_state: 游戏状态
            
        Returns:
            存档数据
        """
        save_data = {
            "version": "1.0.0",
            "timestamp": datetime.now().isoformat(),
            "playtime": game_state.get("playtime", 0),
            "current_frame": game_state.get("current_frame", ""),
            "game_progress": game_state.get("game_progress", {}),
            "character_data": game_state.get("character_data", {}),
            "player_data": game_state.get("player_data", {}),
            "flags": game_state.get("flags", {}),
            "story_progress": game_state.get("story_progress", {}),
            "statistics": game_state.get("statistics", {})
        }
        return save_data
    
    def save_game(self, game_state: Dict[str, Any], save_name: str) -> bool:
        """
        保存游戏
        
        Args:
            game_state: 游戏状态
            save_name: 存档名称
            
        Returns:
            是否保存成功
        """
        try:
            save_data = self.create_save_data(game_state)
            save_path = os.path.join(self.save_dir, f"{save_name}.json")
            
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            
            print(f"游戏已保存到: {save_name}")
            return True
            
        except Exception as e:
            print(f"保存失败: {e}")
            return False
    
    def load_game(self, save_name: str) -> Optional[Dict[str, Any]]:
        """
        加载游戏
        
        Args:
            save_name: 存档名称
            
        Returns:
            游戏状态数据，如果加载失败返回None
        """
        try:
            save_path = os.path.join(self.save_dir, f"{save_name}.json")
            
            if not os.path.exists(save_path):
                print(f"存档文件不存在: {save_name}")
                return None
            
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            print(f"游戏已从存档加载: {save_name}")
            return save_data
            
        except Exception as e:
            print(f"加载失败: {e}")
            return None
    
    def quicksave(self, game_state: Dict[str, Any]) -> bool:
        """
        快速保存
        
        Args:
            game_state: 游戏状态
            
        Returns:
            是否保存成功
        """
        try:
            save_data = self.create_save_data(game_state)
            save_path = os.path.join(self.save_dir, self.quicksave_file)
            
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            
            print("快速保存完成")
            return True
            
        except Exception as e:
            print(f"快速保存失败: {e}")
            return False
    
    def quickload(self) -> Optional[Dict[str, Any]]:
        """
        快速加载
        
        Returns:
            游戏状态数据，如果加载失败返回None
        """
        try:
            save_path = os.path.join(self.save_dir, self.quicksave_file)
            
            if not os.path.exists(save_path):
                print("快速存档不存在")
                return None
            
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            print("快速加载完成")
            return save_data
            
        except Exception as e:
            print(f"快速加载失败: {e}")
            return None
    
    def autosave(self, game_state: Dict[str, Any]) -> bool:
        """
        自动保存
        
        Args:
            game_state: 游戏状态
            
        Returns:
            是否保存成功
        """
        try:
            save_data = self.create_save_data(game_state)
            save_path = os.path.join(self.save_dir, self.autosave_file)
            
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            
            print("自动保存完成")
            return True
            
        except Exception as e:
            print(f"自动保存失败: {e}")
            return False
    
    def get_save_list(self) -> List[Dict[str, Any]]:
        """
        获取存档列表
        
        Returns:
            存档信息列表
        """
        save_list = []
        
        if not os.path.exists(self.save_dir):
            return save_list
        
        for filename in os.listdir(self.save_dir):
            if filename.endswith('.json') and filename not in [self.quicksave_file, self.autosave_file]:
                try:
                    save_path = os.path.join(self.save_dir, filename)
                    with open(save_path, 'r', encoding='utf-8') as f:
                        save_data = json.load(f)
                    
                    save_info = {
                        "filename": filename[:-5],  # 去掉.json扩展名
                        "timestamp": save_data.get("timestamp", "未知时间"),
                        "playtime": save_data.get("playtime", 0),
                        "current_frame": save_data.get("current_frame", "未知位置"),
                        "file_size": os.path.getsize(save_path)
                    }
                    save_list.append(save_info)
                    
                except Exception as e:
                    print(f"读取存档信息失败 {filename}: {e}")
                    continue
        
        # 按时间戳排序
        save_list.sort(key=lambda x: x["timestamp"], reverse=True)
        return save_list
    
    def delete_save(self, save_name: str) -> bool:
        """
        删除存档
        
        Args:
            save_name: 存档名称
            
        Returns:
            是否删除成功
        """
        try:
            save_path = os.path.join(self.save_dir, f"{save_name}.json")
            
            if os.path.exists(save_path):
                os.remove(save_path)
                print(f"存档已删除: {save_name}")
                return True
            else:
                print(f"存档不存在: {save_name}")
                return False
                
        except Exception as e:
            print(f"删除存档失败: {e}")
            return False
    
    def has_quicksave(self) -> bool:
        """检查是否有快速存档"""
        save_path = os.path.join(self.save_dir, self.quicksave_file)
        return os.path.exists(save_path)
    
    def has_autosave(self) -> bool:
        """检查是否有自动存档"""
        save_path = os.path.join(self.save_dir, self.autosave_file)
        return os.path.exists(save_path)
    
    def get_save_info(self, save_name: str) -> Optional[Dict[str, Any]]:
        """
        获取指定存档的详细信息
        
        Args:
            save_name: 存档名称
            
        Returns:
            存档详细信息
        """
        try:
            save_path = os.path.join(self.save_dir, f"{save_name}.json")
            
            if not os.path.exists(save_path):
                return None
            
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            # 格式化时间显示
            timestamp = save_data.get("timestamp", "")
            try:
                dt = datetime.fromisoformat(timestamp)
                formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
            except:
                formatted_time = timestamp
            
            # 格式化游戏时长
            playtime = save_data.get("playtime", 0)
            hours = playtime // 3600
            minutes = (playtime % 3600) // 60
            seconds = playtime % 60
            
            return {
                "save_name": save_name,
                "save_time": formatted_time,
                "playtime": f"{hours:02d}:{minutes:02d}:{seconds:02d}",
                "current_frame": save_data.get("current_frame", "未知位置"),
                "version": save_data.get("version", "未知版本"),
                "file_size": os.path.getsize(save_path)
            }
            
        except Exception as e:
            print(f"获取存档信息失败: {e}")
            return None
    
    def cleanup_old_saves(self, max_saves: int = 10):
        """
        清理旧存档，保留最新的指定数量
        
        Args:
            max_saves: 最大保留存档数量
        """
        save_list = self.get_save_list()
        
        if len(save_list) > max_saves:
            # 删除最旧的存档
            for save_info in save_list[max_saves:]:
                self.delete_save(save_info["filename"])
            
            print(f"已清理 {len(save_list) - max_saves} 个旧存档")

class GameProgress:
    """游戏进度跟踪"""
    
    def __init__(self):
        """初始化游戏进度"""
        self.start_time = time.time()
        self.playtime = 0
        self.current_frame = ""
        self.completed_frames = set()
        self.unlocked_endings = set()
        self.statistics = {
            "choices_made": 0,
            "dialogues_seen": 0,
            "gifts_given": 0,
            "saves_made": 0,
            "loads_made": 0
        }
    
    def update_playtime(self):
        """更新游戏时长"""
        current_time = time.time()
        self.playtime = int(current_time - self.start_time)
    
    def set_current_frame(self, frame_id: str):
        """设置当前剧情帧"""
        self.current_frame = frame_id
        self.completed_frames.add(frame_id)
    
    def unlock_ending(self, ending_id: str):
        """解锁结局"""
        self.unlocked_endings.add(ending_id)
    
    def add_statistic(self, stat_name: str, amount: int = 1):
        """添加统计数据"""
        if stat_name in self.statistics:
            self.statistics[stat_name] += amount
    
    def get_progress_data(self) -> Dict[str, Any]:
        """获取进度数据"""
        self.update_playtime()
        return {
            "playtime": self.playtime,
            "current_frame": self.current_frame,
            "completed_frames": list(self.completed_frames),
            "unlocked_endings": list(self.unlocked_endings),
            "statistics": self.statistics.copy()
        }
    
    def load_progress_data(self, data: Dict[str, Any]):
        """加载进度数据"""
        self.playtime = data.get("playtime", 0)
        self.current_frame = data.get("current_frame", "")
        self.completed_frames = set(data.get("completed_frames", []))
        self.unlocked_endings = set(data.get("unlocked_endings", []))
        self.statistics = data.get("statistics", {
            "choices_made": 0,
            "dialogues_seen": 0,
            "gifts_given": 0,
            "saves_made": 0,
            "loads_made": 0
        })
        
        # 重新设置开始时间
        self.start_time = time.time() - self.playtime

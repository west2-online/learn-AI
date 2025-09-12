#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置加载器 - 负责加载YAML配置文件
Configuration Loader - Load YAML configuration files
"""

import yaml
import os
from typing import Dict, Any, Optional

class ConfigLoader:
    """配置文件加载器"""
    
    def __init__(self, config_dir: str = "."):
        """
        初始化配置加载器
        
        Args:
            config_dir: 配置文件目录
        """
        self.config_dir = config_dir
        self._cache = {}  # 配置缓存
        
    def load_config(self, filename: str) -> Dict[str, Any]:
        """
        加载YAML配置文件
        
        Args:
            filename: 配置文件名
            
        Returns:
            配置数据字典
        """
        if filename in self._cache:
            return self._cache[filename]
            
        file_path = os.path.join(self.config_dir, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                config = yaml.safe_load(file)
                self._cache[filename] = config
                return config
        except FileNotFoundError:
            print(f"配置文件未找到: {file_path}")
            return {}
        except yaml.YAMLError as e:
            print(f"YAML解析错误: {e}")
            return {}
    
    def get_game_config(self) -> Dict[str, Any]:
        """获取游戏主配置"""
        return self.load_config("game_config.yaml")
    
    def get_prologue_frames(self) -> Dict[str, Any]:
        """获取序章剧情帧"""
        return self.load_config("prologue_frames.yaml")
    
    def get_senpai_route_frames(self) -> Dict[str, Any]:
        """获取学姐路线剧情帧"""
        return self.load_config("senpai_route_frames.yaml")
    
    def get_xiaobai_route_frames(self) -> Dict[str, Any]:
        """获取小白路线剧情帧"""
        return self.load_config("xiaobai_route_frames.yaml")
    
    def get_jiejie_route_frames(self) -> Dict[str, Any]:
        """获取姐姐路线剧情帧"""
        return self.load_config("jiejie_route_frames.yaml")
    
    def get_dialogue_system(self) -> Dict[str, Any]:
        """获取对话系统配置"""
        return self.load_config("dialogue_system.yaml")
    
    def get_ending_frames(self) -> Dict[str, Any]:
        """获取结局剧情帧"""
        return self.load_config("ending_frames.yaml")
    
    def get_character_config(self, character_name: str) -> Optional[Dict[str, Any]]:
        """
        获取指定角色的配置
        
        Args:
            character_name: 角色名称 (senpai/xiaobai/jiejie)
            
        Returns:
            角色配置数据
        """
        game_config = self.get_game_config()
        heroines = game_config.get("heroines", {})
        return heroines.get(character_name)
    
    def get_gift_effects(self) -> Dict[str, Any]:
        """获取礼物效果配置"""
        game_config = self.get_game_config()
        return game_config.get("game_systems", {}).get("gift_system", {}).get("gifts", {})
    
    def get_affinity_config(self) -> Dict[str, Any]:
        """获取好感度系统配置"""
        game_config = self.get_game_config()
        return game_config.get("game_systems", {}).get("affinity_system", {})
    
    def reload_config(self, filename: str) -> Dict[str, Any]:
        """
        重新加载配置文件（清除缓存）
        
        Args:
            filename: 配置文件名
            
        Returns:
            重新加载的配置数据
        """
        if filename in self._cache:
            del self._cache[filename]
        return self.load_config(filename)
    
    def clear_cache(self):
        """清除所有配置缓存"""
        self._cache.clear()

# 全局配置加载器实例
config_loader = ConfigLoader()

def get_config_loader() -> ConfigLoader:
    """获取全局配置加载器实例"""
    return config_loader

def set_config_dir(config_dir: str):
    """设置配置文件目录"""
    global config_loader
    config_loader = ConfigLoader(config_dir)

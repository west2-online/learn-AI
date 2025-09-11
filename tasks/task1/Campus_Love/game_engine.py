#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
游戏引擎核心 - 管理游戏主要逻辑和状态
Game Engine Core - Manage main game logic and state
"""

import time
import random
from typing import Dict, Any, Optional, List
from character_system import CharacterManager
from story_loader import get_story_loader, StoryFrame
from save_system import SaveSystem, GameProgress
from ui_system import get_ui
from config_loader import get_config_loader

class GameEngine:
    """游戏引擎"""
    
    def __init__(self):
        """初始化游戏引擎"""
        self.ui = get_ui()
        self.story_loader = get_story_loader()
        self.character_manager = CharacterManager()
        self.save_system = SaveSystem()
        self.progress = GameProgress()
        self.config_loader = get_config_loader()
        
        # 游戏状态
        self.current_frame_id = "frame_001"  # 从序章开始
        self.game_flags = {}
        self.player_data = {
            "name": "主角",
            "attributes": {
                "intelligence": 95,
                "appearance": 90,
                "programming": 100,
                "social": 70,
                "art": 60
            },
            "personality": {}
        }
        
        # 游戏运行状态
        self.running = True
        self.in_menu = False
        
    def start_game(self):
        """开始游戏"""
        self.ui.clear_screen()
        self.show_game_intro()
        
        # 主游戏循环
        while self.running:
            try:
                if self.in_menu:
                    self.handle_menu()
                else:
                    self.handle_story_frame()
                    
            except KeyboardInterrupt:
                self.quit_game()
            except Exception as e:
                self.ui.print_error(f"游戏出错: {e}")
                self.ui.wait_for_input()
    
    def show_game_intro(self):
        """显示游戏开场"""
        game_config = self.config_loader.get_game_config()
        game_info = game_config.get("game_info", {})
        
        self.ui.print_title(game_info.get("title", "校园恋爱物语"))
        self.ui.print_subtitle(game_info.get("subtitle", "如果在校园里遇见你"))
        
        print()
        print("  " + game_info.get("description", "一个关于校园生活与青春爱恋的互动故事"))
        print()
        
        # 显示游戏控制说明
        self.show_controls()
        
        self.ui.wait_for_input("按回车键开始游戏...")
    
    def show_controls(self):
        """显示游戏控制说明"""
        controls = [
            "🎮 游戏控制说明:",
            "",
            "  1, 2, 3, 4 - 选择选项",
            "  Q - 快速存档",
            "  L - 快速读档", 
            "  S - 存档菜单",
            "  R - 读档菜单",
            "  A - 查看好感度",
            "  M - 主菜单",
            "  H - 帮助",
            "  ESC - 退出游戏",
            ""
        ]
        
        for line in controls:
            print(line)
    
    def handle_story_frame(self):
        """处理剧情帧"""
        current_frame = self.story_loader.get_frame(self.current_frame_id)
        
        if not current_frame:
            self.ui.print_error(f"找不到剧情帧: {self.current_frame_id}")
            self.in_menu = True
            return
        
        # 检查解锁条件
        game_state = self.get_game_state()
        if not self.story_loader.check_frame_condition(current_frame, game_state):
            self.ui.print_error("不满足剧情条件")
            self.in_menu = True
            return
        
        # 更新进度
        self.progress.set_current_frame(self.current_frame_id)
        
        # 显示剧情内容
        self.display_frame(current_frame)
        
        # 处理用户输入
        self.handle_frame_input(current_frame)
    
    def display_frame(self, frame: StoryFrame):
        """显示剧情帧内容"""
        # 显示剧情内容
        self.ui.print_story_frame(frame.content, frame.title, frame.scene)
        
        # 处理角色发展
        if frame.character_development:
            self.apply_character_development(frame.character_development)
        
        # 应用角色状态变化
        if frame.character_stats:
            self.apply_character_stats(frame.character_stats)
        
        # 如果是对话类型，显示对话选项
        if frame.type == "dialogue" and frame.has_choices():
            choices = frame.get_choice_list()
            self.display_choices(choices)
        elif frame.has_choices():
            choices = frame.get_choice_list()
            self.display_choices(choices)
    
    def display_choices(self, choices: List[Dict[str, Any]]):
        """显示选择项"""
        if not choices:
            return
        
        print("🤔 请选择你的行动:")
        print()
        
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice['text']}")
            if choice.get('description'):
                print(f"     {choice['description']}")
            print()
        
        print("  其他操作:")
        print("  Q - 快速存档  L - 快速读档  A - 查看好感度  M - 主菜单")
        print()
    
    def handle_frame_input(self, frame: StoryFrame):
        """处理剧情帧输入"""
        if frame.has_choices():
            # 有选择的剧情帧
            choices = frame.get_choice_list()
            valid_choices = [str(i) for i in range(1, len(choices) + 1)]
            valid_choices.extend(['q', 'l', 'a', 'm', 's', 'r', 'h'])
            
            while True:
                choice = self.ui.get_choice("请输入选择", valid_choices).lower()
                
                if choice in ['q', 'l', 'a', 'm', 's', 'r', 'h']:
                    if self.handle_special_command(choice):
                        return
                    continue
                
                # 处理选择
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(choices):
                    selected_choice = choices[choice_index]
                    choice_key = selected_choice['key']
                    
                    # 应用选择效果
                    self.apply_choice_effect(frame, choice_key)
                    
                    # 更新统计
                    self.progress.add_statistic("choices_made")
                    
                    # 转到下一帧
                    next_frame = frame.get_next_frame(choice_key)
                    if next_frame:
                        self.current_frame_id = next_frame
                    else:
                        print(f"警告：找不到选择 {choice_key} 对应的下一帧")
                        self.in_menu = True
                    return
        else:
            # 没有选择的剧情帧，等待用户继续
            print("按回车继续，或输入命令 (Q-快存 L-快读 A-好感度 M-菜单):")
            user_input = input().strip().lower()
            
            if user_input in ['q', 'l', 'a', 'm', 's', 'r', 'h']:
                if self.handle_special_command(user_input):
                    return
            
            # 转到下一帧
            next_frame = frame.get_next_frame()
            if next_frame:
                self.current_frame_id = next_frame
            else:
                self.in_menu = True
    
    def handle_special_command(self, command: str) -> bool:
        """
        处理特殊命令
        
        Returns:
            是否需要中断当前流程
        """
        if command == 'q':  # 快速存档
            self.quicksave()
            return False
        elif command == 'l':  # 快速读档
            return self.quickload()
        elif command == 'a':  # 查看好感度
            self.show_affinity()
            return False
        elif command == 'm':  # 主菜单
            self.in_menu = True
            return True
        elif command == 's':  # 存档菜单
            self.show_save_menu()
            return False
        elif command == 'r':  # 读档菜单
            return self.show_load_menu()
        elif command == 'h':  # 帮助
            self.show_help()
            return False
        
        return False
    
    def apply_choice_effect(self, frame: StoryFrame, choice_key: str):
        """应用选择效果"""
        effect = frame.get_choice_effect(choice_key)
        
        if not effect:
            return
        
        current_target = self.character_manager.get_current_target()
        
        # 应用好感度变化
        if "affinity" in effect and current_target:
            affinity_str = str(effect["affinity"])
            try:
                if affinity_str.startswith(('+', '-')):
                    affinity_change = int(affinity_str)
                    actual_change = current_target.add_affinity(affinity_change, "对话选择")
                    
                    if actual_change != 0:
                        print(f"💕 {current_target.display_name} 好感度 {actual_change:+d}")
            except ValueError:
                pass
        
        # 应用性格特征变化
        if "personality" in effect:
            personality_str = effect["personality"]
            # 解析性格变化字符串，如 "谦逊+3, 开放+5"
            for trait_change in personality_str.split(','):
                trait_change = trait_change.strip()
                if '+' in trait_change:
                    trait, value = trait_change.split('+')
                    self.player_data["personality"][trait.strip()] = \
                        self.player_data["personality"].get(trait.strip(), 0) + int(value)
        
        # 设置标记
        if "flag" in effect:
            flag_name = effect["flag"]
            if current_target:
                current_target.set_flag(flag_name)
        
        # 设置游戏标记
        if "game_flag" in effect:
            flag_name = effect["game_flag"]
            self.game_flags[flag_name] = True
    
    def apply_character_development(self, development: Dict[str, Any]):
        """应用角色发展"""
        current_target = self.character_manager.get_current_target()
        if not current_target:
            return
        
        # 应用好感度变化
        if "affinity" in development:
            affinity = development["affinity"]
            current_target.affinity = max(0, min(100, affinity))
        
        # 设置关系阶段
        if "relationship_stage" in development:
            current_target.relationship_stage = development["relationship_stage"]
        
        # 设置特殊标记
        for key, value in development.items():
            if key not in ["affinity", "relationship_stage"] and isinstance(value, bool):
                current_target.set_flag(key, value)
    
    def apply_character_stats(self, stats: Dict[str, Any]):
        """应用角色状态"""
        current_target = self.character_manager.get_current_target()
        if not current_target:
            return
        
        # 应用好感度变化
        if "affinity" in stats:
            current_target.affinity = max(0, min(100, stats["affinity"]))
        
        # 应用其他状态
        if "first_impression" in stats:
            current_target.set_flag("first_impression", stats["first_impression"])
    
    def handle_menu(self):
        """处理主菜单"""
        while self.in_menu and self.running:
            self.show_main_menu()
            
            choice = self.ui.get_choice("请选择", ["1", "2", "3", "4", "5", "6", "7", "8", "0"])
            
            if choice == "1":  # 继续游戏
                self.in_menu = False
            elif choice == "2":  # 存档
                self.show_save_menu()
            elif choice == "3":  # 读档
                if self.show_load_menu():
                    self.in_menu = False
            elif choice == "4":  # 查看好感度
                self.show_affinity()
            elif choice == "5":  # 游戏统计
                self.show_statistics()
            elif choice == "6":  # 设置
                self.show_settings()
            elif choice == "7":  # 帮助
                self.show_help()
            elif choice == "8":  # 关于
                self.show_about()
            elif choice == "0":  # 退出
                self.quit_game()
    
    def show_main_menu(self):
        """显示主菜单"""
        menu_options = [
            {"text": "继续游戏", "icon": "▶️"},
            {"text": "存档", "icon": "💾"},
            {"text": "读档", "icon": "📁"},
            {"text": "查看好感度", "icon": "💕"},
            {"text": "游戏统计", "icon": "📊"},
            {"text": "设置", "icon": "⚙️"},
            {"text": "帮助", "icon": "❓"},
            {"text": "关于", "icon": "ℹ️"}
        ]
        
        self.ui.print_menu("主菜单", menu_options)
    
    def show_save_menu(self):
        """显示存档菜单"""
        self.ui.clear_screen()
        self.ui.print_title("💾 存档管理")
        
        saves = self.save_system.get_save_list()
        
        print("选择存档位置:")
        for i in range(1, 6):  # 5个存档位
            save_name = f"save_{i:02d}"
            existing_save = next((s for s in saves if s["filename"] == save_name), None)
            
            if existing_save:
                print(f"  {i}. [已使用] {save_name} - {existing_save['timestamp']}")
            else:
                print(f"  {i}. [空位] {save_name}")
        
        print(f"  Q. 快速存档")
        print(f"  0. 返回")
        print()
        
        choice = self.ui.get_choice("请选择存档位置", ["1", "2", "3", "4", "5", "q", "0"])
        
        if choice == "0":
            return
        elif choice == "q":
            self.quicksave()
        else:
            save_name = f"save_{int(choice):02d}"
            game_state = self.get_game_state()
            if self.save_system.save_game(game_state, save_name):
                self.progress.add_statistic("saves_made")
                self.ui.print_success(f"游戏已保存到位置 {choice}")
            self.ui.wait_for_input()
    
    def show_load_menu(self) -> bool:
        """
        显示读档菜单
        
        Returns:
            是否成功读档
        """
        self.ui.clear_screen()
        self.ui.print_title("📁 读档管理")
        
        saves = self.save_system.get_save_list()
        
        if not saves:
            self.ui.print_info("没有找到存档文件")
            self.ui.wait_for_input()
            return False
        
        # 显示存档列表
        self.ui.print_save_list(saves)
        
        valid_choices = [str(i) for i in range(1, len(saves) + 1)]
        if self.save_system.has_quicksave():
            print(f"  Q. 快速读档")
            valid_choices.append("q")
        
        valid_choices.append("0")
        print(f"  0. 返回")
        print()
        
        choice = self.ui.get_choice("请选择要读取的存档", valid_choices)
        
        if choice == "0":
            return False
        elif choice == "q":
            return self.quickload()
        else:
            save_index = int(choice) - 1
            if 0 <= save_index < len(saves):
                save_name = saves[save_index]["filename"]
                return self.load_game(save_name)
        
        return False
    
    def show_affinity(self):
        """显示好感度"""
        self.ui.clear_screen()
        characters = self.character_manager.get_all_characters()
        char_data = {name: {
            "met": char.met,
            "affinity": char.affinity,
            "display_name": char.display_name,
            "relationship_stage": char.relationship_stage
        } for name, char in characters.items()}
        
        self.ui.print_character_status(char_data)
        self.ui.wait_for_input()
    
    def show_statistics(self):
        """显示游戏统计"""
        self.ui.clear_screen()
        self.ui.print_title("📊 游戏统计")
        
        progress_data = self.progress.get_progress_data()
        self.ui.print_game_stats(progress_data)
        
        # 显示剧情进度
        story_progress = self.story_loader.get_story_progress(self.get_game_state())
        print(f"📖 剧情进度: {story_progress['completed_frames']}/{story_progress['total_frames']} "
              f"({story_progress['completion_rate']:.1%})")
        
        self.ui.wait_for_input()
    
    def show_settings(self):
        """显示设置"""
        self.ui.clear_screen()
        self.ui.print_title("⚙️ 设置")
        
        print("  暂无可设置项目")
        print()
        self.ui.wait_for_input()
    
    def show_help(self):
        """显示帮助"""
        self.ui.clear_screen()
        self.ui.print_title("❓ 帮助")
        self.show_controls()
        self.ui.wait_for_input()
    
    def show_about(self):
        """显示关于"""
        self.ui.clear_screen()
        self.ui.print_title("ℹ️ 关于游戏")
        
        game_config = self.config_loader.get_game_config()
        game_info = game_config.get("game_info", {})
        
        print(f"  游戏名称: {game_info.get('title', '校园恋爱物语')}")
        print(f"  版本: {game_info.get('version', '1.0.0')}")
        print(f"  描述: {game_info.get('description', '')}")
        print()
        print("  基于原Campus_IF_Love剧本扩展制作")
        print("  感谢您的游玩！")
        print()
        
        self.ui.wait_for_input()
    
    def quicksave(self):
        """快速存档"""
        game_state = self.get_game_state()
        if self.save_system.quicksave(game_state):
            self.progress.add_statistic("saves_made")
            print("✅ 快速存档完成")
        else:
            print("❌ 快速存档失败")
        time.sleep(1)
    
    def quickload(self) -> bool:
        """
        快速读档
        
        Returns:
            是否成功读档
        """
        save_data = self.save_system.quickload()
        if save_data:
            self.load_game_state(save_data)
            self.progress.add_statistic("loads_made")
            print("✅ 快速读档完成")
            time.sleep(1)
            return True
        else:
            print("❌ 快速读档失败")
            time.sleep(1)
            return False
    
    def load_game(self, save_name: str) -> bool:
        """
        读取游戏
        
        Args:
            save_name: 存档名称
            
        Returns:
            是否成功读档
        """
        save_data = self.save_system.load_game(save_name)
        if save_data:
            self.load_game_state(save_data)
            self.progress.add_statistic("loads_made")
            return True
        else:
            self.ui.print_error("读档失败")
            self.ui.wait_for_input()
            return False
    
    def get_game_state(self) -> Dict[str, Any]:
        """获取当前游戏状态"""
        progress_data = self.progress.get_progress_data()
        character_data = self.character_manager.save_data()
        
        return {
            "version": "1.0.0",
            "current_frame": self.current_frame_id,
            "game_flags": self.game_flags,
            "player_data": self.player_data,
            "character_data": character_data,
            **progress_data
        }
    
    def load_game_state(self, save_data: Dict[str, Any]):
        """加载游戏状态"""
        self.current_frame_id = save_data.get("current_frame", "frame_001")
        self.game_flags = save_data.get("game_flags", {})
        self.player_data = save_data.get("player_data", self.player_data)
        
        # 加载角色数据
        character_data = save_data.get("character_data", {})
        if character_data:
            self.character_manager.load_data(character_data)
        
        # 加载进度数据
        self.progress.load_progress_data(save_data)
    
    def quit_game(self):
        """退出游戏"""
        self.ui.clear_screen()
        self.ui.print_title("👋 感谢游玩")
        
        # 自动保存
        game_state = self.get_game_state()
        self.save_system.autosave(game_state)
        
        print("  游戏已自动保存")
        print("  欢迎下次再来！")
        print()
        
        self.running = False

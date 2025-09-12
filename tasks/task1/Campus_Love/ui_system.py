#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户界面系统 - 终端界面显示和交互
UI System - Terminal interface display and interaction
"""

import os
import sys
import time
from typing import List, Dict, Any, Optional, Callable
from datetime import datetime

class UISystem:
    """终端用户界面系统"""
    
    def __init__(self):
        """初始化UI系统"""
        self.width = 80  # 界面宽度
        self.separator = "=" * self.width
        self.thin_separator = "-" * self.width
        
    def clear_screen(self):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_title(self, title: str):
        """打印标题"""
        print(self.separator)
        print(f" {title} ".center(self.width))
        print(self.separator)
    
    def print_subtitle(self, subtitle: str):
        """打印副标题"""
        print(f" {subtitle} ".center(self.width))
        print(self.thin_separator)
    
    def print_box(self, content: str, title: str = ""):
        """打印带边框的内容"""
        lines = content.split('\n')
        max_width = max(len(line) for line in lines) if lines else 0
        box_width = min(max_width + 4, self.width)
        
        if title:
            print(f"╭─ {title} " + "─" * (box_width - len(title) - 4) + "╮")
        else:
            print("╭" + "─" * (box_width - 2) + "╮")
        
        for line in lines:
            padding = box_width - len(line) - 3
            print(f"│ {line}" + " " * padding + "│")
        
        print("╰" + "─" * (box_width - 2) + "╯")
    
    def print_story_frame(self, content: str, title: str = "", scene: str = ""):
        """打印剧情帧"""
        self.clear_screen()
        
        if title:
            self.print_title(f"📖 {title}")
        
        if scene:
            self.print_subtitle(f"🎬 场景: {scene}")
            print()
        
        # 逐行显示内容，模拟打字效果
        lines = content.split('\n')
        for line in lines:
            if line.strip():
                print(f"  {line}")
                time.sleep(0.1)  # 可调整显示速度
            else:
                print()
        print()
    
    def print_dialogue(self, speaker: str, text: str, options: List[Dict[str, Any]] = None):
        """打印对话"""
        # 显示说话者和对话内容
        print(f"💬 {speaker}:")
        print(f'   "{text}"')
        print()
        
        # 显示选项
        if options:
            print("请选择你的回答:")
            for i, option in enumerate(options, 1):
                print(f"  {i}. {option['text']}")
            print()
    
    def get_choice(self, prompt: str = "请输入选择", valid_choices: List[str] = None, timeout: int = None) -> str:
        """获取用户选择"""
        while True:
            try:
                if timeout:
                    print(f"{prompt} (超时 {timeout} 秒): ", end="", flush=True)
                else:
                    print(f"{prompt}: ", end="", flush=True)
                
                choice = input().strip()
                
                if valid_choices and choice not in valid_choices:
                    print(f"❌ 无效选择，请输入: {', '.join(valid_choices)}")
                    continue
                
                return choice
                
            except KeyboardInterrupt:
                print("\n\n游戏已退出")
                sys.exit(0)
            except EOFError:
                return ""
    
    def print_menu(self, title: str, options: List[Dict[str, Any]], show_back: bool = True):
        """打印菜单"""
        self.clear_screen()
        self.print_title(title)
        
        for i, option in enumerate(options, 1):
            icon = option.get('icon', '►')
            desc = option.get('description', '')
            print(f"  {i}. {icon} {option['text']}")
            if desc:
                print(f"     {desc}")
            print()
        
        if show_back:
            print(f"  0. 🔙 返回")
        print()
    
    def print_character_status(self, characters: Dict[str, Any]):
        """打印角色状态"""
        print("=" * 60)
        print(" 📊 角色好感度 ".center(60))
        print("=" * 60)
        
        for name, char in characters.items():
            if char.get('met', False):
                affinity = char.get('affinity', 0)
                display_name = char.get('display_name', name)
                relationship = char.get('relationship_stage', 'stranger')
                
                # 好感度条显示
                bar_length = 20
                filled_length = int(bar_length * affinity / 100)
                bar = "█" * filled_length + "░" * (bar_length - filled_length)
                
                # 关系状态图标
                if affinity >= 85:
                    status_icon = "💖"
                elif affinity >= 60:
                    status_icon = "😊"
                elif affinity >= 30:
                    status_icon = "🙂"
                else:
                    status_icon = "😐"
                
                print(f"  {status_icon} {display_name}")
                print(f"     好感度: [{bar}] {affinity}/100")
                print(f"     关系: {relationship}")
                print()
    
    def print_save_list(self, saves: List[Dict[str, Any]]):
        """打印存档列表"""
        if not saves:
            print("  没有找到存档文件")
            return
        
        print("存档列表:")
        print("-" * 70)
        
        for i, save in enumerate(saves, 1):
            filename = save.get('filename', '未知')
            timestamp = save.get('timestamp', '未知时间')
            playtime = save.get('playtime', 0)
            current_frame = save.get('current_frame', '未知位置')
            
            # 格式化时间显示
            try:
                if timestamp != '未知时间':
                    dt = datetime.fromisoformat(timestamp)
                    time_str = dt.strftime("%m-%d %H:%M")
                else:
                    time_str = timestamp
            except:
                time_str = timestamp
            
            # 格式化游戏时长
            hours = playtime // 3600
            minutes = (playtime % 3600) // 60
            time_played = f"{hours:02d}:{minutes:02d}"
            
            print(f"  {i}. {filename}")
            print(f"     时间: {time_str} | 游戏时长: {time_played}")
            print(f"     位置: {current_frame}")
            print()
    
    def print_game_stats(self, stats: Dict[str, Any]):
        """打印游戏统计"""
        print("📈 游戏统计")
        print("-" * 40)
        
        playtime = stats.get('playtime', 0)
        hours = playtime // 3600
        minutes = (playtime % 3600) // 60
        seconds = playtime % 60
        
        print(f"  游戏时长: {hours:02d}:{minutes:02d}:{seconds:02d}")
        print(f"  做出选择: {stats.get('choices_made', 0)} 次")
        print(f"  对话次数: {stats.get('dialogues_seen', 0)} 次")
        print(f"  送出礼物: {stats.get('gifts_given', 0)} 次")
        print(f"  保存次数: {stats.get('saves_made', 0)} 次")
        print(f"  读取次数: {stats.get('loads_made', 0)} 次")
        print()
    
    def print_gift_menu(self, gifts: Dict[str, Any]):
        """打印礼物菜单"""
        self.print_title("🎁 礼物选择")
        
        for i, (gift_name, gift_info) in enumerate(gifts.items(), 1):
            description = gift_info.get('description', '神秘的礼物')
            print(f"  {i}. {gift_name}")
            print(f"     {description}")
            print()
        
        print(f"  0. 🔙 取消")
        print()
    
    def show_gift_result(self, gift_name: str, character_name: str, affinity_change: int):
        """显示送礼结果"""
        if affinity_change > 0:
            print(f"✨ {character_name} 收到了 {gift_name}，好感度 +{affinity_change}!")
        elif affinity_change < 0:
            print(f"😅 {character_name} 对 {gift_name} 不太感兴趣，好感度 {affinity_change}...")
        else:
            print(f"😐 {character_name} 收到了 {gift_name}，没什么特别反应")
        
        print("\n按回车键继续...")
        input()
    
    def print_ending(self, title: str, content: str, ending_type: str):
        """打印结局"""
        self.clear_screen()
        
        # 根据结局类型选择不同的图标和颜色
        if ending_type == "true_ending":
            icon = "💖"
            border = "✨" * (self.width // 2)
        elif ending_type == "good_ending":
            icon = "😊" 
            border = "🌟" * (self.width // 2)
        elif ending_type == "normal_ending":
            icon = "🙂"
            border = "⭐" * (self.width // 2)
        else:
            icon = "👋"
            border = "🌸" * (self.width // 2)
        
        print(border)
        print(f" {icon} {title} {icon} ".center(self.width))
        print(border)
        print()
        
        # 逐行显示结局内容
        lines = content.split('\n')
        for line in lines:
            if line.strip():
                print(f"  {line}")
                time.sleep(0.3)
            else:
                print()
        
        print("\n" + border)
        print(" 感谢游玩！ ".center(self.width))
        print(border)
    
    def wait_for_input(self, prompt: str = "按回车键继续..."):
        """等待用户输入"""
        try:
            input(f"\n{prompt}")
        except KeyboardInterrupt:
            print("\n\n游戏已退出")
            sys.exit(0)
    
    def print_loading(self, text: str = "加载中"):
        """显示加载动画"""
        animation = "|/-\\"
        for i in range(8):
            print(f"\r{text} {animation[i % len(animation)]}", end="", flush=True)
            time.sleep(0.3)
        print("\r" + " " * (len(text) + 2) + "\r", end="", flush=True)
    
    def print_error(self, message: str):
        """打印错误信息"""
        print(f"❌ 错误: {message}")
    
    def print_success(self, message: str):
        """打印成功信息"""
        print(f"✅ {message}")
    
    def print_warning(self, message: str):
        """打印警告信息"""
        print(f"⚠️ 警告: {message}")
    
    def print_info(self, message: str):
        """打印信息"""
        print(f"ℹ️ {message}")

# 全局UI系统实例
ui = UISystem()

def get_ui() -> UISystem:
    """获取全局UI系统实例"""
    return ui

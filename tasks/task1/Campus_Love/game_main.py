#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
校园恋爱物语 - 主游戏文件
Campus Love Story - Main Game File
"""

import sys
import os
from game_engine import GameEngine

def main():
    """主函数"""
    try:
        # 检查依赖
        try:
            import yaml
        except ImportError:
            print("错误: 需要安装 PyYAML 库")
            print("请运行: pip install PyYAML")
            return
        
        # 设置配置文件目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        from config_loader import set_config_dir
        set_config_dir(current_dir)
        
        # 创建游戏引擎并开始游戏
        game = GameEngine()
        game.start_game()
        
    except KeyboardInterrupt:
        print("\n\n游戏已退出")
    except Exception as e:
        print(f"\n游戏出现错误: {e}")
        print("请检查游戏文件是否完整")

if __name__ == "__main__":
    main()

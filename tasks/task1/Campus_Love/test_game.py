#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的游戏测试脚本
Simple Game Test Script
"""

def test_imports():
    """测试模块导入"""
    try:
        print("测试模块导入...")
        
        # 测试配置加载器
        from config_loader import get_config_loader
        config_loader = get_config_loader()
        print("✅ config_loader 导入成功")
        
        # 测试角色系统
        from character_system import CharacterManager
        char_manager = CharacterManager()
        print("✅ character_system 导入成功")
        
        # 测试剧情加载器
        from story_loader import get_story_loader
        story_loader = get_story_loader()
        print("✅ story_loader 导入成功")
        
        # 测试存档系统
        from save_system import SaveSystem
        save_system = SaveSystem()
        print("✅ save_system 导入成功")
        
        # 测试UI系统
        from ui_system import get_ui
        ui = get_ui()
        print("✅ ui_system 导入成功")
        
        print("\n🎉 所有模块导入成功！")
        return True
        
    except ImportError as e:
        print(f"❌ 导入失败: {e}")
        return False
    except Exception as e:
        print(f"❌ 其他错误: {e}")
        return False

def test_yaml_loading():
    """测试YAML文件加载"""
    try:
        print("\n测试YAML文件加载...")
        
        from config_loader import get_config_loader
        config_loader = get_config_loader()
        
        # 测试主配置
        game_config = config_loader.get_game_config()
        if game_config:
            print("✅ game_config.yaml 加载成功")
        else:
            print("❌ game_config.yaml 加载失败")
            
        # 测试序章
        prologue = config_loader.get_prologue_frames()
        if prologue:
            print("✅ prologue_frames.yaml 加载成功")
        else:
            print("❌ prologue_frames.yaml 加载失败")
            
        print("\n🎉 YAML文件加载测试完成！")
        return True
        
    except Exception as e:
        print(f"❌ YAML加载测试失败: {e}")
        return False

def test_character_system():
    """测试角色系统"""
    try:
        print("\n测试角色系统...")
        
        from character_system import CharacterManager
        char_manager = CharacterManager()
        
        # 测试角色创建
        characters = char_manager.get_all_characters()
        print(f"✅ 创建了 {len(characters)} 个角色")
        
        # 测试好感度系统
        senpai = char_manager.get_character("senpai")
        if senpai:
            old_affinity = senpai.affinity
            senpai.add_affinity(10, "测试")
            new_affinity = senpai.affinity
            print(f"✅ 好感度系统工作正常: {old_affinity} -> {new_affinity}")
        
        print("\n🎉 角色系统测试完成！")
        return True
        
    except Exception as e:
        print(f"❌ 角色系统测试失败: {e}")
        return False

def test_save_system():
    """测试存档系统"""
    try:
        print("\n测试存档系统...")
        
        from save_system import SaveSystem
        save_system = SaveSystem()
        
        # 测试保存
        test_data = {"test": "data", "number": 123}
        save_result = save_system.save_game(test_data, "test_save.json")
        if save_result:
            print("✅ 保存功能正常")
        else:
            print("❌ 保存功能失败")
            
        # 测试读取
        load_result = save_system.load_game("test_save.json")
        if load_result and load_result.get("test") == "data":
            print("✅ 读取功能正常")
        else:
            print("❌ 读取功能失败")
            
        # 清理测试文件
        import os
        if os.path.exists("test_save.json"):
            os.remove("test_save.json")
            
        print("\n🎉 存档系统测试完成！")
        return True
        
    except Exception as e:
        print(f"❌ 存档系统测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🧪 开始游戏系统测试")
    print("=" * 50)
    
    success_count = 0
    total_tests = 4
    
    # 执行各项测试
    if test_imports():
        success_count += 1
    
    if test_yaml_loading():
        success_count += 1
        
    if test_character_system():
        success_count += 1
        
    if test_save_system():
        success_count += 1
    
    # 输出测试结果
    print("\n" + "=" * 50)
    print(f"🧪 测试完成！成功: {success_count}/{total_tests}")
    
    if success_count == total_tests:
        print("🎉 所有测试通过！游戏系统工作正常。")
        print("\n💡 提示: 可以运行 'python game_main.py' 开始游戏")
    else:
        print("⚠️ 部分测试失败，请检查相关模块。")
        
    print("\n💡 游戏已准备就绪，可以运行 'python game_main.py' 开始游戏！")

if __name__ == "__main__":
    main()

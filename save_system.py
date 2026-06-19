"""
ドラゴンクエスト風RPG - セーブ・ロード機能
"""

import json
import os
from datetime import datetime


class SaveData:
    """セーブデータクラス"""
    
    def __init__(self, filename="savegame.json"):
        self.filename = filename
        self.saves = {}
    
    def save_game(self, player, slot=1):
        """ゲームをセーブする"""
        save_info = {
            'slot': slot,
            'player_name': player.name,
            'level': player.level,
            'hp': player.hp,
            'max_hp': player.max_hp,
            'mp': player.mp,
            'max_mp': player.max_mp,
            'attack': player.attack,
            'defense': player.defense,
            'speed': player.speed,
            'experience': player.experience,
            'gold': player.gold,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # インベントリがあればセーブ
        if hasattr(player, 'inventory'):
            inventory_data = {
                'items': [],
                'equipment': {}
            }
            
            for item in player.inventory.items:
                item_info = {
                    'name': item.name,
                    'item_type': item.item_type,
                    'value': item.value,
                    'description': item.description
                }
                inventory_data['items'].append(item_info)
            
            for slot_type, equipment in player.inventory.equipment.items():
                if equipment:
                    eq_info = {
                        'name': equipment.name,
                        'equipment_type': equipment.equipment_type,
                        'attack_bonus': equipment.attack_bonus,
                        'defense_bonus': equipment.defense_bonus,
                        'hp_bonus': equipment.hp_bonus,
                        'speed_bonus': equipment.speed_bonus,
                        'value': equipment.value
                    }
                    inventory_data['equipment'][slot_type] = eq_info
            
            save_info['inventory'] = inventory_data
        
        # スキルがあればセーブ
        if hasattr(player, 'skills'):
            skill_names = [skill.name for skill in player.skills]
            save_info['skills'] = skill_names
        
        # クエストがあればセーブ
        if hasattr(player, 'quests'):
            quest_data = []
            for quest in player.quests:
                quest_info = {
                    'title': quest.title,
                    'completed': quest.completed,
                    'progress': quest.progress,
                    'claimed': quest.claimed
                }
                quest_data.append(quest_info)
            save_info['quests'] = quest_data
        
        self.saves[slot] = save_info
        self._write_to_file()
        
        print(f"\n💾 スロット {slot} にセーブしました！")
        print(f"   {player.name} - Lv.{player.level}")
        print(f"   セーブ時刻: {save_info['timestamp']}")
    
    def load_game(self, player, slot=1):
        """ゲームをロードする"""
        self._read_from_file()
        
        if slot not in self.saves:
            print(f"スロット {slot} にセーブデータがありません。")
            return False
        
        save_info = self.saves[slot]
        
        # プレイヤーデータをロード
        player.name = save_info['player_name']
        player.level = save_info['level']
        player.hp = save_info['hp']
        player.max_hp = save_info['max_hp']
        player.mp = save_info['mp']
        player.max_mp = save_info['max_mp']
        player.attack = save_info['attack']
        player.defense = save_info['defense']
        player.speed = save_info['speed']
        player.experience = save_info['experience']
        player.gold = save_info['gold']
        
        print(f"\n📂 スロット {slot} からロードしました！")
        print(f"   {player.name} - Lv.{player.level}")
        print(f"   セーブ時刻: {save_info['timestamp']}")
        
        return True
    
    def list_saves(self):
        """セーブデータの一覧を表示"""
        self._read_from_file()
        
        print("\n" + "=" * 50)
        print("【セーブデータ一覧】")
        print("=" * 50)
        
        if not self.saves:
            print("セーブデータがありません。\n")
            return
        
        for slot in sorted(self.saves.keys()):
            save_info = self.saves[slot]
            player_name = save_info.get('player_name', '???')
            level = save_info.get('level', '?')
            timestamp = save_info.get('timestamp', '不明')
            
            print(f"\nスロット {slot}:")
            print(f"  キャラクター: {player_name}")
            print(f"  レベル: {level}")
            print(f"  セーブ時刻: {timestamp}")
        
        print()
    
    def delete_save(self, slot=1):
        """セーブデータを削除"""
        self._read_from_file()
        
        if slot in self.saves:
            del self.saves[slot]
            self._write_to_file()
            print(f"\n🗑️  スロット {slot} のセーブデータを削除しました。")
            return True
        
        print(f"スロット {slot} にセーブデータがありません。")
        return False
    
    def _write_to_file(self):
        """ファイルに書き込む"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.saves, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"セーブエラー: {e}")
    
    def _read_from_file(self):
        """ファイルから読み込む"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.saves = json.load(f)
            else:
                self.saves = {}
        except (IOError, json.JSONDecodeError) as e:
            print(f"ロードエラー: {e}")
            self.saves = {}


class SaveManager:
    """セーブ管理クラス"""
    
    def __init__(self):
        self.save_data = SaveData()
    
    def show_save_menu(self, player):
        """セーブメニューを表示"""
        print("\n" + "─" * 50)
        print("【セーブメニュー】")
        print("─" * 50)
        print("1. ゲームをセーブ")
        print("2. ゲームをロード")
        print("3. セーブデータ一覧")
        print("4. セーブデータ削除")
        print("5. メインメニューに戻る")
        print("─" * 50)
        
        while True:
            choice = input("\n> ").strip()
            
            if choice == '1':
                self.save_slot_menu(player, action='save')
                break
            elif choice == '2':
                self.save_slot_menu(player, action='load')
                break
            elif choice == '3':
                self.save_data.list_saves()
                break
            elif choice == '4':
                self.delete_save_menu()
                break
            elif choice == '5':
                break
            else:
                print("1～5の数字を入力してください。")
    
    def save_slot_menu(self, player, action='save'):
        """スロット選択メニュー"""
        print(f"\n【セーブスロット選択】")
        print("1. スロット1")
        print("2. スロット2")
        print("3. スロット3")
        print("4. キャンセル")
        
        while True:
            choice = input("\n> ").strip()
            
            if choice in ['1', '2', '3']:
                slot = int(choice)
                if action == 'save':
                    self.save_data.save_game(player, slot)
                elif action == 'load':
                    self.save_data.load_game(player, slot)
                break
            elif choice == '4':
                break
            else:
                print("1～4の数字を入力してください。")
    
    def delete_save_menu(self):
        """セーブデータ削除メニュー"""
        print(f"\n【削除するスロットを選択】")
        print("1. スロット1")
        print("2. スロット2")
        print("3. スロット3")
        print("4. キャンセル")
        
        while True:
            choice = input("\n> ").strip()
            
            if choice in ['1', '2', '3']:
                slot = int(choice)
                confirm = input(f"スロット {slot} を削除してもよろしいですか？ (y/n): ").strip().lower()
                if confirm == 'y':
                    self.save_data.delete_save(slot)
                break
            elif choice == '4':
                break
            else:
                print("1～4の数字を入力してください。")

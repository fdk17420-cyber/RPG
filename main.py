"""
ドラゴンクエスト風RPG - メインゲーム（拡張版）
全ての機能を統合したバージョン
"""

import random
from character import Player
from skills import SkillList
from battle import Battle
from items import Inventory, ItemList
from enemies import EnemyFactory
from dungeon import DungeonManager, DungeonExplorer, DungeonFloor
from npc import create_town_npcs, ShopNPC
from save_system import SaveManager


class ExpandedGame:
    """拡張版ゲーム管理クラス"""
    
    def __init__(self):
        self.player = None
        self.running = True
        self.in_town = True
        self.save_manager = SaveManager()
        self.dungeon_explorer = None
        self.npcs = []
        self.current_location = 'town'
    
    def show_title(self):
        """タイトル画面表示"""
        title = """
╔════════════════════════════════════════╗
║   🐉 ドラゴンクエスト風RPG 🐉        ║
║                                        ║
║   ~ 完全版 ターンベース戦闘ゲーム ~  ║
║   セーブ・ダンジョン・NPC・装備品     ║
╚════════════════════════════════════════╝
"""
        print(title)
        print("【新規ゲーム / ゲーム続行】")
        print("1. 新規ゲーム開始")
        print("2. ゲーム続行（ロード）")
        print("3. 終了")
        print("─" * 40)
        
        while True:
            choice = input("\n> ").strip()
            if choice == '1':
                self.create_player()
                break
            elif choice == '2':
                if self.load_game():
                    break
            elif choice == '3':
                self.running = False
                return
            else:
                print("1～3の数字を入力してください。")
    
    def create_player(self):
        """プレイヤー作成"""
        print("\n【ゲーム開始】")
        print("─" * 40)
        
        while True:
            name = input("勇者の名前を入力してください: ").strip()
            if name and len(name) <= 20:
                break
            print("名前は1文字以上20文字以内でお願いします。")
        
        self.player = Player(name=name)
        self.player.inventory = Inventory()
        self.player.quests = []
        
        # 初期スキルを習得
        for skill in SkillList.get_player_start_skills():
            self.player.add_skill(skill)
        
        # 初期アイテムを追加
        potion = ItemList.get_all_items()['potion']
        self.player.inventory.add_item(potion, 3)
        
        self.dungeon_explorer = DungeonExplorer(self.player)
        self.npcs = create_town_npcs()
        
        print(f"\n✨ {self.player.name}が誕生した！")
        print(self.player.show_status())
    
    def load_game(self):
        """ゲームをロード"""
        self.save_manager.show_save_menu(self.player or Player())
        
        if self.player is None:
            print("ゲームを新規作成してください。")
            return False
        
        self.dungeon_explorer = DungeonExplorer(self.player)
        self.npcs = create_town_npcs()
        return True
    
    def main_menu(self):
        """メインメニュー表示"""
        print("\n" + "═" * 50)
        print("【タウンメニュー】")
        print("═" * 50)
        print("1. ⚔️  敵と戦闘")
        print("2. 🏰 ダンジョン探索")
        print("3. 👥 NPC・ショップ")
        print("4. 📊 ステータス確認")
        print("5. 🎒 インベントリ")
        print("6. 📝 クエスト確認")
        print("7. 💾 セーブ・ロード")
        print("8. 🌙 ゲーム終了")
        print("─" * 50)
        
        while True:
            choice = input("\n> ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                return choice
            print("1～8の数字を入力してください。")
    
    def start_battle(self):
        """通常戦闘を開始"""
        if not self.player.is_alive:
            print("\n😢 勇者はすでに倒されています...")
            return
        
        print("\n【野外遭遇戦】")
        enemy = EnemyFactory.get_random_enemy()
        battle = Battle(self.player, enemy)
        result = battle.execute_battle()
        
        # クエスト進捗を更新
        if result == 'win':
            for quest in self.player.quests:
                quest.record_kill(enemy.name, self.player)
        
        if result == 'lose':
            self.player.is_alive = False
            self.running = False
    
    def show_dungeon_menu(self):
        """ダンジョンメニュー"""
        if self.dungeon_explorer.is_in_dungeon():
            print("\n【ダンジョン内メニュー】")
            print("1. 次の階層へ進む")
            print("2. 敵と戦闘")
            print("3. ダンジョンから脱出")
            print("4. ステータス確認")
            print("─" * 40)
            
            while True:
                choice = input("\n> ").strip()
                
                if choice == '1':
                    if self.dungeon_explorer.advance_floor():
                        print(f"\n{self.dungeon_explorer.current_floor}階に到達した...")
                    else:
                        print("\nダンジョンをクリアした！")
                        return
                
                elif choice == '2':
                    floor = self.dungeon_explorer.show_floor_info()
                    if floor and floor.enemies:
                        enemy = floor.enemies[0]
                        battle = Battle(self.player, enemy)
                        result = battle.execute_battle()
                        
                        if result == 'lose':
                            print("\nダンジョンから脱出できなかった...")
                            self.player.is_alive = False
                            self.running = False
                            return
                
                elif choice == '3':
                    if self.dungeon_explorer.escape_dungeon():
                        return
                    else:
                        floor = self.dungeon_explorer.show_floor_info()
                        if floor and floor.enemies:
                            enemy = floor.enemies[0]
                            battle = Battle(self.player, enemy)
                            result = battle.execute_battle()
                            if result == 'lose':
                                self.player.is_alive = False
                                self.running = False
                                return
                
                elif choice == '4':
                    print(self.player.show_status())
                    self.dungeon_explorer.get_dungeon_status()
                    break
                else:
                    print("1～4の数字を入力してください。")
        
        else:
            print("\n【ダンジョン選択】")
            DungeonManager.list_dungeons()
            
            print("どのダンジョンに入りますか？")
            print("1. 初心者用洞窟")
            print("2. 魔法の森")
            print("3. 暗い城")
            print("4. 火山地帯")
            print("5. 暗黒の塔")
            print("6. キャンセル")
            
            dungeon_map = {
                '1': 'beginner',
                '2': 'forest',
                '3': 'castle',
                '4': 'volcano',
                '5': 'dark_tower'
            }
            
            while True:
                choice = input("\n> ").strip()
                
                if choice in dungeon_map:
                    if self.dungeon_explorer.enter_dungeon(dungeon_map[choice]):
                        break
                elif choice == '6':
                    break
                else:
                    print("1～6の数字を入力してください。")
    
    def show_npc_menu(self):
        """NPC・ショップメニュー"""
        print("\n【タウン - NPC・ショップ】")
        for i, npc in enumerate(self.npcs, 1):
            print(f"{i}. {npc.name}と話す")
        print(f"{len(self.npcs) + 1}. キャンセル")
        
        while True:
            try:
                choice = int(input("\n> ").strip())
                if choice == len(self.npcs) + 1:
                    break
                if 1 <= choice <= len(self.npcs):
                    npc = self.npcs[choice - 1]
                    npc.talk(self.player)
                    break
                else:
                    print("無効な選択です。")
            except ValueError:
                print("数字を入力してください。")
    
    def show_status(self):
        """ステータス画面"""
        stats = self.player.inventory.get_equipped_stats()
        total_attack = self.player.attack + stats['attack']
        total_defense = self.player.defense + stats['defense']
        
        print(self.player.show_status())
        print("【装備ボーナス】")
        print(f"攻撃力ボーナス: +{stats['attack']}")
        print(f"防御力ボーナス: +{stats['defense']}")
        print(f"【合計ステータス】")
        print(f"攻撃力: {total_attack}")
        print(f"防御力: {total_defense}")
    
    def show_inventory(self):
        """インベントリ画面"""
        self.player.inventory.show_inventory()
    
    def show_quests(self):
        """クエスト確認"""
        print("\n" + "─" * 50)
        print("【クエスト一覧】")
        print("─" * 50)
        
        if not self.player.quests:
            print("受注中のクエストがありません。\n")
            return
        
        for i, quest in enumerate(self.player.quests, 1):
            status = "✅ 完了" if quest.completed else "進行中"
            print(f"\n{i}. {quest.title} [{status}]")
            print(f"   {quest.description}")
            print(f"   進捗: {quest.progress}/{quest.required}")
            print(f"   報酬: 経験値+{quest.reward_exp}, ゴルド+{quest.reward_gold}")
            
            if quest.completed and not quest.claimed:
                claim = input("\n   報酬を受け取りますか？ (y/n): ").strip().lower()
                if claim == 'y':
                    quest.claim(self.player)
        
        print()
    
    def show_game_over(self):
        """ゲームオーバー画面"""
        print("\n" + "═" * 50)
        print("╔" + "═" * 48 + "╗")
        print("║" + " " * 48 + "║")
        print("║" + "  ゲームオーバー".center(48) + "║")
        print("║" + " " * 48 + "║")
        print("║" + f"  {self.player.name} - Lv.{self.player.level}".center(48) + "║")
        print("║" + f"  最終経験値: {self.player.experience}".center(48) + "║")
        print("║" + f"  獲得ゴルド: {self.player.gold}".center(48) + "║")
        print("║" + " " * 48 + "║")
        print("╚" + "═" * 48 + "╝")
        print("=" * 50 + "\n")
    
    def run(self):
        """ゲームメインループ"""
        self.show_title()
        
        if not self.running or not self.player:
            return
        
        while self.running and self.player.is_alive:
            choice = self.main_menu()
            
            if choice == '1':
                self.start_battle()
            elif choice == '2':
                self.show_dungeon_menu()
            elif choice == '3':
                self.show_npc_menu()
            elif choice == '4':
                self.show_status()
            elif choice == '5':
                self.show_inventory()
            elif choice == '6':
                self.show_quests()
            elif choice == '7':
                self.save_manager.show_save_menu(self.player)
            elif choice == '8':
                confirm = input("\nゲームを終了してもよろしいですか？ (y/n): ").strip().lower()
                if confirm == 'y':
                    print("\nゲームを終了します...")
                    self.running = False
        
        if not self.player.is_alive:
            self.show_game_over()


def main():
    """メイン関数"""
    game = ExpandedGame()
    game.run()


if __name__ == "__main__":
    main()

"""
ドラゴンクエスト風RPG - メインゲーム
シンプルなターンベース戦闘システムで敵と戦闘します
"""

import random
from character import Player
from skills import SkillList
from battle import Battle, BattleFactory


class Game:
    """ゲーム管理クラス"""
    
    def __init__(self):
        self.player = None
        self.running = True
    
    def show_title(self):
        """タイトル画面表示"""
        title = """
╔════════════════════════════════════════╗
║   🐉 ドラゴンクエスト風RPG 🐉        ║
║                                        ║
║     ~ ターンベース戦闘システム ~      ║
╚════════════════════════════════════════╝
"""
        print(title)
    
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
        
        # 初期スキルを習得
        for skill in SkillList.get_player_start_skills():
            self.player.add_skill(skill)
        
        print(f"\n✨ {self.player.name}が誕生した！")
        print(self.player.show_status())
    
    def main_menu(self):
        """メインメニュー表示"""
        print("\n" + "═" * 40)
        print("【メインメニュー】")
        print("═" * 40)
        print("1. 敵と戦闘")
        print("2. ステータス確認")
        print("3. スキル一覧")
        print("4. ゲーム終了")
        print("─" * 40)
        
        while True:
            choice = input("\n> ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            print("1～4の数字を入力してください。")
    
    def start_battle(self):
        """戦闘を開始"""
        if not self.player.is_alive:
            print("\n😢 勇者はすでに倒されています...")
            return
        
        print("\n【敵出現】")
        enemy = BattleFactory.get_random_enemy()
        battle = Battle(self.player, enemy)
        result = battle.execute_battle()
        
        if result == 'lose':
            self.player.is_alive = False
            self.running = False
    
    def show_status(self):
        """ステータス画面"""
        print(self.player.show_status())
        print(f"ゴルド: {self.player.gold}")
    
    def show_skills(self):
        """スキル一覧表示"""
        print("\n" + "─" * 40)
        print("【習得スキル一覧】")
        print("─" * 40)
        
        if not self.player.skills:
            print("スキルを習得していません。")
            return
        
        for i, skill in enumerate(self.player.skills, 1):
            print(f"{i}. {skill.name}")
            print(f"   MP消費: {skill.mp_cost} | 威力: {skill.power}")
        
        print("\n【利用可能なスキル一覧】")
        print("ゲーム進行により習得できるスキル:")
        all_skills = SkillList.get_all_player_skills()
        for skill in all_skills:
            if skill not in self.player.skills:
                print(f"  - {skill.name} (MP消費: {skill.mp_cost})")
    
    def show_game_over(self):
        """ゲームオーバー画面"""
        print("\n" + "═" * 50)
        print("╔" + "═" * 48 + "╗")
        print("║" + " " * 48 + "║")
        print("║" + f"  ゲームオーバー".center(48) + "║")
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
        self.create_player()
        
        while self.running:
            choice = self.main_menu()
            
            if choice == '1':
                self.start_battle()
            elif choice == '2':
                self.show_status()
            elif choice == '3':
                self.show_skills()
            elif choice == '4':
                print("\nゲームを終了します...")
                self.running = False
        
        if not self.player.is_alive:
            self.show_game_over()


def main():
    """メイン関数"""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

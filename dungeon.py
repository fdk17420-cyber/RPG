"""
ドラゴンクエスト風RPG - ダンジョン探索システム
"""

import random
from enemies import EnemyFactory


class Dungeon:
    """ダンジョンクラス"""
    
    def __init__(self, name, floors, difficulty):
        self.name = name
        self.floors = floors
        self.current_floor = 1
        self.difficulty = difficulty  # 1-10
        self.description = ""
        self.visited = False
    
    def show_info(self):
        """ダンジョン情報を表示"""
        print(f"\n【{self.name}】")
        print(f"難易度: {'★' * self.difficulty}")
        print(f"階層数: {self.floors}階")
        print(f"{self.description}")


class DungeonFloor:
    """ダンジョンの階層"""
    
    def __init__(self, floor_number, dungeon_name, difficulty):
        self.floor_number = floor_number
        self.dungeon_name = dungeon_name
        self.difficulty = difficulty
        self.enemies = []
        self.treasures = []
        self.generate_floor()
    
    def generate_floor(self):
        """階層を生成"""
        # ランダムに敵を配置
        enemy_count = random.randint(1, 3)
        for _ in range(enemy_count):
            enemy = EnemyFactory.get_dungeon_enemies(self.floor_number)
            self.enemies.append(enemy)
    
    def show_description(self):
        """階層の説明を表示"""
        descriptions = {
            1: "薄暗い洞窟の入り口だ。弱い敵が徘徊している。",
            2: "洞窟は深くなっている。敵の気配が増している。",
            3: "妖しい光が漂っている。不気味な敵が現れ始めた。",
            4: "地下深くへ。ここは敵の巣だ。",
            5: "深い地下。強力な敵が現れるようになった。",
            6: "さらに奥深く。危険が迫っている。",
            7: "ボスの間へ向かう通路。強い敵が守っている。",
            8: "ボスの館。恐ろしい気配が満ちている。",
            9: "暗黒の領域。邪悪な力が渦巻いている。",
            10: "竜の玉座。運命の時が来た。"
        }
        return descriptions.get(self.floor_number, "謎の空間だ。")


class DungeonManager:
    """ダンジョン管理クラス"""
    
    dungeons = {
        'beginner': Dungeon("初心者用洞窟", 3, 1),
        'forest': Dungeon("魔法の森", 5, 2),
        'castle': Dungeon("暗い城", 6, 3),
        'volcano': Dungeon("火山地帯", 7, 4),
        'dark_tower': Dungeon("暗黒の塔", 10, 5)
    }
    
    @staticmethod
    def setup_dungeons():
        """ダンジョンを設定"""
        DungeonManager.dungeons['beginner'].description = "新しい冒険者向けの簡単なダンジョン。"
        DungeonManager.dungeons['forest'].description = "魔法が満ちた森。不思議な敵がいる。"
        DungeonManager.dungeons['castle'].description = "廃れた古い城。強い敵が徘徊している。"
        DungeonManager.dungeons['volcano'].description = "溶岩が流れる危険な地帯。"
        DungeonManager.dungeons['dark_tower'].description = "暗黒の力に満ちた塔。ドラゴンが待つ。"
    
    @staticmethod
    def get_dungeon(dungeon_id):
        """ダンジョンを取得"""
        return DungeonManager.dungeons.get(dungeon_id)
    
    @staticmethod
    def list_dungeons():
        """全ダンジョンをリスト表示"""
        print("\n" + "═" * 50)
        print("【利用可能なダンジョン】")
        print("═" * 50)
        
        for i, (key, dungeon) in enumerate(DungeonManager.dungeons.items(), 1):
            status = "✅ 訪問済み" if dungeon.visited else "🔒 未訪問"
            print(f"\n{i}. {dungeon.name} {status}")
            print(f"   難易度: {'★' * dungeon.difficulty}")
            print(f"   階層数: {dungeon.floors}階")
        
        print()


class DungeonExplorer:
    """ダンジョン探索システム"""
    
    def __init__(self, player):
        self.player = player
        self.current_dungeon = None
        self.current_floor = 0
        DungeonManager.setup_dungeons()
    
    def enter_dungeon(self, dungeon_id):
        """ダンジョンに入る"""
        dungeon = DungeonManager.get_dungeon(dungeon_id)
        if not dungeon:
            print("そのダンジョンは存在しません。")
            return False
        
        if self.player.hp < self.player.max_hp // 2:
            print("体力が不足しています。宿屋で回復してください。")
            return False
        
        self.current_dungeon = dungeon
        self.current_floor = 1
        dungeon.visited = True
        
        print(f"\n{'═' * 50}")
        print(f"🏰 {dungeon.name}に突入した！")
        print(f"{'═' * 50}")
        print(f"\n{dungeon.description}")
        print(f"\n1階層を進み始めた...")
        
        return True
    
    def show_floor_info(self):
        """階層情報を表示"""
        if not self.current_dungeon:
            return
        
        floor = DungeonFloor(self.current_floor, self.current_dungeon.name, 
                            self.current_dungeon.difficulty)
        
        print(f"\n{'─' * 50}")
        print(f"【{self.current_dungeon.name} {self.current_floor}階】")
        print(f"{'─' * 50}")
        print(f"{floor.show_description()}")
        print(f"\n敵の数: {len(floor.enemies)}体")
        print()
        
        return floor
    
    def advance_floor(self):
        """階層を進める"""
        if not self.current_dungeon:
            return False
        
        if self.current_floor >= self.current_dungeon.floors:
            self.dungeon_clear()
            return False
        
        self.current_floor += 1
        return True
    
    def dungeon_clear(self):
        """ダンジョンをクリア"""
        print(f"\n{'═' * 50}")
        print(f"🎉 {self.current_dungeon.name}をクリアした！")
        print(f"{'═' * 50}")
        
        # クリア報酬
        bonus_exp = 500 * self.current_dungeon.difficulty
        bonus_gold = 300 * self.current_dungeon.difficulty
        
        self.player.gain_experience(bonus_exp)
        self.player.gold += bonus_gold
        
        print(f"\n📊 クリア報酬:")
        print(f"   経験値 +{bonus_exp}")
        print(f"   ゴルド +{bonus_gold}")
        print(f"   (合計ゴルド: {self.player.gold})\n")
        
        self.current_dungeon = None
        self.current_floor = 0
    
    def escape_dungeon(self):
        """ダンジョンから脱出"""
        if not self.current_dungeon:
            return
        
        # 脱出確率: 階層が浅いほど成功しやすい
        escape_chance = 50 + (self.current_dungeon.floors - self.current_floor) * 5
        
        if random.random() * 100 < escape_chance:
            print(f"\n✓ {self.current_dungeon.name}から脱出した！")
            self.current_dungeon = None
            self.current_floor = 0
            return True
        else:
            print(f"\n✗ 脱出に失敗した！敵に遭遇してしまった！")
            return False
    
    def is_in_dungeon(self):
        """ダンジョンにいるか"""
        return self.current_dungeon is not None
    
    def get_dungeon_status(self):
        """ダンジョンの状態を表示"""
        if not self.current_dungeon:
            return
        
        progress = (self.current_floor / self.current_dungeon.floors) * 100
        
        print(f"\n【ダンジョン状態】")
        print(f"ダンジョン: {self.current_dungeon.name}")
        print(f"現在階層: {self.current_floor}/{self.current_dungeon.floors}")
        print(f"進行度: {progress:.0f}%")
        print()

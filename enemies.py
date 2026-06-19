"""
ドラゴンクエスト風RPG - 敵キャラクター拡張版
大幅に敵の種類を増加
"""

from character import Enemy
from skills import PoisonAttack, EnemySlash
import random


class EnemyFactory:
    """敵生成ファクトリー - 拡張版"""
    
    # 雑魚敵
    @staticmethod
    def create_slime():
        """スライム - 最弱敵"""
        enemy = Enemy("スライム", hp=20, mp=5, attack=8, defense=2, speed=5, 
                     exp_reward=50, gold_reward=30)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_blue_slime():
        """青いスライム"""
        enemy = Enemy("青いスライム", hp=25, mp=8, attack=10, defense=3, speed=6,
                     exp_reward=70, gold_reward=40)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_red_slime():
        """赤いスライム"""
        enemy = Enemy("赤いスライム", hp=30, mp=10, attack=12, defense=4, speed=7,
                     exp_reward=90, gold_reward=50)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_goblin():
        """ゴブリン"""
        enemy = Enemy("ゴブリン", hp=35, mp=10, attack=12, defense=4, speed=8,
                     exp_reward=100, gold_reward=60)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_hobgoblin():
        """ホブゴブリン - 強いゴブリン"""
        enemy = Enemy("ホブゴブリン", hp=50, mp=15, attack=18, defense=6, speed=10,
                     exp_reward=150, gold_reward=100)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_skeleton():
        """スケルトン"""
        enemy = Enemy("スケルトン", hp=40, mp=8, attack=15, defense=6, speed=9,
                     exp_reward=150, gold_reward=100)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_bone_knight():
        """ボーンナイト - 強いスケルトン"""
        enemy = Enemy("ボーンナイト", hp=60, mp=12, attack=22, defense=10, speed=11,
                     exp_reward=200, gold_reward=150)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_zombie():
        """ゾンビ"""
        enemy = Enemy("ゾンビ", hp=45, mp=5, attack=16, defense=8, speed=4,
                     exp_reward=160, gold_reward=80)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_mummy():
        """ミイラ - 強いゾンビ"""
        enemy = Enemy("ミイラ", hp=55, mp=10, attack=20, defense=10, speed=6,
                     exp_reward=210, gold_reward=120)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_orc():
        """オーク"""
        enemy = Enemy("オーク", hp=60, mp=8, attack=20, defense=7, speed=8,
                     exp_reward=180, gold_reward=110)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_orc_warrior():
        """オーク戦士 - 強いオーク"""
        enemy = Enemy("オーク戦士", hp=75, mp=12, attack=25, defense=9, speed=9,
                     exp_reward=240, gold_reward=160)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_bat():
        """コウモリ - 素早い敵"""
        enemy = Enemy("コウモリ", hp=15, mp=3, attack=7, defense=1, speed=12,
                     exp_reward=40, gold_reward=25)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_giant_bat():
        """ジャイアントバット - 大きなコウモリ"""
        enemy = Enemy("ジャイアントバット", hp=35, mp=8, attack=14, defense=4, speed=13,
                     exp_reward=120, gold_reward=70)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_spider():
        """クモ"""
        enemy = Enemy("クモ", hp=25, mp=5, attack=11, defense=3, speed=10,
                     exp_reward=80, gold_reward=45)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_giant_spider():
        """ジャイアントスパイダー - 大きなクモ"""
        enemy = Enemy("ジャイアントスパイダー", hp=50, mp=10, attack=18, defense=6, speed=11,
                     exp_reward=170, gold_reward=105)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_wolf():
        """狼"""
        enemy = Enemy("狼", hp=40, mp=6, attack=16, defense=5, speed=12,
                     exp_reward=140, gold_reward=85)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_dire_wolf():
        """ダイアウルフ - 大きな狼"""
        enemy = Enemy("ダイアウルフ", hp=65, mp=10, attack=23, defense=8, speed=13,
                     exp_reward=220, gold_reward=140)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    # ボスキャラクター
    @staticmethod
    def create_goblin_king():
        """ゴブリンキング - ボス敵"""
        enemy = Enemy("ゴブリンキング", hp=120, mp=30, attack=30, defense=15, speed=12,
                     exp_reward=500, gold_reward=400)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_skeleton_king():
        """スケルトンキング - ボス敵"""
        enemy = Enemy("スケルトンキング", hp=140, mp=40, attack=35, defense=18, speed=14,
                     exp_reward=600, gold_reward=500)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_dark_lord():
        """ダークロード - 最強ボス"""
        enemy = Enemy("ダークロード", hp=200, mp=50, attack=45, defense=20, speed=15,
                     exp_reward=1000, gold_reward=1000)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_dragon():
        """ドラゴン - 最終ボス"""
        enemy = Enemy("ドラゴン", hp=250, mp=60, attack=50, defense=25, speed=16,
                     exp_reward=1500, gold_reward=1500)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ダンジョン階層別敵生成
    @staticmethod
    def get_dungeon_enemies(floor):
        """ダンジョンの階層に応じた敵を取得"""
        enemy_map = {
            1: [EnemyFactory.create_slime, EnemyFactory.create_blue_slime,
                EnemyFactory.create_bat],
            2: [EnemyFactory.create_goblin, EnemyFactory.create_red_slime,
                EnemyFactory.create_spider],
            3: [EnemyFactory.create_hobgoblin, EnemyFactory.create_zombie,
                EnemyFactory.create_giant_bat],
            4: [EnemyFactory.create_skeleton, EnemyFactory.create_orc,
                EnemyFactory.create_giant_spider],
            5: [EnemyFactory.create_bone_knight, EnemyFactory.create_orc_warrior,
                EnemyFactory.create_wolf],
            6: [EnemyFactory.create_mummy, EnemyFactory.create_dire_wolf],
            7: [EnemyFactory.create_goblin_king],
            8: [EnemyFactory.create_skeleton_king],
            9: [EnemyFactory.create_dark_lord],
            10: [EnemyFactory.create_dragon]
        }
        
        enemies = enemy_map.get(floor, [EnemyFactory.create_slime])
        return random.choice(enemies)()
    
    @staticmethod
    def get_random_enemy():
        """ランダムな敵を取得"""
        enemies = [
            EnemyFactory.create_slime,
            EnemyFactory.create_blue_slime,
            EnemyFactory.create_goblin,
            EnemyFactory.create_skeleton,
            EnemyFactory.create_zombie,
            EnemyFactory.create_orc,
            EnemyFactory.create_bat,
            EnemyFactory.create_spider,
            EnemyFactory.create_wolf,
        ]
        return random.choice(enemies)()

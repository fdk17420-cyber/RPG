"""
ドラゴンクエスト風RPG - 敵キャラクター大幅拡張版（100種類以上）
"""

from character import Enemy
from skills import PoisonAttack, EnemySlash
import random


class EnemyFactory:
    """敵生成ファクトリー - 大幅拡張版"""
    
    # ===== 第1層：スライム系（10種類） =====
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
        """��いスライム"""
        enemy = Enemy("赤いスライム", hp=30, mp=10, attack=12, defense=4, speed=7,
                     exp_reward=90, gold_reward=50)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_green_slime():
        """緑のスライム"""
        enemy = Enemy("緑のスライム", hp=28, mp=12, attack=11, defense=3, speed=6,
                     exp_reward=80, gold_reward=45)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_yellow_slime():
        """黄色いスライム"""
        enemy = Enemy("黄色いスライム", hp=22, mp=15, attack=9, defense=2, speed=8,
                     exp_reward=75, gold_reward=42)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_purple_slime():
        """紫のスライム"""
        enemy = Enemy("紫のスライム", hp=32, mp=18, attack=13, defense=4, speed=7,
                     exp_reward=95, gold_reward=55)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_golden_slime():
        """金色のスライム"""
        enemy = Enemy("金色のスライム", hp=35, mp=20, attack=14, defense=5, speed=8,
                     exp_reward=150, gold_reward=200)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_black_slime():
        """黒いスライム"""
        enemy = Enemy("黒いスライム", hp=40, mp=25, attack=15, defense=6, speed=7,
                     exp_reward=120, gold_reward=70)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_slime_stack():
        """スライムスタック - 積み重なったスライム"""
        enemy = Enemy("スライムスタック", hp=50, mp=15, attack=18, defense=8, speed=5,
                     exp_reward=140, gold_reward=80)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_metal_slime():
        """メタルスライム - 稀な敵"""
        enemy = Enemy("メタルスライム", hp=10, mp=5, attack=5, defense=30, speed=20,
                     exp_reward=500, gold_reward=500)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    # ===== 第2層：ゴブリン系（12種類） =====
    @staticmethod
    def create_goblin():
        """ゴブリン"""
        enemy = Enemy("ゴブリン", hp=35, mp=10, attack=12, defense=4, speed=8,
                     exp_reward=100, gold_reward=60)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_goblin_soldier():
        """ゴブリン兵"""
        enemy = Enemy("ゴブリン兵", hp=40, mp=12, attack=14, defense=5, speed=8,
                     exp_reward=110, gold_reward=65)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_hobgoblin():
        """ホブゴブリン"""
        enemy = Enemy("ホブゴブリン", hp=50, mp=15, attack=18, defense=6, speed=10,
                     exp_reward=150, gold_reward=100)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_goblin_mage():
        """ゴブリン魔法使い"""
        enemy = Enemy("ゴブリン魔法使い", hp=38, mp=25, attack=10, defense=4, speed=9,
                     exp_reward=130, gold_reward=75)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_goblin_archer():
        """ゴブリン弓手"""
        enemy = Enemy("ゴブリン弓手", hp=35, mp=8, attack=16, defense=3, speed=12,
                     exp_reward=125, gold_reward=70)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_goblin_shaman():
        """ゴブリン呪術師"""
        enemy = Enemy("ゴブリン呪術師", hp=42, mp=30, attack=11, defense=5, speed=9,
                     exp_reward=140, gold_reward=85)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_goblin_berserker():
        """ゴブリン狂戦士"""
        enemy = Enemy("ゴブリン狂戦士", hp=55, mp=10, attack=22, defense=5, speed=10,
                     exp_reward=160, gold_reward=95)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_goblin_knight():
        """ゴブリン騎士"""
        enemy = Enemy("ゴブリン騎士", hp=60, mp=12, attack=19, defense=8, speed=9,
                     exp_reward=170, gold_reward=105)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_goblin_leader():
        """ゴブリンリーダー"""
        enemy = Enemy("ゴブリンリーダー", hp=65, mp=15, attack=20, defense=7, speed=10,
                     exp_reward=180, gold_reward=115)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_goblin_warlord():
        """ゴブリン軍将"""
        enemy = Enemy("ゴブリン軍将", hp=80, mp=20, attack=25, defense=9, speed=11,
                     exp_reward=220, gold_reward=140)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_goblin_king():
        """ゴブリンキング - ボス敵"""
        enemy = Enemy("ゴブリンキング", hp=120, mp=30, attack=30, defense=15, speed=12,
                     exp_reward=500, gold_reward=400)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_goblin_emperor():
        """ゴブリン皇帝 - 超強敵"""
        enemy = Enemy("ゴブリン皇帝", hp=150, mp=40, attack=35, defense=18, speed=13,
                     exp_reward=700, gold_reward=600)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ===== 第3層：スケルトン系（12種類） =====
    @staticmethod
    def create_skeleton():
        """スケルトン"""
        enemy = Enemy("スケルトン", hp=40, mp=8, attack=15, defense=6, speed=9,
                     exp_reward=150, gold_reward=100)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_skeleton_warrior():
        """スケルトン戦士"""
        enemy = Enemy("スケルトン戦士", hp=48, mp=10, attack=17, defense=7, speed=9,
                     exp_reward=160, gold_reward=110)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_bone_knight():
        """ボーンナイト"""
        enemy = Enemy("ボーンナイト", hp=60, mp=12, attack=22, defense=10, speed=11,
                     exp_reward=200, gold_reward=150)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_skeleton_mage():
        """スケルトン魔法使い"""
        enemy = Enemy("スケルトン魔法使い", hp=45, mp=20, attack=12, defense=6, speed=10,
                     exp_reward=170, gold_reward=120)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_skeleton_archer():
        """スケルトン弓手"""
        enemy = Enemy("スケルトン弓手", hp=42, mp=8, attack=18, defense=5, speed=13,
                     exp_reward=165, gold_reward=115)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_bone_shield():
        """ボーンシールド - 防御特化"""
        enemy = Enemy("ボーンシールド", hp=70, mp=10, attack=14, defense=15, speed=8,
                     exp_reward=180, gold_reward=125)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_bone_guardian():
        """ボーンガーディアン"""
        enemy = Enemy("ボーンガーディアン", hp=75, mp=15, attack=20, defense=12, speed=9,
                     exp_reward=210, gold_reward=155)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_cursed_skeleton():
        """呪われたスケルトン"""
        enemy = Enemy("呪われたスケルトン", hp=55, mp=25, attack=16, defense=7, speed=10,
                     exp_reward=190, gold_reward=135)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_bone_commander():
        """ボーンコマンダー"""
        enemy = Enemy("ボーンコマンダー", hp=80, mp=18, attack=24, defense=11, speed=11,
                     exp_reward=230, gold_reward=170)
        enemy.skills = [EnemySlash()]
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
    def create_bone_emperor():
        """ボーン皇帝 - 超強敵"""
        enemy = Enemy("ボーン皇帝", hp=170, mp=50, attack=40, defense=20, speed=15,
                     exp_reward=800, gold_reward=700)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ===== 第4層：ゾンビ系（10種類） =====
    @staticmethod
    def create_zombie():
        """ゾンビ"""
        enemy = Enemy("ゾンビ", hp=45, mp=5, attack=16, defense=8, speed=4,
                     exp_reward=160, gold_reward=80)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_rotten_zombie():
        """腐ったゾンビ"""
        enemy = Enemy("腐ったゾンビ", hp=50, mp=8, attack=17, defense=9, speed=4,
                     exp_reward=170, gold_reward=90)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_mummy():
        """ミイラ"""
        enemy = Enemy("ミイラ", hp=55, mp=10, attack=20, defense=10, speed=6,
                     exp_reward=210, gold_reward=120)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_zombie_knight():
        """ゾンビ騎士"""
        enemy = Enemy("ゾンビ騎士", hp=65, mp=12, attack=22, defense=11, speed=6,
                     exp_reward=240, gold_reward=150)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_zombie_archer():
        """ゾンビ弓手"""
        enemy = Enemy("ゾンビ弓手", hp=48, mp=8, attack=19, defense=7, speed=8,
                     exp_reward=195, gold_reward=110)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_zombie_mage():
        """ゾンビ魔法使い"""
        enemy = Enemy("ゾンビ魔法使い", hp=52, mp=22, attack=14, defense=8, speed=7,
                     exp_reward=215, gold_reward=130)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_plague_zombie():
        """疫病ゾンビ"""
        enemy = Enemy("疫病ゾンビ", hp=58, mp=15, attack=18, defense=9, speed=5,
                     exp_reward=225, gold_reward=140)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_zombie_lord():
        """ゾンビロード"""
        enemy = Enemy("ゾンビロード", hp=85, mp=25, attack=28, defense=12, speed=8,
                     exp_reward=290, gold_reward=200)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_zombie_king():
        """ゾンビキング"""
        enemy = Enemy("ゾンビキング", hp=110, mp=35, attack=32, defense=14, speed=9,
                     exp_reward=400, gold_reward=300)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ===== 第5層：オーク系（12種類） =====
    @staticmethod
    def create_orc():
        """オーク"""
        enemy = Enemy("オーク", hp=60, mp=8, attack=20, defense=7, speed=8,
                     exp_reward=180, gold_reward=110)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_orc_soldier():
        """オーク兵"""
        enemy = Enemy("オーク兵", hp=65, mp=10, attack=22, defense=8, speed=8,
                     exp_reward=195, gold_reward=125)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_orc_warrior():
        """オーク戦士"""
        enemy = Enemy("オーク戦士", hp=75, mp=12, attack=25, defense=9, speed=9,
                     exp_reward=240, gold_reward=160)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_orc_berserker():
        """オーク狂戦士"""
        enemy = Enemy("オーク狂戦士", hp=85, mp=10, attack=30, defense=8, speed=10,
                     exp_reward=270, gold_reward=180)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_orc_shaman():
        """オーク呪術師"""
        enemy = Enemy("オーク呪術師", hp=70, mp=28, attack=16, defense=8, speed=9,
                     exp_reward=230, gold_reward=150)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_orc_archer():
        """オーク弓手"""
        enemy = Enemy("オーク弓手", hp=62, mp=8, attack=23, defense=6, speed=11,
                     exp_reward=215, gold_reward=140)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_orc_knight():
        """オーク騎士"""
        enemy = Enemy("オーク騎士", hp=80, mp=12, attack=26, defense=11, speed=9,
                     exp_reward=260, gold_reward=170)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_orc_commander():
        """オーク司令官"""
        enemy = Enemy("オーク司令官", hp=95, mp=18, attack=28, defense=12, speed=10,
                     exp_reward=310, gold_reward=210)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_orc_warlord():
        """オーク軍将"""
        enemy = Enemy("オーク軍将", hp=110, mp=22, attack=32, defense=13, speed=11,
                     exp_reward=360, gold_reward=250)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_orc_king():
        """オークキング"""
        enemy = Enemy("オークキング", hp=135, mp=30, attack=37, defense=15, speed=12,
                     exp_reward=550, gold_reward=450)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_orc_emperor():
        """オーク皇帝"""
        enemy = Enemy("オーク皇帝", hp=160, mp=40, attack=42, defense=18, speed=13,
                     exp_reward=750, gold_reward=600)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ===== 第6層：飛行敵（10種類） =====
    @staticmethod
    def create_bat():
        """コウモリ"""
        enemy = Enemy("コウモリ", hp=15, mp=3, attack=7, defense=1, speed=12,
                     exp_reward=40, gold_reward=25)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_giant_bat():
        """ジャイアントバット"""
        enemy = Enemy("ジャイアントバット", hp=35, mp=8, attack=14, defense=4, speed=13,
                     exp_reward=120, gold_reward=70)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_vampire_bat():
        """ヴァンパイアバット"""
        enemy = Enemy("ヴァンパイアバット", hp=45, mp=12, attack=18, defense=6, speed=14,
                     exp_reward=180, gold_reward=120)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_harpy():
        """ハーピー"""
        enemy = Enemy("ハーピー", hp=38, mp=10, attack=16, defense=5, speed=15,
                     exp_reward=140, gold_reward=85)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_wyvern():
        """ワイバーン"""
        enemy = Enemy("ワイバーン", hp=70, mp=15, attack=25, defense=10, speed=13,
                     exp_reward=280, gold_reward=180)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_phoenix():
        """フェニックス"""
        enemy = Enemy("フェニックス", hp=85, mp=25, attack=28, defense=12, speed=14,
                     exp_reward=350, gold_reward=250)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_griffin():
        """グリフォン"""
        enemy = Enemy("グリフォン", hp=90, mp=18, attack=30, defense=13, speed=12,
                     exp_reward=380, gold_reward=280)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_pegasus():
        """ペガサス"""
        enemy = Enemy("ペガサス", hp=95, mp=20, attack=32, defense=12, speed=16,
                     exp_reward=420, gold_reward=320)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_dragon_wyvern():
        """ドラゴンワイバーン"""
        enemy = Enemy("ドラゴンワイバーン", hp=120, mp=30, attack=38, defense=16, speed=14,
                     exp_reward=550, gold_reward=450)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ===== 第7層：爬虫類系（10種類） =====
    @staticmethod
    def create_spider():
        """クモ"""
        enemy = Enemy("クモ", hp=25, mp=5, attack=11, defense=3, speed=10,
                     exp_reward=80, gold_reward=45)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_giant_spider():
        """ジャイアントスパイダー"""
        enemy = Enemy("ジャイアントスパイダー", hp=50, mp=10, attack=18, defense=6, speed=11,
                     exp_reward=170, gold_reward=105)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_cave_spider():
        """洞窟蜘蛛"""
        enemy = Enemy("洞窟蜘蛛", hp=60, mp=12, attack=20, defense=8, speed=12,
                     exp_reward=210, gold_reward=140)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_scorpion():
        """サソリ"""
        enemy = Enemy("サソリ", hp=42, mp=8, attack=16, defense=7, speed=9,
                     exp_reward=130, gold_reward=75)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_giant_scorpion():
        """巨大サソリ"""
        enemy = Enemy("巨大サソリ", hp=65, mp=12, attack=22, defense=9, speed=10,
                     exp_reward=230, gold_reward=150)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_basilisk():
        """バジリスク"""
        enemy = Enemy("バジリスク", hp=75, mp=18, attack=25, defense=11, speed=11,
                     exp_reward=280, gold_reward=180)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_snake_lord():
        """ヘビ王"""
        enemy = Enemy("ヘビ王", hp=95, mp=25, attack=30, defense=12, speed=12,
                     exp_reward=360, gold_reward=260)
        enemy.skills = [PoisonAttack(), EnemySlash()]
        return enemy
    
    @staticmethod
    def create_medusa():
        """メデューサ"""
        enemy = Enemy("メデューサ", hp=80, mp=28, attack=24, defense=10, speed=11,
                     exp_reward=320, gold_reward=220)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_hydra():
        """ヒドラ"""
        enemy = Enemy("ヒドラ", hp=140, mp=35, attack=38, defense=16, speed=12,
                     exp_reward=650, gold_reward=550)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ===== 第8層：獣系（12種類） =====
    @staticmethod
    def create_wolf():
        """狼"""
        enemy = Enemy("狼", hp=40, mp=6, attack=16, defense=5, speed=12,
                     exp_reward=140, gold_reward=85)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_dire_wolf():
        """ダイアウルフ"""
        enemy = Enemy("ダイアウルフ", hp=65, mp=10, attack=23, defense=8, speed=13,
                     exp_reward=220, gold_reward=140)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_werewolf():
        """ウェアウルフ"""
        enemy = Enemy("ウェアウルフ", hp=80, mp=12, attack=28, defense=10, speed=14,
                     exp_reward=300, gold_reward=200)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_bear():
        """熊"""
        enemy = Enemy("熊", hp=75, mp=8, attack=24, defense=9, speed=9,
                     exp_reward=250, gold_reward=160)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_dire_bear():
        """ダイアベアー"""
        enemy = Enemy("ダイアベアー", hp=95, mp=10, attack=30, defense=12, speed=10,
                     exp_reward=340, gold_reward=240)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_lion():
        """ライオン"""
        enemy = Enemy("ライオン", hp=70, mp=8, attack=26, defense=9, speed=12,
                     exp_reward=260, gold_reward=170)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_tiger():
        """虎"""
        enemy = Enemy("虎", hp=72, mp=8, attack=27, defense=8, speed=13,
                     exp_reward=270, gold_reward=180)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_behemoth():
        """ベヒーモス"""
        enemy = Enemy("ベヒーモス", hp=120, mp=15, attack=35, defense=14, speed=10,
                     exp_reward=450, gold_reward=350)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_chimera():
        """キメラ"""
        enemy = Enemy("キメラ", hp=110, mp=20, attack=32, defense=13, speed=12,
                     exp_reward=480, gold_reward=380)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_cerberus():
        """ケルベロス"""
        enemy = Enemy("ケルベロス", hp=130, mp=25, attack=36, defense=15, speed=13,
                     exp_reward=600, gold_reward=500)
        enemy.skills = [EnemySlash(), PoisonAttack()]
        enemy.is_boss = True
        return enemy
    
    # ===== 第9層：魔族系（15種類） =====
    @staticmethod
    def create_imp():
        """インプ - 小悪魔"""
        enemy = Enemy("インプ", hp=30, mp=15, attack=10, defense=4, speed=11,
                     exp_reward=100, gold_reward=60)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_demon():
        """デーモン"""
        enemy = Enemy("デーモン", hp=65, mp=25, attack=22, defense=9, speed=11,
                     exp_reward=220, gold_reward=150)
        enemy.skills = [PoisonAttack(), EnemySlash()]
        return enemy
    
    @staticmethod
    def create_succubus():
        """サキュバス"""
        enemy = Enemy("サキュバス", hp=60, mp=30, attack=18, defense=8, speed=12,
                     exp_reward=210, gold_reward=140)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_incubus():
        """インキュバス"""
        enemy = Enemy("インキュバス", hp=62, mp=28, attack=20, defense=8, speed=12,
                     exp_reward=220, gold_reward=145)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_devil():
        """デビル"""
        enemy = Enemy("デビル", hp=85, mp=35, attack=28, defense=11, speed=12,
                     exp_reward=300, gold_reward=220)
        enemy.skills = [PoisonAttack(), EnemySlash()]
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
    
    # ===== その他の特別な敵（10種類） =====
    @staticmethod
    def create_golem():
        """ゴーレム"""
        enemy = Enemy("ゴーレム", hp=100, mp=5, attack=26, defense=18, speed=6,
                     exp_reward=350, gold_reward=250)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_stone_golem():
        """石のゴーレム"""
        enemy = Enemy("石のゴーレム", hp=120, mp=8, attack=28, defense=20, speed=7,
                     exp_reward=400, gold_reward=300)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_iron_golem():
        """鉄のゴーレム"""
        enemy = Enemy("鉄のゴーレム", hp=140, mp=10, attack=32, defense=22, speed=8,
                     exp_reward=500, gold_reward=400)
        enemy.skills = [EnemySlash()]
        return enemy
    
    @staticmethod
    def create_wizard():
        """魔法使い"""
        enemy = Enemy("魔法使い", hp=50, mp=40, attack=12, defense=6, speed=10,
                     exp_reward=180, gold_reward=120)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_lich():
        """リッチ - 不死の魔法使い"""
        enemy = Enemy("リッチ", hp=100, mp=60, attack=20, defense=12, speed=11,
                     exp_reward=450, gold_reward=350)
        enemy.skills = [PoisonAttack(), EnemySlash()]
        enemy.is_boss = True
        return enemy
    
    @staticmethod
    def create_cultist():
        """カルト信者"""
        enemy = Enemy("カルト信者", hp=48, mp=20, attack=14, defense=6, speed=9,
                     exp_reward=130, gold_reward=80)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_witch():
        """魔女"""
        enemy = Enemy("魔女", hp=55, mp=35, attack=16, defense=7, speed=10,
                     exp_reward=160, gold_reward=110)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_sorcerer():
        """魔術師"""
        enemy = Enemy("魔術師", hp=62, mp=42, attack=18, defense=8, speed=11,
                     exp_reward=200, gold_reward=140)
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_warlock():
        """ウォーロック"""
        enemy = Enemy("ウォーロック", hp=80, mp=50, attack=24, defense=10, speed=12,
                     exp_reward=300, gold_reward=220)
        enemy.skills = [PoisonAttack(), EnemySlash()]
        return enemy
    
    @staticmethod
    def create_archmage():
        """大魔法使い"""
        enemy = Enemy("大魔法使い", hp=110, mp=70, attack=30, defense=12, speed=13,
                     exp_reward=520, gold_reward=420)
        enemy.skills = [PoisonAttack(), EnemySlash()]
        enemy.is_boss = True
        return enemy
    
    # ===== ダンジョン階層別敵生成 =====
    @staticmethod
    def get_dungeon_enemies(floor):
        """ダンジョンの階層に応じた敵を取得"""
        enemy_map = {
            1: [EnemyFactory.create_slime, EnemyFactory.create_blue_slime,
                EnemyFactory.create_bat, EnemyFactory.create_green_slime,
                EnemyFactory.create_yellow_slime],
            2: [EnemyFactory.create_goblin, EnemyFactory.create_red_slime,
                EnemyFactory.create_spider, EnemyFactory.create_giant_bat,
                EnemyFactory.create_goblin_soldier],
            3: [EnemyFactory.create_hobgoblin, EnemyFactory.create_zombie,
                EnemyFactory.create_giant_spider, EnemyFactory.create_orc,
                EnemyFactory.create_skeleton],
            4: [EnemyFactory.create_skeleton_warrior, EnemyFactory.create_orc_warrior,
                EnemyFactory.create_mummy, EnemyFactory.create_giant_scorpion,
                EnemyFactory.create_bone_knight],
            5: [EnemyFactory.create_orc_berserker, EnemyFactory.create_wyvern,
                EnemyFactory.create_basilisk, EnemyFactory.create_vampire_bat,
                EnemyFactory.create_werewolf],
            6: [EnemyFactory.create_goblin_warlord, EnemyFactory.create_griffin,
                EnemyFactory.create_medusa, EnemyFactory.create_behemoth,
                EnemyFactory.create_demon],
            7: [EnemyFactory.create_goblin_king, EnemyFactory.create_chimera,
                EnemyFactory.create_hydra, EnemyFactory.create_devil,
                EnemyFactory.create_phoenix],
            8: [EnemyFactory.create_skeleton_king, EnemyFactory.create_cerberus,
                EnemyFactory.create_iron_golem, EnemyFactory.create_lich,
                EnemyFactory.create_archmage],
            9: [EnemyFactory.create_dark_lord, EnemyFactory.create_dragon_wyvern,
                EnemyFactory.create_dragon, EnemyFactory.create_behemoth,
                EnemyFactory.create_warlock],
            10: [EnemyFactory.create_dragon]
        }
        
        enemies = enemy_map.get(floor, [EnemyFactory.create_slime])
        return random.choice(enemies)()
    
    @staticmethod
    def get_random_enemy():
        """ランダムな敵を取得"""
        enemies = [
            EnemyFactory.create_slime, EnemyFactory.create_blue_slime,
            EnemyFactory.create_goblin, EnemyFactory.create_skeleton,
            EnemyFactory.create_zombie, EnemyFactory.create_orc,
            EnemyFactory.create_bat, EnemyFactory.create_spider,
            EnemyFactory.create_wolf, EnemyFactory.create_harpy,
            EnemyFactory.create_scorpion, EnemyFactory.create_imp,
            EnemyFactory.create_demon, EnemyFactory.create_wizard,
            EnemyFactory.create_werewolf, EnemyFactory.create_wyvern,
        ]
        return random.choice(enemies)()
    
    @staticmethod
    def get_all_enemies():
        """全ての敵を取得（リスト）"""
        return [
            # スライム系
            EnemyFactory.create_slime, EnemyFactory.create_blue_slime,
            EnemyFactory.create_red_slime, EnemyFactory.create_green_slime,
            EnemyFactory.create_yellow_slime, EnemyFactory.create_purple_slime,
            EnemyFactory.create_golden_slime, EnemyFactory.create_black_slime,
            EnemyFactory.create_slime_stack, EnemyFactory.create_metal_slime,
            # ゴブリン系
            EnemyFactory.create_goblin, EnemyFactory.create_goblin_soldier,
            EnemyFactory.create_hobgoblin, EnemyFactory.create_goblin_mage,
            EnemyFactory.create_goblin_archer, EnemyFactory.create_goblin_shaman,
            EnemyFactory.create_goblin_berserker, EnemyFactory.create_goblin_knight,
            EnemyFactory.create_goblin_leader, EnemyFactory.create_goblin_warlord,
            EnemyFactory.create_goblin_king, EnemyFactory.create_goblin_emperor,
            # スケルトン系
            EnemyFactory.create_skeleton, EnemyFactory.create_skeleton_warrior,
            EnemyFactory.create_bone_knight, EnemyFactory.create_skeleton_mage,
            EnemyFactory.create_skeleton_archer, EnemyFactory.create_bone_shield,
            EnemyFactory.create_bone_guardian, EnemyFactory.create_cursed_skeleton,
            EnemyFactory.create_bone_commander, EnemyFactory.create_skeleton_king,
            EnemyFactory.create_bone_emperor,
            # ゾンビ系
            EnemyFactory.create_zombie, EnemyFactory.create_rotten_zombie,
            EnemyFactory.create_mummy, EnemyFactory.create_zombie_knight,
            EnemyFactory.create_zombie_archer, EnemyFactory.create_zombie_mage,
            EnemyFactory.create_plague_zombie, EnemyFactory.create_zombie_lord,
            EnemyFactory.create_zombie_king,
            # オーク系
            EnemyFactory.create_orc, EnemyFactory.create_orc_soldier,
            EnemyFactory.create_orc_warrior, EnemyFactory.create_orc_berserker,
            EnemyFactory.create_orc_shaman, EnemyFactory.create_orc_archer,
            EnemyFactory.create_orc_knight, EnemyFactory.create_orc_commander,
            EnemyFactory.create_orc_warlord, EnemyFactory.create_orc_king,
            EnemyFactory.create_orc_emperor,
            # 飛行敵
            EnemyFactory.create_bat, EnemyFactory.create_giant_bat,
            EnemyFactory.create_vampire_bat, EnemyFactory.create_harpy,
            EnemyFactory.create_wyvern, EnemyFactory.create_phoenix,
            EnemyFactory.create_griffin, EnemyFactory.create_pegasus,
            EnemyFactory.create_dragon_wyvern,
            # 爬虫類系
            EnemyFactory.create_spider, EnemyFactory.create_giant_spider,
            EnemyFactory.create_cave_spider, EnemyFactory.create_scorpion,
            EnemyFactory.create_giant_scorpion, EnemyFactory.create_basilisk,
            EnemyFactory.create_snake_lord, EnemyFactory.create_medusa,
            EnemyFactory.create_hydra,
            # 獣系
            EnemyFactory.create_wolf, EnemyFactory.create_dire_wolf,
            EnemyFactory.create_werewolf, EnemyFactory.create_bear,
            EnemyFactory.create_dire_bear, EnemyFactory.create_lion,
            EnemyFactory.create_tiger, EnemyFactory.create_behemoth,
            EnemyFactory.create_chimera, EnemyFactory.create_cerberus,
            # 魔族・その他
            EnemyFactory.create_imp, EnemyFactory.create_demon,
            EnemyFactory.create_succubus, EnemyFactory.create_incubus,
            EnemyFactory.create_devil, EnemyFactory.create_dark_lord,
            EnemyFactory.create_dragon, EnemyFactory.create_golem,
            EnemyFactory.create_stone_golem, EnemyFactory.create_iron_golem,
            EnemyFactory.create_wizard, EnemyFactory.create_lich,
            EnemyFactory.create_cultist, EnemyFactory.create_witch,
            EnemyFactory.create_sorcerer, EnemyFactory.create_warlock,
            EnemyFactory.create_archmage,
        ]

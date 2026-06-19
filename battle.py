"""
ドラゴンクエスト風RPG - ターンベース戦闘システム
"""

import random
from character import Enemy


class Battle:
    """戦闘システムクラス"""
    
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0
        self.battle_log = []
    
    def determine_turn_order(self):
        """素早さで行動順序を決定"""
        player_speed = self.player.speed + random.randint(-5, 5)
        enemy_speed = self.enemy.speed + random.randint(-5, 5)
        return player_speed >= enemy_speed
    
    def start_battle(self):
        """戦闘開始"""
        print("\n" + "="*50)
        print(f"⚔️  {self.enemy.name} が現れた！")
        print("="*50)
        print(f"\n敵: {self.enemy.name}")
        print(f"  HP: {self.enemy.hp}/{self.enemy.max_hp}")
        print(f"  攻撃力: {self.enemy.attack}, 防御力: {self.enemy.defense}\n")
    
    def show_status(self):
        """戦闘中のステータス表示"""
        print(f"\n{'─'*50}")
        print(f"勇者: HP {self.player.hp}/{self.player.max_hp} | MP {self.player.mp}/{self.player.max_mp}")
        print(f"{self.enemy.name}: HP {self.enemy.hp}/{self.enemy.max_hp}")
        print(f"{'─'*50}\n")
    
    def player_turn(self):
        """プレイヤーのターン"""
        print(f"\n【{self.player.name}のターン】")
        
        while True:
            print("\nアクションを選択してください:")
            print("1. 通常攻撃")
            print("2. スキル/魔法")
            print("3. ステータス確認")
            
            choice = input("\n> ").strip()
            
            if choice == '1':
                return self.player_normal_attack()
            elif choice == '2':
                result = self.player_use_skill()
                if result is not None:
                    return result
            elif choice == '3':
                print(self.player.show_status())
            else:
                print("無効な選択です。もう一度選んでください。")
    
    def player_normal_attack(self):
        """プレイヤーの通常攻撃"""
        damage = self.player.attack + random.randint(-3, 3)
        actual_damage = self.enemy.take_damage(damage)
        
        message = f"{self.player.name}は{self.enemy.name}を攻撃した！\n"
        message += f"{self.enemy.name}に{actual_damage}のダメージ！"
        print(f"\n✨ {message}")
        return True
    
    def player_use_skill(self):
        """プレイヤーがスキルを使用"""
        available_skills = self.player.get_available_skills()
        
        if not available_skills:
            print("\n使用可能なスキルがありません！")
            return None
        
        print("\n【スキル選択】")
        for i, skill in enumerate(available_skills, 1):
            print(f"{i}. {skill.name} (MP消費: {skill.mp_cost})")
        print(f"{len(available_skills) + 1}. キャンセル")
        
        try:
            choice = int(input("\n> ").strip())
            if choice == len(available_skills) + 1:
                return None
            if 1 <= choice <= len(available_skills):
                skill = available_skills[choice - 1]
                message = skill.use(self.player, self.enemy)
                print(f"\n✨ {message}")
                return True
            else:
                print("無効な選択です。")
                return None
        except ValueError:
            print("数字を入力してください。")
            return None
    
    def enemy_turn(self):
        """敵のターン"""
        print(f"\n【{self.enemy.name}のターン】")
        
        action_type, skill = self.enemy.get_action()
        
        if action_type == 'attack':
            self.enemy_normal_attack()
        elif action_type == 'skill' and skill:
            self.enemy_use_skill(skill)
    
    def enemy_normal_attack(self):
        """敵の通常攻撃"""
        damage = self.enemy.attack + random.randint(-3, 3)
        actual_damage = self.player.take_damage(damage)
        
        message = f"{self.enemy.name}は{self.player.name}を攻撃した！\n"
        message += f"{self.player.name}に{actual_damage}のダメージ！"
        print(f"\n💥 {message}")
    
    def enemy_use_skill(self, skill):
        """敵がスキルを使用"""
        message = skill.use(self.enemy, self.player)
        print(f"\n💥 {message}")
    
    def check_battle_end(self):
        """戦闘終了条件をチェック"""
        if not self.player.is_alive:
            return 'lose'
        elif not self.enemy.is_alive:
            return 'win'
        return None
    
    def end_battle(self, result):
        """戦闘終了処理"""
        print("\n" + "="*50)
        
        if result == 'win':
            print(f"🎉 {self.enemy.name}を倒した！")
            print("="*50)
            
            exp = self.enemy.exp_reward
            gold = self.enemy.gold_reward
            
            self.player.gain_experience(exp)
            self.player.gold += gold
            
            print(f"\n📊 戦闘結果:")
            print(f"   経験値 +{exp}")
            print(f"   ゴルド +{gold}")
            print(f"   (合計ゴルド: {self.player.gold})")
            
            if self.player.hp < self.player.max_hp:
                self.player.heal(int(self.player.max_hp * 0.5))
                print(f"\n💚 戦闘後にHP が少し回復した！")
        
        elif result == 'lose':
            print(f"😢 {self.player.name}は倒された...")
            print("="*50)
            print(f"\nゲームオーバー")
        
        print()
    
    def execute_battle(self):
        """戦闘を実行"""
        self.start_battle()
        player_first = self.determine_turn_order()
        
        while True:
            self.show_status()
            
            if player_first:
                self.player_turn()
                result = self.check_battle_end()
                if result:
                    self.end_battle(result)
                    return result
                
                self.enemy_turn()
                result = self.check_battle_end()
                if result:
                    self.end_battle(result)
                    return result
            else:
                self.enemy_turn()
                result = self.check_battle_end()
                if result:
                    self.end_battle(result)
                    return result
                
                self.player_turn()
                result = self.check_battle_end()
                if result:
                    self.end_battle(result)
                    return result
            
            self.turn += 1


class BattleFactory:
    """敵生成ファクトリー"""
    
    @staticmethod
    def create_slime():
        """スライムを生成"""
        from skills import PoisonAttack
        enemy = Enemy(
            name="スライム",
            hp=20,
            mp=5,
            attack=8,
            defense=2,
            speed=5,
            exp_reward=50,
            gold_reward=30
        )
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_goblin():
        """ゴブリンを生成"""
        from skills import PoisonAttack
        enemy = Enemy(
            name="ゴブリン",
            hp=35,
            mp=10,
            attack=12,
            defense=4,
            speed=8,
            exp_reward=100,
            gold_reward=60
        )
        enemy.skills = [PoisonAttack()]
        return enemy
    
    @staticmethod
    def create_skeleton():
        """スケルトンを生成"""
        enemy = Enemy(
            name="スケルトン",
            hp=40,
            mp=8,
            attack=15,
            defense=6,
            speed=9,
            exp_reward=150,
            gold_reward=100
        )
        return enemy
    
    @staticmethod
    def get_random_enemy():
        """ランダムな敵を取得"""
        enemies = [
            BattleFactory.create_slime,
            BattleFactory.create_goblin,
            BattleFactory.create_skeleton
        ]
        return random.choice(enemies)()

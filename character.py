"""
ドラゴンクエスト風RPG - キャラクタークラス定義
"""

class Character:
    """キャラクター基本クラス"""
    
    def __init__(self, name, hp, mp, attack, defense, speed, level=1):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.is_alive = True
        self.experience = 0
    
    def take_damage(self, damage):
        """ダメージを受ける"""
        actual_damage = max(1, damage - self.defense // 2)
        self.hp -= actual_damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
        return actual_damage
    
    def heal(self, amount):
        """HPを回復する"""
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - old_hp
    
    def recover_mp(self, amount):
        """MPを回復する"""
        old_mp = self.mp
        self.mp = min(self.max_mp, self.mp + amount)
        return self.mp - old_mp
    
    def use_mp(self, amount):
        """MPを消費する"""
        if self.mp >= amount:
            self.mp -= amount
            return True
        return False
    
    def gain_experience(self, amount):
        """経験値を獲得する"""
        self.experience += amount
        if self.experience >= 100 * self.level:
            self.level_up()
    
    def level_up(self):
        """レベルアップ"""
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mp += 10
        self.mp = self.max_mp
        self.attack += 5
        self.defense += 3
        self.speed += 2
        print(f"\n🎉 {self.name} がレベルアップ！ レベル {self.level} になった！")
        print(f"   HP: +20 ({self.max_hp}), MP: +10 ({self.max_mp})")
        print(f"   攻撃力: +5 ({self.attack}), 防御力: +3 ({self.defense})\n")
    
    def show_status(self):
        """ステータス表示"""
        status = f"""
━━━━━━━━━━━━━━━━━━━━━━
{self.name} のステータス
━━━━━━━━━━━━━━━━━━━━━━
Lv. {self.level}
HP: {self.hp}/{self.max_hp}
MP: {self.mp}/{self.max_mp}
攻撃力: {self.attack}
防御力: {self.defense}
素早さ: {self.speed}
経験値: {self.experience}/{100 * self.level}
━━━━━━━━━━━━━━━━━━━━━━
"""
        return status


class Player(Character):
    """プレイヤークラス（勇者）"""
    
    def __init__(self, name="勇者"):
        super().__init__(
            name=name,
            hp=50,
            mp=20,
            attack=15,
            defense=8,
            speed=10,
            level=1
        )
        self.gold = 0
        self.skills = []
    
    def add_skill(self, skill):
        """スキルを習得する"""
        self.skills.append(skill)
    
    def get_available_skills(self):
        """使用可能なスキルを返す"""
        return [s for s in self.skills if s.can_use(self)]


class Enemy(Character):
    """敵キャラクタークラス"""
    
    def __init__(self, name, hp, mp, attack, defense, speed, exp_reward, gold_reward):
        super().__init__(name, hp, mp, attack, defense, speed)
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
    
    def get_action(self):
        """敵のアクションを決定する（簡易AI）"""
        import random
        
        # スキルの使用確率（30%）
        if random.random() < 0.3 and hasattr(self, 'skills'):
            usable_skills = [s for s in self.skills if s.can_use(self)]
            if usable_skills:
                return ('skill', random.choice(usable_skills))
        
        # 通常攻撃
        return ('attack', None)

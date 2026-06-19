"""
ドラゴンクエスト風RPG - スキル・魔法システム
"""

import random


class Skill:
    """スキル基本クラス"""
    
    def __init__(self, name, mp_cost, power, effect_type='damage'):
        self.name = name
        self.mp_cost = mp_cost
        self.power = power
        self.effect_type = effect_type  # 'damage', 'heal', 'debuff'
    
    def can_use(self, character):
        """スキルを使用可能か判定"""
        return character.mp >= self.mp_cost
    
    def use(self, user, target):
        """スキルを使用する"""
        if not self.can_use(user):
            return None
        
        user.use_mp(self.mp_cost)
        
        if self.effect_type == 'damage':
            return self.damage_effect(user, target)
        elif self.effect_type == 'heal':
            return self.heal_effect(user, target)
        elif self.effect_type == 'debuff':
            return self.debuff_effect(user, target)
    
    def damage_effect(self, user, target):
        """ダメージ効果"""
        damage = user.attack + self.power + random.randint(-5, 5)
        actual_damage = target.take_damage(damage)
        return f"{user.name}は{self.name}を放った！\n{target.name}に{actual_damage}のダメージ！"
    
    def heal_effect(self, user, target):
        """回復効果"""
        amount = self.power + random.randint(0, 10)
        healed = target.heal(amount)
        return f"{user.name}は{self.name}を唱えた！\n{target.name}のHPが{healed}回復した！"
    
    def debuff_effect(self, user, target):
        """デバフ効果"""
        damage = user.attack + self.power + random.randint(-3, 3)
        actual_damage = target.take_damage(damage)
        return f"{user.name}は{self.name}を唱えた！\n{target.name}に{actual_damage}のダメージを与えた！"


# 勇者のスキル
class Slash(Skill):
    """斬撃 - 基本スキル"""
    def __init__(self):
        super().__init__("斬撃", mp_cost=0, power=10, effect_type='damage')


class PowerSlash(Skill):
    """パワースラッシュ - 強力な攻撃"""
    def __init__(self):
        super().__init__("パワースラッシュ", mp_cost=8, power=20, effect_type='damage')


class Heal(Skill):
    """ホイミ - HP回復"""
    def __init__(self):
        super().__init__("ホイミ", mp_cost=5, power=30, effect_type='heal')


class GreatHeal(Skill):
    """ベホイミ - 大回復"""
    def __init__(self):
        super().__init__("ベホイミ", mp_cost=15, power=80, effect_type='heal')


class IceStrike(Skill):
    """イオ - 氷の魔法"""
    def __init__(self):
        super().__init__("イオ", mp_cost=10, power=25, effect_type='damage')


class Lightning(Skill):
    """ライデイン - 電撃の魔法"""
    def __init__(self):
        super().__init__("ライデイン", mp_cost=12, power=30, effect_type='damage')


# 敵スキル
class EnemySlash(Skill):
    """敵用基本攻撃"""
    def __init__(self):
        super().__init__("敵の斬撃", mp_cost=0, power=5, effect_type='damage')


class PoisonAttack(Skill):
    """毒攻撃"""
    def __init__(self):
        super().__init__("毒攻撃", mp_cost=3, power=8, effect_type='damage')


class SkillList:
    """スキル管理クラス"""
    
    @staticmethod
    def get_player_start_skills():
        """プレイヤーの初期スキルを取得"""
        return [Slash(), Heal()]
    
    @staticmethod
    def get_all_player_skills():
        """全プレイヤースキルを取得"""
        return [
            Slash(),
            PowerSlash(),
            Heal(),
            GreatHeal(),
            IceStrike(),
            Lightning()
        ]

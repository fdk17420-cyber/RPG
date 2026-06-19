"""
ドラゴンクエスト風RPG - アイテム・装備品システム
"""

class Item:
    """アイテム基本クラス"""
    
    def __init__(self, name, item_type, value, description=""):
        self.name = name
        self.item_type = item_type  # 'consumable', 'equipment', 'quest'
        self.value = value  # 価格またはレアリティ
        self.description = description
    
    def use(self, user):
        """アイテムを使用する"""
        return f"{self.name}を使用した！"


class ConsumableItem(Item):
    """消費アイテム"""
    
    def __init__(self, name, effect_type, amount, value, description=""):
        super().__init__(name, 'consumable', value, description)
        self.effect_type = effect_type  # 'heal_hp', 'heal_mp', 'revive'
        self.amount = amount
    
    def use(self, user):
        """消費アイテムを使用する"""
        if self.effect_type == 'heal_hp':
            healed = user.heal(self.amount)
            return f"{user.name}のHPが{healed}回復した！"
        elif self.effect_type == 'heal_mp':
            recovered = user.recover_mp(self.amount)
            return f"{user.name}のMPが{recovered}回復した！"
        elif self.effect_type == 'revive':
            if not user.is_alive:
                user.is_alive = True
                user.hp = user.max_hp // 2
                return f"{user.name}が復活した！"
            return "対象は生きています。"
        return "使用できません。"


class Equipment(Item):
    """装備品"""
    
    def __init__(self, name, equipment_type, attack_bonus=0, defense_bonus=0, 
                 hp_bonus=0, speed_bonus=0, value=0, description=""):
        super().__init__(name, 'equipment', value, description)
        self.equipment_type = equipment_type  # 'weapon', 'armor', 'accessory'
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.hp_bonus = hp_bonus
        self.speed_bonus = speed_bonus
    
    def equip(self, player):
        """装備を装備する"""
        return f"{player.name}は{self.name}を装備した！"


class Inventory:
    """インベントリシステム"""
    
    def __init__(self):
        self.items = []
        self.equipment = {
            'weapon': None,
            'armor': None,
            'accessory': None
        }
    
    def add_item(self, item, quantity=1):
        """アイテムを追加"""
        for i in range(quantity):
            self.items.append(item)
    
    def remove_item(self, item):
        """アイテムを削除"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def equip_item(self, item):
        """装備品を装備"""
        if isinstance(item, Equipment):
            old_equipment = self.equipment[item.equipment_type]
            self.equipment[item.equipment_type] = item
            return old_equipment
        return None
    
    def get_equipped_stats(self):
        """装備から得られるステータスボーナス"""
        stats = {
            'attack': 0,
            'defense': 0,
            'hp': 0,
            'speed': 0
        }
        for equipment in self.equipment.values():
            if equipment:
                stats['attack'] += equipment.attack_bonus
                stats['defense'] += equipment.defense_bonus
                stats['hp'] += equipment.hp_bonus
                stats['speed'] += equipment.speed_bonus
        return stats
    
    def show_inventory(self):
        """インベントリを表示"""
        print("\n" + "─" * 50)
        print("【インベントリ】")
        print("─" * 50)
        
        if not self.items:
            print("アイテムがありません。\n")
            return
        
        print("\n【持ち物】")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - {item.description}")
        
        print("\n【装備中】")
        for slot_type, equipment in self.equipment.items():
            if equipment:
                print(f"  {slot_type}: {equipment.name}")
            else:
                print(f"  {slot_type}: 未装備")
        
        print()


# アイテムリスト
class ItemList:
    """アイテム管理"""
    
    @staticmethod
    def get_all_items():
        """全アイテムを取得"""
        return {
            # 消費アイテム
            'potion': ConsumableItem("ポーション", "heal_hp", 50, 100, "HPを50回復する"),
            'hi_potion': ConsumableItem("ハイポーション", "heal_hp", 150, 300, "HPを150回復する"),
            'mp_potion': ConsumableItem("マジックポーション", "heal_mp", 30, 200, "MPを30回復する"),
            'revive_potion': ConsumableItem("復活の薬", "revive", 0, 500, "倒れた仲間を復活させる"),
            
            # 武器
            'iron_sword': Equipment("鉄の剣", "weapon", attack_bonus=10, value=500, 
                                   description="基本的な剣"),
            'steel_sword': Equipment("鋼の剣", "weapon", attack_bonus=20, value=1500, 
                                    description="強力な剣"),
            'legendary_sword': Equipment("伝説の剣", "weapon", attack_bonus=40, value=5000, 
                                        description="最強の剣"),
            
            # 防具
            'leather_armor': Equipment("革の鎧", "armor", defense_bonus=5, value=400, 
                                      description="軽い防具"),
            'iron_armor': Equipment("鉄の鎧", "armor", defense_bonus=15, value=1200, 
                                   description="頑丈な防具"),
            'dragon_armor': Equipment("竜の鎧", "armor", defense_bonus=30, hp_bonus=50, 
                                     value=4000, description="最高の防具"),
            
            # アクセサリー
            'ring_of_strength': Equipment("力の指輪", "accessory", attack_bonus=5, value=800, 
                                         description="攻撃力を上げる"),
            'ring_of_defense': Equipment("守りの指輪", "accessory", defense_bonus=8, value=800, 
                                        description="防御力を上げる"),
            'ring_of_speed': Equipment("速度の指輪", "accessory", speed_bonus=3, value=800, 
                                      description="素早さを上げる"),
        }
    
    @staticmethod
    def get_shop_items():
        """ショップで販売するアイテム"""
        return {
            'potion': ItemList.get_all_items()['potion'],
            'hi_potion': ItemList.get_all_items()['hi_potion'],
            'mp_potion': ItemList.get_all_items()['mp_potion'],
            'iron_sword': ItemList.get_all_items()['iron_sword'],
            'leather_armor': ItemList.get_all_items()['leather_armor'],
        }

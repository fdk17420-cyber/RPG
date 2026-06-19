"""
ドラゴンクエスト風RPG - NPC会話・クエスト・商人システム
"""
from typing import List, Optional
from items import ItemList


class DialogueNode:
    """簡易的な会話ノード
    text: 表示するテキスト
    options: list of tuples (option_text, next_node_index, action)
    action: optional string to trigger ('shop','quest','leave')
    """

    def __init__(self, text: str, options: Optional[List[tuple]] = None):
        self.text = text
        self.options = options or []


class Quest:
    """簡易クエスト管理クラス
    例: 敵を倒す系のクエストを想定
    """

    def __init__(self, title: str, description: str, target: str, required: int,
                 reward_exp: int, reward_gold: int, reward_item_key: Optional[str] = None):
        self.title = title
        self.description = description
        self.target = target
        self.required = required
        self.progress = 0
        self.completed = False
        self.reward_exp = reward_exp
        self.reward_gold = reward_gold
        self.reward_item_key = reward_item_key
        self.claimed = False

    def record_kill(self, enemy_name: str, player):
        if self.completed:
            return
        if enemy_name == self.target:
            self.progress += 1
            if self.progress >= self.required:
                self.completed = True
                print(f"\n🎉 クエスト完了: {self.title}")
                print(f"   {self.description}")

    def claim(self, player):
        if not self.completed or self.claimed:
            return False
        player.gain_experience(self.reward_exp)
        player.gold += self.reward_gold
        if self.reward_item_key:
            all_items = ItemList.get_all_items()
            item = all_items.get(self.reward_item_key)
            if item:
                # playerインベントリを想定しているため、存在するなら追加
                if hasattr(player, 'inventory'):
                    player.inventory.add_item(item)
        self.claimed = True
        print(f"\n📦 報酬を受け取った: 経験値+{self.reward_exp}, ゴルド+{self.reward_gold}")
        return True


class NPC:
    """汎用NPCクラス。会話とクエストの管理を行う。"""

    def __init__(self, name: str, nodes: Optional[List[DialogueNode]] = None, quest: Optional[Quest] = None):
        self.name = name
        self.nodes = nodes or []
        self.quest = quest

    def talk(self, player):
        print(f"\n【{self.name} と会話】")
        if not self.nodes:
            print("...特に話すことはないようだ。")
            return

        index = 0
        while True:
            node = self.nodes[index]
            print(f"\n{self.name}: {node.text}")
            if not node.options:
                break
            for i, (opt_text, _, _) in enumerate(node.options, 1):
                print(f"{i}. {opt_text}")

            try:
                choice = int(input("\n> ").strip())
                if not (1 <= choice <= len(node.options)):
                    print("無効な選択です。")
                    continue
            except ValueError:
                print("数字を入力してください。")
                continue

            _, next_index, action = node.options[choice - 1]
            if action == 'shop':
                ShopNPC.open_shop(player)
                break
            if action == 'quest':
                if self.quest and not self.quest.completed:
                    print(f"\n📝 クエストを受注した: {self.quest.title}")
                    print(f"   {self.quest.description}")
                    # プレイヤーにクエストを紐付ける
                    if hasattr(player, 'quests'):
                        player.quests.append(self.quest)
                    else:
                        player.quests = [self.quest]
                elif self.quest and self.quest.completed and not self.quest.claimed:
                    print("\nクエストを報告します...")
                    self.quest.claim(player)
                else:
                    print("\n特に依頼はありません。")
                break
            if action == 'leave' or next_index is None:
                print("\n会話を終了しました。")
                break
            index = next_index


class ShopNPC(NPC):
    """商人NPC。ショップを開いてアイテムを売買できる。"""

    @staticmethod
    def open_shop(player):
        shop_items = ItemList.get_shop_items()
        keys = list(shop_items.keys())
        print("\n【ショップ】いらっしゃい！何を買う？")
        while True:
            for i, k in enumerate(keys, 1):
                item = shop_items[k]
                print(f"{i}. {item.name} - {item.value}ゴルド ({item.description})")
            print(f"{len(keys)+1}. 退出")

            try:
                choice = int(input("\n> ").strip())
            except ValueError:
                print("数字を入力してください。")
                continue

            if choice == len(keys) + 1:
                print("\nまたお越しください！")
                break
            if not (1 <= choice <= len(keys)):
                print("無効な選択です。")
                continue

            key = keys[choice - 1]
            item = shop_items[key]
            if player.gold >= item.value:
                player.gold -= item.value
                if hasattr(player, 'inventory'):
                    player.inventory.add_item(item)
                else:
                    # 簡易的にインベントリを持たせる
                    player.inventory = type('Inv', (), {'items': [item], 'add_item': lambda self, it: self.items.append(it)})()
                print(f"\n購入しました: {item.name}")
                print(f"残りゴルド: {player.gold}")
            else:
                print("\nゴルドが不足しています。")


# NPCのサンプルデータ作成
def create_town_npcs():
    shopkeeper_nodes = [
        DialogueNode("いらっしゃい、旅の者よ。商品を見ていきな。", options=[
            ("買い物をする", None, 'shop'),
            ("また来る", None, 'leave')
        ])
    ]
    shopkeeper = ShopNPC("商人のジョバンニ", nodes=shopkeeper_nodes)

    quest = Quest(
        title="スライム退治",
        description="スライムを3匹討伐してほしい。",
        target="スライム",
        required=3,
        reward_exp=200,
        reward_gold=150,
        reward_item_key='potion'
    )
    quest_nodes = [
        DialogueNode("村人: 最近スライムが増えて困っているんだ。手伝ってくれないか？", options=[
            ("引き受ける", None, 'quest'),
            ("考えておく", None, 'leave')
        ])
    ]
    quest_giver = NPC("村人のハンス", nodes=quest_nodes, quest=quest)

    return [shopkeeper, quest_giver]

from Card import Card, Card_Spell, Card_Trap, Card_Monster, Card_ExtraMonster
import json
from pathlib import Path

class CardDatabaseManager:

    # 0-60 Deck 61-75 Extra Deck
    CardsCurrentDeck_Player: list[Card]
    CardsCurrentDeck_Opponent: list[Card]

    CardsListUnlocked: list[tuple[Card, bool]]
    CardsBoosterPacks: list[tuple[str, list[Card]]]

    def __init__(self):
        pass

    @staticmethod
    def parse_json(path_to_file):
        path = Path(path_to_file)
        if not path.exists():
            raise Exception("Input JSON file not found!")

        with (open(path, "r") as file):
            data = json.load(file)

            for card_data in data:

                Name = card_data["Name"]
                ID = card_data["id"]
                Category = card_data["Category"]
                Description = card_data["Effect"][0]
                CardArt = card_data["Card art"]

                match Category:
                    case "SPELL":
                        card = Card_Spell()
                    case "TRAP":
                        card = Card_Trap()
                    case "MONSTER":
                        card = Card_Monster(Name, ID, [], CardArt, Description, ATK, DEF,)
                    case "FUSION" | "LINK" | "XYZ" | "SYNCHRO":
                        card = Card_ExtraMonster()
                    case _:
                        raise Exception("Invalid card type when reading data.")

                print(card)

                print(f"{card_data["Name"]} {card_data["Category"]} {card_data["Effect"][0]}")



CardDatabaseManager.parse_json("data/dummy_json.json")

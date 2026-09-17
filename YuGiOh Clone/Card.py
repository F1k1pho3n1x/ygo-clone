from Effect import Effect
from ECardCategory import ECardCategory, ECardAttribute, ESpellType, ETrapType, EExtraMonsterType


class Card:
    Name: str
    ID: str
    Category: ECardCategory
    Effects: list[Effect]
    CardArt: str
    Description: str

    # Makes an instance of a card - physical copy for the game
    def __init__(self, Name: str, ID: str, Category: ECardCategory, Effects: list, CardArt: str, Description: str):
        self.Name = Name
        self.ID = ID
        self.Category = Category
        self.Effects = Effects
        self.CardArt = CardArt
        self.Description = Description

    def __str__(self):
        return f"({self.ID}) {self.Category}: {self.Name} - {self.Description}"

class Card_Spell(Card):
    SpellType: ESpellType


    def __init__(self, Name: str, ID: str, Effects: list, CardArt: str, Description: str):



        super().__init__(Name, ID, ECardCategory.SPELL, Effects, CardArt, Description)



class Card_Trap(Card):
    TrapType: ETrapType

    def __init__(self, Name: str, ID: str, Effects: list, CardArt: str, Description: str):
        self.TrapType = ETrapType.NORMAL


        super().__init__(Name, ID, ECardCategory.TRAP, Effects, CardArt, Description)


class Card_Monster(Card):
    ATK: int
    DEF: int
    Type: str
    Ability: str
    Attribute: ECardAttribute

    def __init__(self, Name: str, ID: str, Effects: list, CardArt: str, Description: str):
        self.ATK = 0
        self.DEF = 0
        self.Type = "N/A"
        self.Ability = "Normal"
        self.Attribute = ECardAttribute.OTHER


        super().__init__(Name, ID, ECardCategory.MONSTER, Effects, CardArt, Description)

    def __str__(self):
        return f"({self.ID}) {self.Category}: {self.Name} | [{self.Type}/{self.Ability}] ({self.ATK:4}/{self.DEF:4}) - {self.Description}"

class Card_ExtraMonster(Card_Monster):
    ExtraMonsterType: EExtraMonsterType
    Materials: list[str]

    def __init__(self, Name: str, ID: str, Effects: list, CardArt: str, Description: str, ExtraMonsterType: str, Materials: list[str]):
        super().__init__(Name, ID, Effects, CardArt, Description)
        self.Category = ECardCategory.EXTRA_MONSTER
        self.ExtraMonsterType = EExtraMonsterType[ExtraMonsterType]
        self.Materials = Materials

    def __str__(self):
        super().__str__()



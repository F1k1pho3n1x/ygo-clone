from enum import Enum

class ECardCategory(Enum):
    MONSTER = 1,
    SPELL = 2,
    TRAP = 3,
    EXTRA_MONSTER = 4,
    OTHER = 5

class ECardAttribute(Enum):
    SPELL = 1,
    TRAP = 2,
    WATER = 3,
    FIRE = 4,
    EARTH = 5,
    WIND = 6,
    LIGHT = 7,
    DARK = 8,
    DIVINE = 9,
    OTHER = 10

class ESpellType(Enum):
    NORMAL = 1,
    QUICK_PLAY = 2,
    CONTINUOUS = 3,
    FIELD = 4,
    EQUIP = 5,
    RITUAL = 6

class ETrapType(Enum):
    NORMAL = 1,
    COUNTER = 2,
    CONTINUOUS = 3
    PHASE = 4
    # Trap cards that activate at a specific Phase, cannot be countered, if not destroyed beforehand (PHASE = 4)

class EExtraMonsterType(Enum):
    FUSION = 1,
    SYNCHRO = 2,
    XYZ = 3,
    LINK = 4.
    OTHER = 5
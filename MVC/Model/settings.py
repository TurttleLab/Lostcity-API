from enum import Enum


class FieldClassEnum(Enum):
    SPACE = 0
    LAVA = 1
    JUNGLE = 2
    OCEAN = 3
    SNOW = 4
    DESSERT = 5


class PlayerEnum(Enum):
    BLACK = 0
    WHITE = 1
    TRASH = 2

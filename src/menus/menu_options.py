from enum import Enum


class MenuOption(Enum):
    PROCESS_USER_INPUT = 1
    PROCESS_FROM_FILE = 2
    SAVE_TO_FILE = 3
    EXIT = 4


class CipherType(Enum):
    ROT13 = "rot13"
    ROT47 = "rot47"


class TextStatus(Enum):
    ENCODED = "encoded"
    DECODED = "decoded"

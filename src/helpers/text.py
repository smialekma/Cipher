from dataclasses import dataclass
from src.menus.menu_options import CipherType, TextStatus


@dataclass
class Text:
    text: str
    rot_type: str | CipherType
    status: str | TextStatus

from dataclasses import dataclass
from src.decoders.cipher_type import CipherType
from src.helpers.text_status import TextStatus


@dataclass
class Text:
    text: str
    rot_type: str | CipherType
    status: str | TextStatus

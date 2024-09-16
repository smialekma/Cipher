from __future__ import annotations
from abc import ABC, abstractmethod
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase


class Decoder(ABC):

    @abstractmethod
    def encode(self, text: str):
        pass

    @abstractmethod
    def decode(self, text: str):
        pass


class RotDecoder(Decoder):
    def __init__(self, shift: int):
        self.shift = shift

    def encode(self, text: str) -> str:
        """This function encodes [plain -> cipher] a text with a Caesar cipher."""
        shift = self.shift
        lookup = str.maketrans(
            lowercase + uppercase,
            lowercase[shift:]
            + lowercase[:shift]
            + uppercase[shift:]
            + uppercase[:shift],
        )
        return text.translate(lookup)

    def decode(self, text: str) -> str:
        """This function decodes [cipher -> plain] a text with a Caesar cipher."""
        shift = -self.shift
        lookup = str.maketrans(
            lowercase + uppercase,
            lowercase[shift:]
            + lowercase[:shift]
            + uppercase[shift:]
            + uppercase[:shift],
        )
        return text.translate(lookup)

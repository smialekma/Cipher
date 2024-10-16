from __future__ import annotations
from abc import ABC, abstractmethod
import codecs


class Decoder(ABC):

    @abstractmethod
    def encode(self, text: str) -> str:
        pass

    @abstractmethod
    def decode(self, text: str) -> str:
        pass


class Rot13Decoder(Decoder):

    def _transform(self, text) -> str:
        return codecs.encode(text, "rot_13")

    def encode(self, text: str) -> str:
        """This function encodes [plain -> cipher] a text with a Caesar cipher."""
        return self._transform(text)

    def decode(self, text: str) -> str:
        """This function decodes [cipher -> plain] a text with a Caesar cipher."""
        return self._transform(text)


class Rot47Decoder(Decoder):

    def encode(self, text: str) -> str:
        """This function encodes [plain -> cipher] a text with a Caesar cipher."""
        encoded_message = ""
        for char in text:
            char_code = ord(char)
            if 33 <= char_code <= 126:
                char_code -= 47
                if char_code < 33:
                    char_code += 94
            encoded_message += chr(char_code)
        return encoded_message

    def decode(self, text: str) -> str:
        """This function decodes [cipher -> plain] a text with a Caesar cipher."""
        decoded_message = ""
        for char in text:
            char_code = ord(char)
            if 33 <= char_code <= 126:
                char_code += 47
                if char_code > 126:
                    char_code -= 94
            decoded_message += chr(char_code)
        return decoded_message

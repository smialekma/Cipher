from rot_decoder import RotDecoder
from abc import ABC, abstractmethod


class DecoderFactory(ABC):

    @abstractmethod
    def create_decoder(self):
        pass


class Rot13Factory(DecoderFactory):

    def create_decoder(self) -> RotDecoder:
        """This function creates Rot13 Decoder"""
        return RotDecoder(13)


class Rot47Factory(DecoderFactory):

    def create_decoder(self) -> RotDecoder:
        """This function creates Rot47 Decoder"""
        return RotDecoder(47)

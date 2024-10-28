from abc import ABC, abstractmethod
from src.decoders.rot_decoder import Rot13Decoder, Rot47Decoder


class DecoderFactory(ABC):

    @abstractmethod
    def create_decoder(self):
        pass


class Rot13Factory(DecoderFactory):

    def create_decoder(self) -> Rot13Decoder:
        """This function creates Rot13 Decoder"""
        return Rot13Decoder()


class Rot47Factory(DecoderFactory):

    def create_decoder(self) -> Rot47Decoder:
        """This function creates Rot47 Decoder"""
        return Rot47Decoder()

from src.decoders.decoder_factory import Rot13Factory, Rot47Factory
from src.decoders.rot_decoder import Rot13Decoder, Rot47Decoder


class TestRot13Factory:
    def test_should_return_rot_13_object_when_create_decoder_method_is_called(self):
        rot13factory = Rot13Factory()
        returned_object = rot13factory.create_decoder()
        assert isinstance(returned_object, Rot13Decoder)


class TestRot47Factory:
    def test_should_return_rot_47_object_when_create_decoder_method_is_called(self):
        rot47factory = Rot47Factory()
        returned_object = rot47factory.create_decoder()
        assert isinstance(returned_object, Rot47Decoder)

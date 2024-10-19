import pytest
from src.helpers.buffer import Buffer
from src.helpers.buffer import Text


class TestBuffer:

    @pytest.fixture()
    def buffer(self):
        return Buffer()

    @pytest.mark.test_buffer_to_dict
    def test_should_return_correct_dict_from_buffer(self, buffer):
        buffer.buffer.clear()

        text1 = Text("heja", "rot47", "decoded")
        text2 = Text("jagjds", "rot13", "encoded")

        buffer.buffer.append(text1)
        buffer.buffer.append(text2)

        returned_dict = {
            "1": {"text": "heja", "rot_type": "rot47", "status": "decoded"},
            "2": {"text": "jagjds", "rot_type": "rot13", "status": "encoded"},
        }

        assert buffer.buffer_to_dict() == returned_dict

        # empty_buffer?

    @pytest.mark.test_single_dict_to_text_object
    def test_should_return_correct_text_object_from_single_dict(self, buffer):
        single_dict = {"text": "heja", "rot_type": "rot47", "status": "decoded"}
        text_obj = buffer._single_dict_to_text_object(single_dict)
        assert isinstance(text_obj, Text)

    @pytest.mark.test_add_to_buffer
    def test_should_add_correctly_to_buffer_when_text_object_is_provided(self, buffer):
        buffer.buffer.clear()

        text = Text("jagjds", "rot13", "encoded")

        buffer.add_to_buffer(text)

        assert buffer.buffer[0].text == "jagjds"
        assert buffer.buffer[0].rot_type == "rot13"
        assert buffer.buffer[0].status == "encoded"

    @pytest.mark.test_dict_to_buffer
    def test_should_add_correctly_to_buffer_when_nested_dict_is_provided(self, buffer):
        buffer.buffer.clear()

        nested_dict = {
            "1": {"text": "heja", "rot_type": "rot47", "status": "decoded"},
            "2": {"text": "jagjds", "rot_type": "rot13", "status": "encoded"},
        }

        buffer.dict_to_buffer(nested_dict)

        assert buffer.buffer[0].rot_type == "rot47"
        assert buffer.buffer[0].text == "heja"
        assert buffer.buffer[1].status == "encoded"
        assert buffer.buffer[1].text == "jagjds"

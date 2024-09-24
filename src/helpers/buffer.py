from src.decoders.text import Text
from dataclasses import asdict


class Buffer:
    buffer: list[Text] = []

    def buffer_to_dict(self) -> dict[int, dict[str, str]]:
        """Takes dataclass objects from buffer and converts them to a dictionary."""
        buffer_dict = {}
        for count, text_object in enumerate(Buffer.buffer, start=1):
            text_object_dict = asdict(text_object)
            buffer_dict[count] = text_object_dict
        return buffer_dict

    def _single_dict_to_text_object(self, python_dict: dict[str, str]) -> Text:
        """Converts a single (not nested) dictionary into a dataclass object."""
        return Text(**python_dict)

    def add_to_buffer(self, obj_to_add: Text) -> None:
        Buffer.buffer.append(obj_to_add)

    def dict_to_buffer(self, nested_dict: dict[int, dict[str, str]]) -> None:
        """Takes nested dictionary and converts it to dataclass objects, then adds it to buffer.
        Dictionary structure: {1:{...}, 2:{...}}"""
        for key, value in nested_dict:
            text_object = self._single_dict_to_text_object(value)
            self.add_to_buffer(text_object)

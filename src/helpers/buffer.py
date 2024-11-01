from dataclasses import asdict
from src.helpers.text import Text


class Buffer:
    buffer: list[Text] = []

    def buffer_to_dict(self) -> dict[str, dict[str, str]]:
        """Takes dataclass objects from buffer and converts them to a dictionary."""
        buffer_dict = {}
        for count, text_object in enumerate(Buffer.buffer, start=1):
            text_object_dict = asdict(text_object)
            count = str(count)
            buffer_dict[count] = text_object_dict
        return buffer_dict

    def _single_dict_to_text_object(self, python_dict: dict[str, str]) -> Text:
        """Converts a single (not nested) dictionary into a dataclass object."""
        return Text(**python_dict)

    def add_to_buffer(self, obj_to_add: Text) -> None:
        Buffer.buffer.append(obj_to_add)

    def dict_to_buffer(self, nested_dict: dict[str, dict[str, str]]) -> None:
        """Takes nested dictionary and converts it to dataclass objects, then adds it to buffer.
        Dictionary structure: {1:{...}, 2:{...}}"""
        for key, value in nested_dict.items():
            text_object = self._single_dict_to_text_object(value)
            self.add_to_buffer(text_object)

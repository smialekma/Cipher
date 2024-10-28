from src.helpers.text import Text


class TestText:
    def test_should_correctly_create_text_object(self):
        text = Text("some text", "rot13", "encoded")
        assert text.text == "some text"
        assert text.rot_type == "rot13"
        assert text.status == "encoded"

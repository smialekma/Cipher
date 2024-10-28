import json
import os
from unittest.mock import patch, call

import pytest

from src.decoders.decoder_factory import Rot13Factory, Rot47Factory
from src.helpers.text import Text
from src.managers.manager import Manager
from src.files.file_handler import FileHandler
from src.menus.menu import Menu
from src.helpers.buffer import Buffer
from src.helpers.text_status import TextStatus
from src.decoders.cipher_type import CipherType


class TestManager:
    FILE_PATH = "test.json"

    @pytest.fixture()
    def manager(self):
        manager = Manager(menu=Menu(), buffer=Buffer(), file_handler=FileHandler())
        return manager

    def test_should_correctly_create_manager_object(self, manager):
        assert isinstance(manager.filehandler, FileHandler)
        assert isinstance(manager.buffer, Buffer)
        assert isinstance(manager.menu, Menu)

    @pytest.mark.test_start
    def test_should_correctly_display_start_message_and_take_user_input(self, manager):
        with patch("builtins.print") as mock_print:
            with patch("builtins.input", return_value="4"):
                assert not manager.start()
                mock_print.assert_has_calls(
                    [
                        call("1 - Enter a text"),
                        call("2 - Load from a json file"),
                        call("3 - Save to a json file"),
                        call("4 - Exit"),
                    ]
                )

    @pytest.mark.test_execute
    def test_should_return_correct_function_for_user_input(self, manager):

        def return_hi():
            print("hi")

        def return_hello():
            print("hello")

        options = {1: return_hi, 2: return_hello}

        with patch("builtins.input", return_value="1"):
            with patch("builtins.print") as mock_print:
                manager.execute(options)
                mock_print.assert_has_calls([call("hi")])

    @pytest.mark.test_execute
    def test_execute_method_expect_error_message_when_number_out_of_range(
        self, manager
    ):

        def return_hi():
            print("hi")

        def return_hello():
            print("hello")

        options = {1: return_hi, 2: return_hello}

        with patch("builtins.input", side_effect=["3", "2"]):
            with patch("builtins.print") as mock_print:
                manager.execute(options)
                mock_print.assert_has_calls([call("You entered an incorrect number.")])

    @pytest.mark.test_save_to_file
    def test_should_correctly_save_to_file(self, manager):
        manager.buffer.buffer.clear()

        file_path = self.FILE_PATH

        text1 = Text("heja", "rot47", "decoded")
        text2 = Text("jag, jds", "rot13", "encoded")

        manager.buffer.buffer.append(text1)
        manager.buffer.buffer.append(text2)

        with patch("builtins.input", return_value=file_path):
            manager.save_to_file()

        with open(file_path, "r") as json_file:
            json_dict = json.load(json_file)

        returned_dict = {
            "1": {"text": "heja", "rot_type": "rot47", "status": "decoded"},
            "2": {"text": "jag, jds", "rot_type": "rot13", "status": "encoded"},
        }

        assert json_dict == returned_dict

    @pytest.mark.test_read_from_file
    def test_should_correctly_load_from_file(self, manager):
        manager.buffer.buffer.clear()

        file_path = self.FILE_PATH

        new_dict = {
            "1": {"text": "heja", "rot_type": "rot47", "status": "decoded"},
            "2": {"text": "jag, jds", "rot_type": "rot13", "status": "encoded"},
        }

        with open(file_path, "w") as json_file:
            json.dump(new_dict, json_file, indent=4)

        with patch("builtins.input", return_value=file_path):
            manager.read_from_file()

        assert manager.buffer.buffer[0].text == "heja"
        assert manager.buffer.buffer[0].status == "decoded"
        assert manager.buffer.buffer[1].text == "jag, jds"
        assert manager.buffer.buffer[1].rot_type == "rot13"

    @pytest.mark.test_get_status
    def test_should_correctly_return_encoded_or_decoded_for_number_chosen(
        self, manager
    ):
        with patch("builtins.input", return_value="1"):
            assert manager._get_status() == TextStatus.ENCODED.value

    @pytest.mark.test_get_status
    def test_get_status_method_expect_error_message_when_number_out_of_range(
        self, manager
    ):
        with patch("builtins.input", side_effect=["5", "4"]):
            with patch("builtins.print") as mock_print:
                manager._get_status()
                mock_print.assert_has_calls(
                    [
                        call("1 - Encode"),
                        call("2 - Decode"),
                        call(),
                        call("You entered an incorrect number."),
                    ]
                )

    @pytest.mark.test_get_rot
    def test_should_correctly_return_rot_for_number_chosen(self, manager):
        with patch("builtins.input", return_value="2"):
            assert manager._get_rot() == CipherType.ROT47.value

    # def test_expect_exception_when_number_out_of_range():
    # pass

    @pytest.mark.test_get_decoder_factory
    def test_should_return_correct_decoder_factory(self, manager):
        rot_type = CipherType.ROT13.value
        factory = manager._get_decoder_factory(rot_type)

        assert isinstance(factory, Rot13Factory)

    @pytest.mark.test_process_user_input
    def test_should_correctly_process_user_input(self, manager, mocker):
        manager.buffer.buffer.clear()
        mocker.patch("src.menus.menu.Menu.get_text", return_value="A kot ma 1 Alę!")
        mocker.patch(
            "src.managers.manager.Manager._get_status",
            return_value=TextStatus.ENCODED.value,
        )
        mocker.patch(
            "src.managers.manager.Manager._get_rot", return_value=CipherType.ROT47.value
        )
        mocker.patch(
            "src.managers.manager.Manager._get_decoder_factory",
            return_value=Rot47Factory(),
        )

        mocker.patch("src.menus.menu.Menu.get_number", return_value=2)

        with patch("builtins.print") as mock_print:
            with patch("builtins.input", return_value="2"):
                manager.process_user_input()
                mock_print.assert_has_calls(
                    [
                        call("Original text: A kot ma 1 Alę!"),
                        call("Processed text: p <@E >2 ` p=ęP"),
                        call(),
                        call("Do you want to:"),
                        call("1 - Get back to the main menu?"),
                        call("2 - Exit?"),
                        call(),
                    ]
                )

        assert manager.buffer.buffer[0].text == "p <@E >2 ` p=ęP"
        assert manager.buffer.buffer[0].status == "encoded"
        assert manager.buffer.buffer[0].rot_type == "rot47"

    @pytest.mark.test_process_text_from_file
    def test_should_correctly_process_texts_from_file(self, manager, mocker):
        test_dict = {
            "1": {"text": "p <@E >2 ` p=ęP", "rot_type": "rot47", "status": "encoded"},
            "2": {
                "text": "The quick brown fox jumps over the lazy dog",
                "rot_type": "rot13",
                "status": "decoded",
            },
            "3": {
                "text": "Fvrznarpmxb! Jvgnz cnńfgjn :)",
                "rot_type": "rot13",
                "status": "encoded",
            },
            "4": {
                "text": "Hello from the other side.",
                "rot_type": "rot47",
                "status": "decoded",
            },
        }

        file_path = self.FILE_PATH

        with open(file_path, "w") as json_file:
            json.dump(test_dict, json_file, indent=4)

        manager.buffer.buffer.clear()
        mocker.patch("src.menus.menu.Menu.get_file_path", return_value=file_path)
        mocker.patch(
            "src.managers.manager.Manager._get_status",
            return_value=TextStatus.ENCODED.value,
        )
        mocker.patch(
            "src.managers.manager.Manager._get_rot", return_value=CipherType.ROT47.value
        )
        mocker.patch(
            "src.managers.manager.Manager._get_decoder_factory",
            return_value=Rot47Factory(),
        )

        mocker.patch("src.menus.menu.Menu.get_number", return_value=2)

        with patch("builtins.print") as mock_print:
            with patch("builtins.input", return_value="2"):
                manager.process_texts_from_file()
                mock_print.assert_has_calls(
                    [
                        call("The text(s) has been loaded."),
                        call(
                            "Original text: The quick brown fox jumps over the lazy dog"
                        ),
                        call(
                            "Processed text: %96 BF:4< 3C@H? 7@I ;F>AD @G6C E96 =2KJ 5@8"
                        ),
                        call(),
                        call("Original text: Hello from the other side."),
                        call("Processed text: w6==@ 7C@> E96 @E96C D:56]"),
                        call(),
                        call("Do you want to:"),
                        call("1 - Get back to the main menu?"),
                        call("2 - Exit?"),
                        call(),
                    ]
                )

    def teardown_method(self):
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)

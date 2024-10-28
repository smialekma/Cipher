import json
import os
from unittest.mock import patch
import pytest

from src.files.file_handler import FileHandler


class TestFileHandler:
    FILE_PATH = "test_json.json"
    FILE_PATH_TXT = "test_txt.txt"
    NEW_FILE_PATH = "new.json"
    EMPTY_FILE_PATH = "empty.json"

    @pytest.fixture()
    def handler(self):
        return FileHandler()

    @pytest.mark.test_read_from_file
    def test_expect_error_message_when_file_path_is_invalid(self, handler):
        with patch("builtins.print") as mock_print:
            handler.read_from_file("invalid/file/path")
            mock_print.assert_called_with(
                "File not found. Please check the path and ensure the file exists."
            )

    @pytest.mark.test_read_from_file
    def test_expect_error_message_when_invalid_file(self, handler):
        with open(self.FILE_PATH_TXT, "w") as file:
            file.write("")

        with patch("builtins.print") as mock_print:
            handler.read_from_file(self.FILE_PATH_TXT)
            mock_print.assert_called_with(
                "Invalid file. Please check the path and ensure the file is valid."
            )

    @pytest.mark.test_read_from_file
    def test_should_return_correct_dict_when_file_path_to_json_file_is_provided(
        self, handler
    ):

        test_dict = {
            "1": {"text": "tekst", "status": "decoded"},
            "2": {"text": "kolejny tekst", "status": "encoded"},
            "3": {"text": "jakis tekst", "status": "encoded"},
            "4": {"text": "inny tekst", "status": "decoded"},
        }

        with open(self.FILE_PATH, "w") as json_file:
            json.dump(test_dict, json_file, indent=4)

        assert handler.read_from_file(self.FILE_PATH) == test_dict

    @pytest.mark.test_read_from_file
    def test_expect_error_message_when_file_is_empty(self, handler):
        with open(self.EMPTY_FILE_PATH, "w") as file:
            file.write("")

        with patch("builtins.print") as mock_print:
            handler.read_from_file(self.EMPTY_FILE_PATH)
            mock_print.assert_called_with(
                "Invalid file. Please check the path and ensure the file is valid."
            )

    @pytest.mark.test_save_to_file
    def test_should_be_saved_correctly_when_appended_to_existing_file(self, handler):

        test_dict = {
            "1": {"text": "tekst", "status": "decoded"},
            "2": {"text": "kolejny tekst", "status": "encoded"},
        }

        appended_dict = {
            "1": {"text": "jakis tekst", "status": "encoded"},
            "2": {"text": "inny tekst", "status": "decoded"},
        }

        returned_dict = {
            "1": {"text": "tekst", "status": "decoded"},
            "2": {"text": "kolejny tekst", "status": "encoded"},
            "3": {"text": "jakis tekst", "status": "encoded"},
            "4": {"text": "inny tekst", "status": "decoded"},
        }

        with open(self.FILE_PATH, "w") as json_file:
            json.dump(test_dict, json_file, indent=4)

        handler.save_to_file(self.FILE_PATH, appended_dict)

        with open(self.FILE_PATH, "r") as json_file:
            json_dict = json.load(json_file)

        assert json_dict == returned_dict

    @pytest.mark.test_save_to_file
    def test_should_be_saved_correctly_when_saved_to_new_file(self, handler):

        test_dict = {
            "1": {"text": "tekst", "status": "decoded"},
            "2": {"text": "kolejny tekst", "status": "encoded"},
            "3": {"text": "jakis tekst", "status": "encoded"},
            "4": {"text": "inny tekst", "status": "decoded"},
        }

        handler.save_to_file(self.NEW_FILE_PATH, test_dict)

        with open(self.NEW_FILE_PATH, "r") as json_file:
            json_dict = json.load(json_file)

        assert json_dict == test_dict

    def teardown_method(self):
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)

        if os.path.exists(self.FILE_PATH_TXT):
            os.remove(self.FILE_PATH_TXT)

        if os.path.exists(self.NEW_FILE_PATH):
            os.remove(self.NEW_FILE_PATH)

        if os.path.exists(self.EMPTY_FILE_PATH):
            os.remove(self.EMPTY_FILE_PATH)

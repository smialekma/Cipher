import json
from unittest.mock import patch

from src.files.file_handler import FileHandler
import pytest


class TestFileHandler:
    FILE_PATH = "test_json.json"

    @pytest.fixture()
    def handler(self):
        return FileHandler()

    # def setup_method(self):
    #     self.file_handler = FileHandler()
    # exceptions??

    @pytest.mark.test_read_from_file
    def test_expect_error_message_when_file_path_is_invalid(self, handler):
        with patch("builtins.print") as mock_print:
            handler.read_from_file("invalid/file/path")
            mock_print.assert_called_with(
                "File not found. Please check the path and ensure the file exists."
            )

    @pytest.mark.test_read_from_file
    def test_should_return_correct_dict_when_file_path_to_json_file_is_provided(
        self, handler
    ):
        file_path = "test_json.json"

        test_dict = {
            "1": {"text": "tekst", "status": "decoded"},
            "2": {"text": "kolejny tekst", "status": "encoded"},
            "3": {"text": "jakis tekst", "status": "encoded"},
            "4": {"text": "inny tekst", "status": "decoded"},
        }

        with open(file_path, "w") as json_file:
            json.dump(test_dict, json_file, indent=4)

        assert handler.read_from_file(file_path) == test_dict

    # @pytest.mark.test_read_from_file
    # def test_expect_exception_when_file_is_empty(self, handler):
    # pass

    @pytest.mark.test_save_to_file
    def test_should_be_saved_correctly_when_appended_to_existing_file(self, handler):
        file_path = "test_json.json"

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

        with open(file_path, "w") as json_file:
            json.dump(test_dict, json_file, indent=4)

        handler.save_to_file(file_path, appended_dict)

        with open(file_path, "r") as json_file:
            json_dict = json.load(json_file)

        assert json_dict == returned_dict

    @pytest.mark.test_save_to_file
    def test_should_be_saved_correctly_when_saved_to_new_file(self, handler):
        file_path = "new.json"

        test_dict = {
            "1": {"text": "tekst", "status": "decoded"},
            "2": {"text": "kolejny tekst", "status": "encoded"},
            "3": {"text": "jakis tekst", "status": "encoded"},
            "4": {"text": "inny tekst", "status": "decoded"},
        }

        handler.save_to_file(file_path, test_dict)

        with open(file_path, "r") as json_file:
            json_dict = json.load(json_file)

        assert json_dict == test_dict

    # def teardown_method(self):
    #     if os.path.exists(self.FILE_PATH):

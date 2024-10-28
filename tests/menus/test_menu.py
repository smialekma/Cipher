import pytest
from unittest.mock import patch, call
from src.menus.menu import Menu


class TestMenu:

    @pytest.fixture()
    def menu(self):
        return Menu()

    def test_should_display_main_menu_options_in_correct_order(self, menu):
        with patch("builtins.print") as mock_print:
            menu.main()
            mock_print.assert_has_calls(
                [
                    call("1 - Enter a text"),
                    call("2 - Load from a json file"),
                    call("3 - Save to a json file"),
                    call("4 - Exit"),
                ]
            )

    def test_should_display_encode_decode_options_in_correct_order(self, menu):
        with patch("builtins.print") as mock_print:
            menu.encode_or_decode()
            mock_print.assert_has_calls([call("1 - Encode"), call("2 - Decode")])

    def test_should_display_choose_cipher_options_in_correct_order(self, menu):
        with patch("builtins.print") as mock_print:
            menu.choose_cipher()
            mock_print.assert_has_calls([call("1 - ROT13"), call("2 - ROT47")])

    @pytest.mark.test_get_number
    def test_expect_error_message_when_string_is_entered(self, menu):
        with patch("builtins.input", side_effect=["hej", "4"]):
            with patch("builtins.print") as mock_print:
                menu.get_number()
                mock_print.assert_has_calls([call("Incorrect value!")])

    @pytest.mark.test_get_number
    def test_should_return_number_entered_into_input(self, menu):
        with patch("builtins.input", return_value="1"):
            assert menu.get_number() == 1

    @pytest.mark.test_get_text
    def test_should_return_string_for_number(self, menu):
        with patch("builtins.input", return_value="1"):
            assert menu.get_text() == "1"

    @pytest.mark.test_get_text
    def test_get_text_should_return_correct_value_for_input(self, menu):
        with patch("builtins.input", return_value="Tekst do zaszyfrowania."):
            assert menu.get_text() == "Tekst do zaszyfrowania."

    @pytest.mark.test_get_file_path
    def test_get_file_path_should_return_correct_value_for_input(self, menu):
        with patch("builtins.input", return_value="C:/Users/User/cipher-files"):
            assert menu.get_file_path() == "C:/Users/User/cipher-files"

    def test_should_correctly_display_original_and_processed_texts(self, menu):
        with patch("builtins.print") as mock_print:
            menu.show_processed_text("Kobyła ma mały bok", "Xbolłn zn znłl obx.")
            mock_print.assert_has_calls(
                [
                    call("Original text: Kobyła ma mały bok"),
                    call("Processed text: Xbolłn zn znłl obx."),
                ]
            )

    def test_should_correctly_display_get_back_menu(self, menu):
        with patch("builtins.print") as mock_print:
            menu.get_back_or_exit()
            mock_print.assert_has_calls(
                [
                    call("Do you want to:"),
                    call("1 - Get back to the main menu?"),
                    call("2 - Exit?"),
                ]
            )

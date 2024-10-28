from unittest.mock import patch, call

from src.run import main


def test_should_correctly_start_a_program():
    with patch("builtins.print") as mock_print:
        with patch("builtins.input", return_value="4"):
            main()
            mock_print.assert_has_calls(
                [
                    call("Welcome to the Cipher project."),
                    call("1 - Enter a text"),
                    call("2 - Load from a json file"),
                    call("3 - Save to a json file"),
                    call("4 - Exit"),
                ]
            )

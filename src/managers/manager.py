from json import JSONDecodeError
from typing import Callable

from src.files.file_handler import FileHandler
from src.menus.menu import Menu
from src.helpers.text import Text

from src.decoders.decoder_factory import DecoderFactory, Rot13Factory, Rot47Factory
from src.helpers.buffer import Buffer
from src.menus.menu_options import MenuOption
from src.decoders.cipher_type import CipherType
from src.helpers.text_status import TextStatus


class Manager:

    def __init__(self, menu: Menu, buffer: Buffer, file_handler: FileHandler):
        self.menu = menu
        self.buffer = buffer
        self.filehandler = file_handler

    def start(self) -> bool:
        self.menu.main()
        options = {
            MenuOption.PROCESS_USER_INPUT.value: self.process_user_input,
            MenuOption.PROCESS_FROM_FILE.value: self.process_texts_from_file,
            MenuOption.SAVE_TO_FILE.value: self.save_to_file,
            MenuOption.EXIT.value: self._exit,
        }
        return self.execute(options)

    def execute(self, options: dict[MenuOption | int, Callable]) -> bool:
        """Asks user for a number and executes it."""
        try:
            number = self.menu.get_number()
            choice = options[number]()
            if choice is False:
                return False
            return True
        except KeyError:
            print("You entered an incorrect number.")
            return self.start()
        except ValueError:
            self.start()

    def save_to_file(self):
        """saves all texts used in a program to a json file"""
        file_path = self.menu.get_file_path()
        dict_to_save = self.buffer.buffer_to_dict()
        try:
            self.filehandler.save_to_file(file_path, dict_to_save)
            print("The texts have been saved.")
        except IOError:
            self.start()

    def read_from_file(self):
        """Asks user to enter file path, loads texts from a json file."""
        file_path = self.menu.get_file_path()
        try:
            dict_from_file = self.filehandler.read_from_file(file_path)
            self.buffer.dict_to_buffer(dict_from_file)
        except FileNotFoundError:
            self.start()
        except JSONDecodeError:
            self.start()

    def _get_status(self) -> TextStatus | bool:
        """Asks user if they want to encode/decode a text and returns their choice
        in the form of a dataclass attribute ('decoded/encoded')."""
        self.menu.encode_or_decode()
        try:
            number = self.menu.get_number()
            options = {1: TextStatus.ENCODED.value, 2: TextStatus.DECODED.value}
            return options[number]
        except KeyError:
            print("You entered an incorrect number.")
            return self.start()

    def _get_rot(self) -> CipherType | bool:
        """Asks user what cipher they want to use and returns their choice."""
        self.menu.choose_cipher()
        try:
            number = self.menu.get_number()
            options = {1: CipherType.ROT13.value, 2: CipherType.ROT47.value}
            return options.get(number)
        except KeyError:
            print("You entered an incorrect number.")
            return self.start()

    def _get_decoder_factory(self, rot_type: CipherType) -> "DecoderFactory":
        """Returns a specific decoder factory based on a CipherType value."""
        rot_options = {
            CipherType.ROT13.value: Rot13Factory(),
            CipherType.ROT47.value: Rot47Factory(),
        }
        return rot_options.get(rot_type)

    def process_user_input(self) -> bool:
        """asks user to type a text, choose the cypher type
        and if they want to decode or encode. Then shows the decoded/encoded text."""
        text = self.menu.get_text()
        status = self._get_status()
        rot_type = self._get_rot()

        decoder_factory = self._get_decoder_factory(rot_type)

        decoder = decoder_factory.create_decoder()

        status_options = {
            TextStatus.ENCODED.value: decoder.encode,
            TextStatus.DECODED.value: decoder.decode,
        }
        processed_text = status_options.get(status)(text)

        self.menu.show_processed_text(text, processed_text)

        text_obj = Text(text=processed_text, status=status, rot_type=rot_type)
        self.buffer.add_to_buffer(text_obj)

        self.menu.get_back_or_exit()
        options = {1: self.start, 2: self._exit}
        return self.execute(options)

    def process_texts_from_file(self) -> bool:
        """Loads texts from a json file, asks user if they want to decode/encode
        and to choose a cipher, then processes appropriate texts."""
        self.read_from_file()
        print("The text(s) has been loaded.")
        status = self._get_status()
        rot = self._get_rot()
        decoder_factory = self._get_decoder_factory(rot_type=rot)
        decoder = decoder_factory.create_decoder()

        for text in self.buffer.buffer:
            if text.status != status:
                status_options = {
                    TextStatus.ENCODED.value: decoder.encode,
                    TextStatus.DECODED.value: decoder.decode,
                }
                processed_text = status_options.get(status)(text.text)
                self.menu.show_processed_text(text.text, processed_text)

        self.menu.get_back_or_exit()
        options = {1: self.start, 2: self._exit}
        return self.execute(options)

    def _exit(self) -> bool:
        return False

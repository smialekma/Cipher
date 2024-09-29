from src.files.file_handler import FileHandler
from src.menus.menu import Menu
from src.decoders.text import Text

from src.decoders.decoder_factory import Rot13Factory, Rot47Factory
from src.helpers.buffer import Buffer
from typing import Callable


class Manager:

    def __init__(self):
        self.menu = Menu()
        self.buffer = Buffer()
        self.filehandler = FileHandler()

    def start(self):
        self.show_menu()
        options = {
            1: self.process_user_input,
            2: self.process_texts_from_file,
            3: self.save_to_file,
            4: self.exit,
        }
        self.execute(options)

    def show_menu(self):
        """shows main menu"""
        self.menu.main()

    def execute(self, options: dict[int, Callable]) -> Callable:
        """Asks user for a number and executes it."""
        number = self.menu.get_number()
        choice = options.get(number)()
        return choice

    def save_to_file(self):
        """saves all texts used in a program to a json file"""
        file_path = self.menu.get_file_path()
        dict_to_save = self.buffer.buffer_to_dict()
        self.filehandler.save_to_file(file_path, dict_to_save)
        print("The texts have been saved.")

    def read_from_file(self):
        """Asks user to enter file path, loads texts from a json file."""
        file_path = self.menu.get_file_path()
        dict_from_file = self.filehandler.read_from_file(file_path)
        self.buffer.dict_to_buffer(dict_from_file)

    # def transform(self, text: Text) -> str:
    # rot_options = {"rot13": Rot13Factory(), "rot47": Rot47Factory()}
    # rot_factory = rot_options.get(text.rot_type)
    # rot = rot_factory.create_decoder()
    # if text.status == "decoded":
    #   return rot.encode(text.text)
    # if text.status == "encoded":
    #   return rot.decode(text.text)

    def _get_status(self) -> str:
        """Asks user if they want to encode/decode a text and returns their choice
        in the form of a dataclass attribute ('decoded/encoded')."""
        self.menu.encode_or_decode()
        number = self.menu.get_number()
        options = {1: "encoded", 2: "decoded"}
        return options.get(number)

    def _get_rot(self) -> str:
        """Asks user what cipher they want to use and returns their choice."""
        self.menu.choose_cipher()
        number = self.menu.get_number()
        options = {1: "rot13", 2: "rot47"}
        return options.get(number)

    def process_user_input(self):
        """asks user to type a text, choose the cypher type
        and if they want to decode or encode. Then shows the decoded/encoded text."""
        text = self.menu.get_text()
        status = self._get_status()
        rot_type = self._get_rot()

        rot_options = {"rot13": Rot13Factory(), "rot47": Rot47Factory()}
        rot_factory = rot_options.get(rot_type)
        rot = rot_factory.create_decoder()

        status_options = {"encoded": rot.encode, "decoded": rot.decode}
        processed_text = status_options.get(status)(text)

        self.menu.show_processed_text(text, processed_text)

        text_obj = Text(text=processed_text, status=status, rot_type=rot_type)
        self.buffer.add_to_buffer(text_obj)

        self.menu.get_back_or_exit()
        options = {1: self.start, 2: self.exit}
        self.execute(options)

    def process_texts_from_file(self):
        """Loads texts from a json file, asks user if they want to decode/encode
        and to choose a cipher, then processes appropriate texts."""
        self.read_from_file()
        print("The text(s) has been loaded.")
        status = self._get_status()
        rot = self._get_rot()
        for text in self.buffer.buffer:
            if text.status != status:
                status_options = {"encoded": rot.encode, "decoded": rot.decode}
                processed_text = status_options.get(status)(text.text)
                self.menu.show_processed_text(text.text, processed_text)
                print()

        self.menu.get_back_or_exit()
        options = {1: self.start, 2: self.exit}
        self.execute(options)

    def exit(self):
        exit()

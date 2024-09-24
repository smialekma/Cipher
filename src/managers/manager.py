from src.files.file_handler import FileHandler
from src.menus.menu import Menu

# from src.decoders.decoder_factory import DecoderFactory
# from src.decoders.rot_decoder import Rot47Decoder, Rot13Decoder
from src.helpers.buffer import Buffer
from typing import Callable


class Manager:

    def __init__(self):
        self.menu = Menu()
        self.buffer = Buffer()
        self.filehandler = FileHandler()

    def start(self):
        print("Welcome to the Cipher project.")
        self.show_menu()
        self.execute()

    def show_menu(self):
        """shows main menu"""
        self.menu.main()

    def execute(self, options: dict[int, Callable]):
        number = self.menu.get_number()
        choice = options.get(number)()
        return choice

    def save_to_file(self, file_path: str):
        """saves all texts used in a program to a json file"""
        dict_to_save = self.buffer.buffer_to_dict()
        self.filehandler.save_to_file(file_path, dict_to_save)

    def get_user_input(self):
        """asks user to type a text,
        choose the cypher type and if the want to decode or encode."""
        self.menu.get_text()
        self.menu.encode_or_decode()
        self.menu.get_number()

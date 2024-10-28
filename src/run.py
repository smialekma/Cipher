from src.managers.manager import Manager
from src.menus.menu import Menu
from src.files.file_handler import FileHandler
from src.helpers.buffer import Buffer


def main():
    print("Welcome to the Cipher project.")

    manager = Manager(menu=Menu(), buffer=Buffer(), file_handler=FileHandler())

    while manager.start():
        pass


if __name__ == "__main__":
    main()

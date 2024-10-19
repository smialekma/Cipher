from managers.manager import Manager
from menus.menu import Menu
from files.file_handler import FileHandler
from helpers.buffer import Buffer


def main():
    print("Welcome to the Cipher project.")

    manager = Manager(menu=Menu(), buffer=Buffer(), file_handler=FileHandler())

    # while manager.start():
    #     pass
    # manager.start()
    while manager.start():
        pass


if __name__ == "__main__":
    main()

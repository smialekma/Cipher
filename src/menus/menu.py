class Menu:

    def main(self) -> None:
        """This function displays main menu options."""
        print("1 - Enter a text")
        print("2 - Load from a json file")
        print("3 - Save to a json file")
        print("4 - Exit")

    def encode_or_decode(self) -> None:
        """This function asks a user to choose if they want encode or decode a text"""
        print("1 - Encode")
        print("2 - Decode")

    def choose_cipher(self) -> None:
        """This function shows a menu where you can choose a cipher."""
        print("Choose cipher:")
        print("1 - ROT13")
        print("2 - ROT47")

    def get_choice(self) -> int:
        """Asks for a user input (number)."""
        try:
            choice = int(input("Enter a number: "))
            return choice
        except ValueError:
            print("Incorrect value!")
            self.get_choice()

    def get_text(self) -> str:
        """Asks for a user input (string)."""
        text = str(input("Enter a text: "))
        return text

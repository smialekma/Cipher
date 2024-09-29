class Menu:

    def main(self) -> None:
        """This method displays main menu options."""
        print("1 - Enter a text")
        print("2 - Load from a json file")
        print("3 - Save to a json file")
        print("4 - Exit")

    def encode_or_decode(self) -> None:
        """This method asks a user to choose if they want to encode or decode a text"""
        print("1 - Encode")
        print("2 - Decode")

    def choose_cipher(self) -> None:
        """This method shows a menu where you can choose a cipher."""
        print("Choose cipher:")
        print("1 - ROT13")
        print("2 - ROT47")

    def get_number(self) -> int:
        """Asks for a user input (number)."""
        try:
            choice = int(input("Enter a number: "))
            return choice
        except ValueError:
            print("Incorrect value!")
            self.get_number()

    def get_text(self) -> str:
        """Asks for a user input (string)."""
        text = str(input("Enter a text: "))
        return text

    def get_file_path(self) -> str:
        """Asks for a file path."""
        file_path = str(input("Enter a file path: "))
        return file_path

    def show_processed_text(self, original_text: str, processed_text: str) -> None:
        """Displays original and decoded/encoded text."""
        print(f"Original text: {original_text}")
        print(f"Processed text: {processed_text}")

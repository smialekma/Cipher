import json
import os


class FileHandler:

    def read_from_file(self, file_path: str) -> dict:
        """This function creates a dictionary from a json file"""
        try:
            with open(file_path, "r") as json_file:
                json_dict = json.load(json_file)
                return json_dict
        except FileNotFoundError:
            print("File not found. Please check the path and ensure the file exists.")

    def save_to_file(self, file_path: str, dict_to_save: dict) -> None:
        """This function saves a dictionary into a json file"""

        if os.path.exists(file_path):
            existing_dict = self.read_from_file(file_path)
            for key, value in dict_to_save.items():
                existing_dict[key] = value
            dict_to_save = existing_dict

        with open(file_path, "w") as json_file:
            json.dump(dict_to_save, json_file, indent=4)

        # TODO: zmienić numerację


if __name__ == "__main__":
    my_dict = {
        3: {"text": "jakis tekst", "status": "encrypted"},
        4: {"text": "inny tekst", "status": "decrypted"},
    }
    file_path = "new.json"
    # file_path = "C:/Users/smial/OneDrive/Pulpit/new.json"
    # file_path2 = "C:/Users/smial/OneDrive/Pulpit/new2.json"

    filehandler = FileHandler()
    filehandler.save_to_file(file_path, my_dict)

    print(filehandler.read_from_file(file_path))
    # filehandler.read_from_file(file_path2)

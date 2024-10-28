import json
import os
from json import JSONDecodeError


class FileHandler:
    def read_from_file(self, file_path: str) -> dict[str, dict[str, str]]:
        """This function creates a dictionary from a json file"""
        try:
            with open(file_path, "r") as json_file:
                json_dict = json.load(json_file)
                return json_dict
        except FileNotFoundError:
            print("File not found. Please check the path and ensure the file exists.")
        except JSONDecodeError:
            print("Invalid file. Please check the path and ensure the file is valid.")

    def save_to_file(
        self, file_path: str, dict_to_save: dict[str, dict[str, str]]
    ) -> None:
        """This function saves a dictionary into a json file"""

        if os.path.exists(file_path):
            existing_dict = self.read_from_file(file_path)
            num_of_keys = len(existing_dict.keys())
            for count, (key, value) in enumerate(dict_to_save.items(), start=1):
                number = str(num_of_keys + count)
                existing_dict[number] = value

            dict_to_save = existing_dict

        try:
            with open(file_path, "w") as json_file:
                json.dump(dict_to_save, json_file, indent=4)
        except IOError:
            print("No such directory!")

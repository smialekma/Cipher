import json
import os
from dataclasses import asdict
from text import Text


class FileHandler:

    def read_from_file(self, file_path):
        """This function creates text object from a json file"""
        try:
            with open(file_path, "r") as json_file:
                json_dict = json.load(json_file)
                return Text(**json_dict)
        except FileNotFoundError:
            print("File not found. Please check the path and ensure the file exists.")

    def save_to_file(self, file_path, text_object):
        """This function saves text object in a json file"""
        text_dict = asdict(text_object)

        if os.path.exists(file_path):
            with open(file_path, 'a') as json_file:
                json.dump(text_dict, json_file)

        else:
            with open(file_path, 'w') as json_file:
                json.dump(text_dict, json_file)
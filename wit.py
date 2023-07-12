import os

from file_handler import FileHandler
from wit_exception import WitException


class Wit:
    @classmethod
    def create_instance(cls):
        return cls()

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        print("got to init")
        if Wit.validate_is_wit_repo():
            # handle nested wits
            raise WitException("the init repository already exists")
        else:
            FileHandler.create_wit()

    @staticmethod
    def move_to_staging(path):
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(path, target_path)

    @staticmethod
    def add(path):
        if not Wit.validate_is_wit_repo():
            raise WitException("no repository exists")
        # if args[0] == '.':
        #     full_path = os.path.abspath(os.getcwd())
        #     print(full_path)
        # else:
        #     full_path = FileHandler.validate_path(args[0])
        #     print(full_path)
        Wit.move_to_staging(path)

    @staticmethod
    def commit(args):
        pass

import os

from file_handler import FileHandler
from wit_interface import WitInterface


class Wit(WitInterface):
    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            # handle nested wits
            pass
        else:
            FileHandler.create_wit()

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        if args[0] == '.':
            full_path = os.path.abspath(os.getcwd())#????????????????????????????????
        else:
            full_path = FileHandler.validate_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit(args):
        pass

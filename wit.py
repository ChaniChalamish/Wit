import os
from logger import Logger
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
        try:
            print("got to init")
            if Wit.validate_is_wit_repo():
                # handle nested wits
                raise WitException("the init repository already exists")
            else:
                FileHandler.create_wit()
         except WitException as e:
              Logger.logger.debug(f"{__name__}  {e}")

    @staticmethod
    def move_to_staging(path):
        Logger.logger.debug(f"{__name__} in move_to_staging")
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(path, target_path)

    @staticmethod
    def add(path):
        try:
            if not Wit.validate_is_wit_repo():
                raise WitException("no repository exists")
            Logger.logger.info(f"{__name__}  add action was activated with {args[0]} files/folders")
            Wit.move_to_staging(path)
         except WitException as e:
            Logger.logger.debug(f"{__name__} {e}")

    @staticmethod
    def commit(args):
        pass

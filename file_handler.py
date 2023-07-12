import logging
import os
import shutil

from wit_exception import WitException

logging_format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
logging.basicConfig(format=logging_format, level=logging.DEBUG)
base_logger = logging.getLogger(__name__)


class FileHandler:
    _working_directory = None
    base_path = None

    @staticmethod
    def make_log():
        base_logger.debug("make log")

    # base path is location of .wit folder

    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        # path is the directory where .wit older exists
        found, path = FileHandler.find_wit()
        print(found, path)
        if found:
            FileHandler._base_path = path
            return found

    @staticmethod
    def find_wit():
        file_name = ".wit"
        # file to be searched
        cur_dir = os.getcwd()  # Dir from where search starts can be replaced with any path

        while True:
            file_list = os.listdir(cur_dir)
            parent_dir = os.path.dirname(cur_dir)
            print(parent_dir)

            if file_name in file_list:
                path = os.path.join(parent_dir, "Wit//.wit")
                return True, path
            else:
                if cur_dir == parent_dir:  # if dir is root dir
                    return False, None
                else:
                    cur_dir = parent_dir

    @classmethod
    def working_directory(cls):
        if cls._working_directory:
            return cls._working_directory
        cls._working_directory = os.getcwd()
        return cls._working_directory

    @staticmethod
    def check_if_directory_exists(target_directory):
        cur_path = " "
        while True:
            cur_path = os.path.join(cur_path, "..")
            file_or_folder_path = os.path.abspath(cur_path)
            print(os.path.splitdrive(file_or_folder_path)[0])
            # if got to driver directory so our direction not found
            if str(f"{os.path.splitdrive(file_or_folder_path)[0]}\\") == file_or_folder_path:
                return False, None
            for (dirpath, dirnames, filenames) in os.walk(cur_path):
                if target_directory in dirnames:
                    return True, file_or_folder_path
                if target_directory in filenames:
                    return True, file_or_folder_path

    @staticmethod
    def check_if_directory_exists1(target_directory):
        print(target_directory)
        cur_path = " "
        while True:
            print(os.getcwd())
            file_or_folder_path = os.path.abspath(cur_path)
            print("got to check existance")
            print(file_or_folder_path, "cur", cur_path)
            print(os.path.splitdrive(file_or_folder_path)[0])
            # if got to driver directory so our direction not found
            if str(f"{os.path.splitdrive(file_or_folder_path)[0]}\\") == file_or_folder_path:
                return False, None
            for (dirpath, dirnames, filenames) in os.walk(cur_path):
                if target_directory in dirnames:
                    return True, file_or_folder_path
                # if target_directory in filenames:
                #     return True, file_or_folder_path
            cur_path = os.path.join(cur_path, "..")

    @staticmethod
    def create_wit():
        img_directory = "images"
        staging_directory = "staging_area"
        parent_dir = f"./.wit"
        img_path = os.path.join(parent_dir, img_directory)
        staging_path = os.path.join(parent_dir, staging_directory)

        try:
            os.makedirs(img_path, exist_ok=True)
            os.makedirs(staging_path, exist_ok=True)
            base_logger.info(f"{parent_dir} ,{staging_directory}, {img_directory} were successfully created")
        except OSError as error:
            base_logger.error(f"could not create {parent_dir} ,{staging_directory}, {img_directory}")
            print(f"Directory '%s' can not be created {error}")

    @classmethod
    def validate_path(cls, path):
        print(type(cls.working_directory()), path)
        # full_path = os.path.join(cls.working_directory(), path)
        full_path = os.path.normpath(os.path.join(cls.working_directory(), path))
        print(full_path)
        if not os.path.exists(full_path):
            raise ValueError("the path does not exists or not in the working directory")
        return True

    @classmethod
    def copy_item(cls, origin, target):
        correct_target = os.path.join(target, origin.split("\\")[-1])
        origin = os.path.abspath(origin)
        if not cls.validate_path(origin) or not cls.validate_path(target):
            raise WitException("the path is not valid")
        # TODO check if the targtte exists
        full_path = os.path.normpath(os.path.join(target, origin))
        if cls.check_if_directory_exists(full_path)[0]:
            raise WitException(f"the file already exists on the target location {full_path}")
        if os.path.isdir(origin):
            # TODO - copy it without creating new folder
            shutil.copytree(origin, correct_target)
            # base_logger.info("")
            return True
        elif os.path.isfile(origin):
            shutil.copyfile(origin, correct_target)
            return True
        else:
            print(origin)
            print(os.path.isfile(origin))
            return "opps"


# print(FileHandler.find_base_path())
# print(FileHandler.check_if_directory_exists('main.py'))
# print(FileHandler.find_wit())

# print(FileHandler.copy_item(".//txt_file1.txt", ".//.wit//staging_area"))

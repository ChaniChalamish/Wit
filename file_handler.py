import os
import shutil


class FileHandler:

    def __init__(self):
        self._base_path = None
        self._working_directory = None

    @property
    def base_path(self):
        if self._base_path:
            return self._base_path

        found, path = FileHandler.check_if_folder_exists('.wit')
        if found:
            self._base_path = path
            return found
        # TODO: handle not wit repo
        raise Exception("Not a wit repository")

    @property
    def working_directory(self):
        if self._working_directory:
            return self._working_directory
        return self._working_directory

    @staticmethod
    def check_if_folder_exists(target_directory):
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
    def create_wit():
        img_directory = "images"
        staging_directory = "staging_area"
        parent_dir = f"./.wit"
        img_path = os.path.join(parent_dir, img_directory)
        staging_path = os.path.join(parent_dir, staging_directory)

        try:
            os.makedirs(img_path, exist_ok=True)
            os.makedirs(staging_path, exist_ok=True)
        except OSError as error:
            print(f"Directory '%s' can not be created {error}")

    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        # TODO: find first dir's path with .wit in it
        found = False
        # TODO: handle not wit repo
        # raise Exception("Not a wit repository")

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            raise ValueError("the path does not exists")
        return True

    @classmethod
    def copy_item(cls, origin, target):
        # if not cls.validate_path(origin) and cls.validate_path(target):
        #     return False
        if os.path.isdir(origin):
            # TODO - copy it without creating new folder
            correct_target = os.path.join(target, 'new_folder')
            shutil.copytree(origin, correct_target)
            return True
        elif os.path.isfile(origin):
            shutil.copyfile(origin, target)
            return True


# f = FileHandler()
# print(f.validate_path())

print(FileHandler.copy_item(".//text_file", ".//.wit//staging_area"))

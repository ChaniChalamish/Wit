import os


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

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            pass
            # TODO: handle file doesn't exist

    @classmethod
    def copy_item(cls, origin, target):
        pass

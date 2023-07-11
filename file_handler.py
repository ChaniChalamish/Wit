import os
import shutil


class FileHandler:
    base_path = None
    working_directory = None

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
            correct_target = os.path.join(target, 'a')
            shutil.copytree(origin, correct_target)  # TODO - create new dir?
            return True
        elif os.path.isfile(origin):
            shutil.copyfile(origin, target)
            return True


# f = FileHandler()
# print(f.validate_path())

print(FileHandler.copy_item(".//text_file", ".//.wit//staging_area"))

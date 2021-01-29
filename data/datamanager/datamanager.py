import os
from typing import List, Optional

import yaml

import data.path
from data.logger.logwindow import LogWindow


class DataManager:
    def __init__(self):
        self.autorank_folder: Optional[str] = None
        self.loaded_paths: List[data.path.Path] = []

    def set_autorank_folder_path(self, path: str) -> None:
        """
        Set the active folder of Autorank.

        :param path: Path to set it to
        """
        assert os.path.isdir(path), f"Path {path} is not a directory!"

        assert self.is_valid_autorank_folder(path), f"Path {path} is not an Autorank directory!"

        self.autorank_folder = path

        LogWindow.log_message(f"Set Autorank folder to {path}")

    def is_valid_autorank_folder(self, path: str) -> bool:
        """
        Check whether a path is a valid Autorank folder. A folder is valid if it contains a Settings.yml and Paths.yml

        :param path: Path of the folder to check
        :return: true if it is a valid Autorank folder. False if not.
        """

        # Check if Paths.yml and Settings.yml exist.
        if not os.path.exists(os.path.join(path, "Paths.yml")):
            return False

        if not os.path.exists(os.path.join(path, "Settings.yml")):
            return False

        # If both exist, we assume it's alright
        return True

    def load_paths_file(self) -> int:
        """
        Loads the Paths.yml file into memory, overwriting any data that was previously in memory.

        :return: The number of paths loaded. -1 if we could not find a Paths.yml file
        """

        # Check if we have a loaded autorank folder
        if self.autorank_folder is None:
            return -1

        # Check if it is a valid folder
        if not self.is_valid_autorank_folder(self.autorank_folder):
            return -1

        # Clear the previous data
        self.loaded_paths.clear()

        LogWindow.log_message("Loading new Paths.yml file.")

        with open(os.path.join(self.autorank_folder, "Paths.yml")) as paths_file:
            paths_data = yaml.load(paths_file, Loader=yaml.FullLoader)

            # Load paths and their data
            for path_name, path_data in paths_data.items():
                loaded_path = data.path.Path.load_from_yaml(path_name, path_data)

                LogWindow.log_message(f"Loaded path '{loaded_path.configuration_name}' with {len(loaded_path.prerequisites)} prerequisite(s), {len(loaded_path.requirements)} requirement(s) and {len(loaded_path.results)} result(s).")

                self.loaded_paths.append(loaded_path)

        LogWindow.log_message(f"Loaded {len(self.loaded_paths)} paths from Paths.yml file.")



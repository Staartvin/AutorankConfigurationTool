from typing import List, Optional, Dict

import data.requirement
import data.result
import data.pathdata


class Path:
    def __init__(self, config_name: str):
        self.prerequisites: List[data.requirement.Requirement] = []
        self.requirements: List[data.requirement.Requirement] = []
        self.results: List[data.result.Result] = []
        self.results_upon_choosing: List[data.result.Result] = []

        self.configuration_name: str = config_name

        self.display_name: Optional[str] = None

        self.repeatable: bool = False

        self.auto_assign: bool = False

        self.only_show_when_eligible: bool = False

        self.cooldown: Optional[str] = None

        self.allow_partial_completion: bool = True

        self.store_progress: bool = False

    @staticmethod
    def load_from_yaml(name: str, yaml_data: Dict) -> "Path":
        """
        Load a path from YAML data (assuming it's a dictionary)

        :param name: Name of the path to create
        :param yaml_data: Data to load the path from
        :return: a Path instance with the data from the given YAML dict.
        """
        path = Path(name)

        defined_prerequisites: Dict = yaml_data.get("prerequisites", {})

        for prerequisite_name, prerequisite_data in defined_prerequisites.items():
            prerequisite: data.requirement.Requirement = data.pathdata.PathData.create_empty_requirement(prerequisite_name)

            prerequisite.load_from_yaml(prerequisite_data)

            path.prerequisites.append(prerequisite)

        return path





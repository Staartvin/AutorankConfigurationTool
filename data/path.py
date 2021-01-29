from typing import List, Optional, Dict

import data.requirement
import data.result
import data.pathdata
from data.logger.logwindow import LogWindow


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

        # Obtain prerequisites and requirements that are defined in the YAML dictionary
        defined_prerequisites: Dict = yaml_data.get("prerequisites", {})
        defined_requirements: Dict = yaml_data.get("requirements", {})

        # Load prerequisites
        for prerequisite_name, prerequisite_data in defined_prerequisites.items():
            # Match prerequisite based on name
            prerequisite: data.requirement.Requirement = data.pathdata.PathData.create_empty_requirement(prerequisite_name)

            # Check if prerequisite could be found
            if prerequisite is None:
                LogWindow.log_message(f"Could not identify prerequisite '{prerequisite_name}' of path '{name}'!")
                continue

            # If the data is not a dict, we force it to a string
            if not isinstance(prerequisite_data, Dict):
                prerequisite_data = str(prerequisite_data)

            # Fill the prerequisite with data
            prerequisite.load_from_yaml(prerequisite_data)

            # Add the prerequisite to the path.
            path.prerequisites.append(prerequisite)

        # Load requirements
        for requirement_name, requirement_data in defined_requirements.items():
            # Match requirement based on name
            requirement: data.requirement.Requirement = data.pathdata.PathData.create_empty_requirement(
                requirement_name)

            # Check if prerequisite could be found
            if requirement is None:
                LogWindow.log_message(f"Could not identify requirement '{requirement_name}' of path '{name}'!")
                continue

            # If the data is not a dict, we force it to a string
            if not isinstance(requirement_data, Dict):
                requirement_data = str(requirement_data)

            # Fill the requirement with data
            requirement.load_from_yaml(requirement_data)

            # Add the requirement to the path.
            path.requirements.append(requirement)

        return path





from abc import ABC, abstractmethod

from typing import List, Optional, Dict

import data.result
from data.logger.logwindow import LogWindow


class Requirement(ABC):

    def __init__(self):
        self.type: "RequirementType" = None
        self.optional: bool = False

        self.results_after_completing: List[data.result.Result] = []
        self.custom_description: Optional[str] = None

        self.value: Optional[str] = None

    @abstractmethod
    def default_description(self) -> str:
        return ""

    def load_from_yaml(self, yaml_data: Dict):
        if isinstance(yaml_data, Dict):
            self.value = yaml_data.get("value", None)
        elif isinstance(yaml_data, str):
            self.value = yaml_data
        else:
            LogWindow.log_message(f"Could not identify type of data passed to requirement '{self.type}': {yaml_data}")






from abc import ABC, abstractmethod

from typing import List, Optional, Dict

import data.result


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
        self.value = yaml_data.get("value", None)






from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class ResultType(Enum):
    BASE_RESULT = 1


class Result(ABC):

    def __init__(self):
        self.type: ResultType = ResultType.BASE_REQUIREMENT

    @abstractmethod
    def default_description(self) -> str:
        return ""

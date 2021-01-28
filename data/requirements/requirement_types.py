import enum
from typing import List, Optional

import data.requirements.requirements as requirements


class RequirementType(enum.Enum):
    """
    This a type of requirement. Note that this is a enum, but it has two member variables. These member variables
    are used to keep track of identifiers that can be used in the Paths.yml file. The other member variable is used to
    be able to create instances of requirements that implement the abstract Requirement class.
    """

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, identifiers: [], requirement):
        # Identifiers that can be used in the Paths.yml
        self.config_identifiers: List[str] = identifiers

        # Class that is used to create a new instance of the implemented requirement
        self.requirement_class: "Requirement" = requirement

    @staticmethod
    def get_requirement_from_identifier(identifier: str) -> Optional["RequirementType"]:
        """
        Find an instance of a RequirementType for a given identifier

        :param identifier: Identifier to look up
        :return: the corresponding RequirementType or None if none was matching
        """
        requirement: "RequirementType"
        for requirement in RequirementType:
            if identifier in requirement.config_identifiers:
                return requirement
        return None

    # Define requirement types
    IN_GROUP_REQUIREMENT = ["in group"], requirements.InGroupRequirement

import re
from typing import Dict, List, Optional

from data.requirement import Requirement
from data.requirements.requirement_types import RequirementType


class PathData:

    @staticmethod
    def create_empty_requirement(identifier_name: str) -> Optional["Requirement"]:
        """
        Create an empty requirement instance for a given identifier. If there is no requirement with the given identifier
        , None will be returned

        :param identifier_name: Identifier to use for looking for the requirement
        :return: an empty requirement instance (or None) if nothing was found.
        """

        cleaned_identifier_name = re.sub(r'\d+', '', identifier_name).strip()

        # Do a lookup to see if we can find a requirement type for the given identifier
        requirement_type: RequirementType = RequirementType.get_requirement_from_identifier(cleaned_identifier_name)

        # If we found nothing, we stop
        if requirement_type is None:
            return None

        # Create empty requirement instance
        empty_requirement: Requirement = requirement_type.requirement_class()

        # Set the type of requirement
        empty_requirement.type = requirement_type

        return empty_requirement

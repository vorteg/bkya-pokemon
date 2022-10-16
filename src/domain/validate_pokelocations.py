from typing import List, Tuple


class ValidatePokeLoc:
    """Class with method to validate if the Pokemon Location exist"""

    @staticmethod
    def validading_loc(locations_available: List, finding_locations: List) -> Tuple:
        valid_loc = []
        no_valid_loc = []
        for location in finding_locations:
            if location in locations_available:
                valid_loc.append(location)
            else:
                no_valid_loc.append(location)
        return valid_loc, no_valid_loc

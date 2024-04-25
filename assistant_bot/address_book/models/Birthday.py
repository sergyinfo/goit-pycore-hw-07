import re
from datetime import datetime
from .Field import Field

class Birthday(Field):
    """
    Class for birthday fields

    Attributes:
    value -- the value of the field

    Methods:
    __init__ -- initializes the field
    __str__ -- returns the string representation of the field
    __validate -- validates the field value
    """
    def __init__(self, value):
        """
        Initializes the field

        Arguments:
        value -- the value of the field

        Returns:
        None

        Raises:
        ValueError -- if the value is invalid
        """
        super().__init__(value)

        message = "Invalid date format. Use DD.MM.YYYY"

        try:
            # validate before assign
            if not self.__validate(value):
                raise ValueError(message)

            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError(message)

    def __str__(self):
        """
        Returns the string representation of the field

        Arguments:
        None

        Returns:
        str -- the string representation of the field

        Raises:
        None
        """
        return self.value.strftime("%d.%m.%Y")

    def __validate(self, value):
        """
        Validates the field value

        Arguments:
        value -- the value to validate

        Returns:
        bool -- True if the value is valid, False otherwise

        Raises:
        None
        """
        return re.match(r"^\d{2}\.\d{2}\.\d{4}$", value) is not None

# private.py
"""Class with public and private attributes."""

class PrivateClass:
    """Class with public and private attributes."""
    
    def __init__(self):
        """Initialize the public and private attributes."""
        self.public_data = "public" # public attribute
        self.__private_data = "private" # private attribute
        
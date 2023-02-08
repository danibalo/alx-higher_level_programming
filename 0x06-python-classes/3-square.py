#!/usr/bin/python3
# 0.square.py By Daniel Balo Tarafa
""" A module that defines square"""


class Square:
    """Class of Square"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: the size of square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less or equal to zero

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Gives Area of the square
            Returns: The square of the size
        """

        return (self.__size ** 2)

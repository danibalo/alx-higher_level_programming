#!/usr/bin/python3
# 0-square.py - By Daniel Balo
"""A module that defines square"""


class Square:
    """ A class that represnts square """

    def __init__(self, size=0):
        """Initializing this square class 
        Args:
            size: represents the size of square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less or equal to zero
            """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

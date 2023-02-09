#!/usr/bin/python3
# 5-square.py By Daniel Balo Tarafa
"""A module of Square """


class Square:
    """A class that defines Square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: the size(side length) of the square
        Raises:
            TypeError: if size is not an integer
            ValueError : if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retirive size (side length) of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """"Calculates Area of the square
            Returns : The square of the given size
        """
        return self.__size ** 2

    def my_print(self):
        """"Prints the # square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * "#")

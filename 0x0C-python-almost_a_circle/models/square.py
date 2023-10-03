#!/usr/bin/python3
"""Defines Square class that inherits from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square class with its attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square objects/instances
        Args:
            size (int): size of the square
            x (int): horizontal coordinates
            y (int): vertical coordinates
            id (int): id of the instances
        """
        super().__init__(size, size, x, y, id)
        self.size = self.width

    @property
    def size(self):
        """size property getter: retrives the size of the square
        Returns:
            size (int): the size instance attributes
        size.setter: set the size of the square
        Args:
            value (int): inherit width and height from Rectangle as size
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Represents square string to the stdout"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update the value of square attributes
        Args:
            *args (tuple): List of attributes
            *kwargs (dict): key and values of attributes
        *args is the list of arguments:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        """
        attrs = ["id", "size", "x", "y"]
        index = 0
        if args is not None and len(args) > 0:
            for arg in args:
                if index < 4:
                    setattr(self, attrs[index], arg)
                    index += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Converts Square instance to dictionary representation"""
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        })

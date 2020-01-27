#!/usr/bin/python3
"""
    square.py module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Inicialitation method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>"""
        idd = self.id
        x = super().x
        y = super().y
        w = super().width
        return "[Square] ({}) {}/{} - {}".format(idd, x, y, w)

    @property
    def size(self):
        """size getter"""
        return super().width

    @size.setter
    def size(self, size):
        """size setter"""
        super(Square, type(self)).width.fset(self, size)
        super(Square, type(self)).height.fset(self, size)

#!/usr/bin/python3
"""
    2-rectangle module
    Class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """
        Class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        s = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                s += (str(self.print_symbol) * self.__width)
                if i != self.__height - 1:
                    s += '\n'
        return s

    def __repr__(self):
        s = '(' + str(self.__width) + ',' + str(self.__height) + ')'
        return self.__class__.__name__ + s

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        area1 = rect_1.width * rect_1.height
        area2 = rect_2.width * rect_2.height
        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2

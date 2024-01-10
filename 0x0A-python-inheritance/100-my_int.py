#!/usr/bin/python3

"""
myInt class which inherits from int
"""


class MyInt(int):
    """Overiding equality and inequality for myInt instance"""

    def __eq__(self, equal):
        """Overides == operator to invert the behavior"""

        return not super().__eq__(equal)

    def __eq__(self, equal):
        """Overides != operator to invert the behavior"""
        return not super().__ne__(equal)

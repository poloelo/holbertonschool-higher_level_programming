#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """MyList class that inherits from list
    
    Public Methods:
        print_sorted: prints the list in ascending order
    """
    
    def print_sorted(self):
        """Prints the list in sorted ascending order"""
        print(sorted(self))

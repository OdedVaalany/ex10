#################################################################
# FILE : apple.py
# WRITER : int the AUTHORS file
# EXERCISE : intro2cs2 ex10 2020
# DESCRIPTION: Apple object
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one
# WEB PAGES I USED: None
# NOTES: ...
#################################################################
from typing import *
import game_parameters as GP


class Apple:
    """
    this object represent the apple object in snake game
    """

    def __init__(self) -> None:
        x, y, self.__score = GP.get_random_apple_data()
        self.__position = (x, y)

    def get_coords(self) -> List[Tuple[int, int]]:
        """
        des: return all the cords of thie obj in the board
        params: None
        return: list of (y,x)
        """
        return [self.__position]

    def is_touched(self, coords: List[Tuple[int, int]]) -> Any:
        """
        des: check if the apple thouch in any cord from the given list
        params: coords - list of coordinates
        return: score if there is any touch' else None
        """
        if self.__position in coords:
            return self.__score

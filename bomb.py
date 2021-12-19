#################################################################
# FILE : bomb.py
# WRITER : int the AUTHORS file
# EXERCISE : intro2cs2 ex10 2020
# DESCRIPTION: Bomb object
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one
# WEB PAGES I USED: None
# NOTES: ...
#################################################################
from typing import *
import game_parameters as GP


class Bomb:
    """
    This class represent the bomb object in the snake game
    """

    def __init__(self) -> None:
        x, y, self.__size, self.__time = GP.get_random_bomb_data()
        self.__position = (x, y)

    def get_position(self) -> Tuple[int, int]:
        """
        des: return the position of the bomb
        :params: None
        :return: (y,x) cord
        """
        return self.__position

    def get_coords(self) -> List[Tuple[int, int]]:
        """
        des: return all the cords of thie obj in the board
        :params: None
        :return: list of (y,x)
        """
        if self.__time > 0:
            return [self.__position]
        elif self.__time == 0:
            return [self.__position, (-1, -1)]
        y: int = self.__position[1]
        x: int = self.__position[0]
        ls: List[Tuple[int, int]] = []
        curr_radius: int = abs(self.__time)
        for i in range(curr_radius):
            ls.append((x + (curr_radius-i), y-i))
            ls.append((x - (curr_radius-i), y+i))
            ls.append((x - i, y - (curr_radius-i)))
            ls.append((x + i, y + (curr_radius-i)))
        return ls

    def update(self) -> bool:
        """
        des: notice to the obj that 1 timelape passed
        :params: None
        :return: if the bomb end her circle
        """
        self.__time -= 1
        if self.__time < (-1) * self.__size:
            return True
        return False

    def is_touched(self, coords: List[Tuple[int, int]]) -> Union[Tuple[int, int], None]:
        """
        des: check if the bomb/explotion wave touch with any coord in given coords list
        :params: coords list
        :return: true if there is any touch else return false
        """
        my_coords: List[Tuple[int, int]] = self.get_coords()
        for me in my_coords:
            if me in coords:
                return me

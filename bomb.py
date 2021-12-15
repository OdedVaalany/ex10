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
        y: int = self.__position[1]
        x: int = self.__position[0]
        ls: List[Tuple[int, int]] = []
        for i in range(abs(self.__time) + 2):
            ls.append((x-i,y - ((abs(self.__time) + 1) - i)))
            ls.append((x+i,y - ((abs(self.__time) + 1) - i)))
            ls.append((x+i ,y + ((abs(self.__time) + 1) - i)))
            ls.append((x-i,y + ((abs(self.__time) + 1) - i)))
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

    def is_touched(self, coords: List[Tuple[int, int]]) -> bool:
        """
        des: check if the bomb/explotion wave touch with any coord in given coords list
        :params: coords list
        :return: true if there is any touch else return false
        """
        my_coords: List[Tuple[int, int]] = self.get_coords()
        for me in my_coords:
            if me in coords:
                return True
        return False

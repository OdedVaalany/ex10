from typing import *
import game_parameters as GP


class apple:
    def __init__(self) -> None:
        y, x, self.__score = GP.get_random_apple_data()
        self.__position = (y, x)

    def get_coords(self) -> List[Tuple[int, int]]:
        """
        des: return all the cords of thie obj in the board
        params: None
        return: list of (y,x)
        """
        return [self.__position]

    def update(self) -> None:
        """
        des: notice to the obj that 1 timelape passed
        params: None
        return: None
        """
        pass

    def is_touched(self, coords: List[Tuple[int, int]]) -> Any:
        """
        des: check if the apple thouch in any cord from the given list
        params: coords - list of coordinates
        return: score if there is any touch' else None
        """
        if self.__position in coords:
            return self.__score

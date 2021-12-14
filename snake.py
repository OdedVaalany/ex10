from typing import List, Tuple
from LinkedList import LinkedList


class snake:
    def __init__(self) -> None:
        self.__head = LinkedList()
        self.__tail = self.__head
        pass

    def get_coords(self) -> List[Tuple[int, int]]:
        """
        des: return all the cords of thie obj in the board
        params: None
        return: list of (y,x)
        """
        pass

    def update(self) -> None:
        """
        des: notice to the obj that 1 timelape passed
        params: None
        return: None
        """
        pass

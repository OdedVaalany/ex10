from tkinter.constants import N
from typing import List, Tuple

from LinkedList import LinkedList
from game_parameters import WIDTH, HEIGHT

POSSIBLE_DIRECTIONS = ["Up", "Down", "Left", "Right"]

class Snake:
    def __init__(self) -> None:
        """
        des: constructor of Snake, creates the snake using
             a linked list
        """
        initial_coords = [(10,10),  (10,9), (10,8)]
        
        self.snake = LinkedList()
        self.direction = "Up"
        self.cells_to_add = 0
        
        for coord in initial_coords:
            self.snake.add(coord)

    def get_coords(self) -> List[Tuple[int, int]]:
        """
        return: list of all the snake's coords of coord (y,x)
        """
        return self.snake.get_list()
    
    def get_direction(self) -> str:
        """
        return: the snake's current movement direction
        """
        return self.direction
    
    def add_length(self, num_to_add: int) -> None:
        """
        des: add cells to the snake's tail
        params: num_to_add - number of cells to add
        """
        self.cells_to_add += num_to_add
    
    def get_head(self) -> Tuple[int,int]:
        """
        des: returns the head coordinate of the snake
        """
        return self.snake.get_head().get_data()

    def set_direction(self, new_direction: str) -> None:
        """
        des: set the snake's movement direction
        params: new_direction - wanted direction
        """
        if not new_direction in POSSIBLE_DIRECTIONS:
            return None
        
        if new_direction in POSSIBLE_DIRECTIONS and\
            not (self.direction == "Left" and new_direction == "Right") and\
            not (self.direction == "Right" and new_direction == "Left") and\
            not (self.direction == "Up" and new_direction == "Down") and\
            not (self.direction == "Down" and new_direction == "Up"):
            self.direction = new_direction
    
    def _get_new_head_coord(self) -> Tuple[int, int]:
        """
        return: Tuple with the new head coord calculated 
                by the snake's current movement
        """
        head_coords = self.snake.get_head().get_data()
        if self.direction == "Up":
            return (head_coords[0], head_coords[1] + 1)
        if self.direction == "Down":
            return (head_coords[0], head_coords[1] - 1)
        if self.direction == "Right":
            return (head_coords[0] + 1, head_coords[1])
        if self.direction == "Left":
            return (head_coords[0] - 1, head_coords[1])
            
    def update(self) -> bool:
        """
        des: this function updates the snake's movement by one cell towards
             the snake's current movement direction. If cells are to be added
             to the snake, it adds to snake's length one cell at a time.
        return: True if update was succesful,
                False otherwise
        """
        if self.cells_to_add == 0:
            self.snake.remove_tail()
        else:
            self.cells_to_add -= 1
        
        new_head = self._get_new_head_coord()
        
        if new_head in self.get_coords():
            self.snake.remove_cell(new_head)
            self.snake.add_head(new_head) 
            return False
        
        self.snake.add_head(new_head) 
        return True
        
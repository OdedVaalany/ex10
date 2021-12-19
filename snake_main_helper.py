#################################################################
# FILE : snake_main_helper.py
# WRITER : int the AUTHORS file
# EXERCISE : intro2cs2 ex10 2020
# DESCRIPTION: extra function to help the main code
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one
# WEB PAGES I USED: None
# NOTES: ...
#################################################################
from typing import List, Tuple, Union
from game_display import GameDisplay
import game_parameters as gp
from snake import Snake
from bomb import Bomb
from apple import Apple


def get_forbidden_coords(snake, bomb, apples) -> List[Tuple[int, int]]:
    """
    generate list of unempty cells, to prevent overwrite
    params: snake, bomb, apples : objects
    :return: list of coordinates
    """
    forbidden_coords = snake.get_coords()
    forbidden_coords.extend(bomb.get_coords())
    forbidden_coords.extend([app.get_coords()[0] for app in apples])

    return forbidden_coords


def generate_bomb(coords: List[Tuple[int, int]]) -> Union[Bomb, None]:
    """
    generate bomb within the board, while consider the unempty cells
    params: list of forbidden cells
    :return: Bomb if there is place else return None
    """
    if len(coords) == gp.WIDTH * gp.HEIGHT:
        return None

    bomb = Bomb()
    while bomb.is_touched(coords):
        bomb = Bomb()

    return bomb


def generate_apple(coords: List[Tuple[int, int]]) -> Union[Apple, None]:
    """
    generate apple within the board, while consider the unempty cells
    params: list of forbidden cells
    :return: Apple if there is place else return None
    """
    if len(coords) == gp.WIDTH * gp.HEIGHT:
        return None

    apple = Apple()
    while apple.is_touched(coords):
        apple = Apple()

    return apple


def draw_objects(
        gd: GameDisplay, score: int, snake: Snake = None, bomb: Bomb = None,
        apples: List[Apple] = None,
        remove_cells_from_snake: List[Tuple[int, int]] = []) -> None:
    """
    print the board with the game_display library
    params: game_display, score - int, the tools on the board (apple,snake,bomb)
             and get list with coords to dont print
    :return: None
    """
    if apples:
        for apple in apples:
            if apple != None:
                coord = apple.get_coords()[0]
                gd.draw_cell(coord[0], coord[1], "green")

    if snake:
        for coord in snake.get_coords():
            if not coord in remove_cells_from_snake:
                gd.draw_cell(coord[0], coord[1], "black")

    if bomb:
        bomb_coords = bomb.get_coords()
        if len(bomb_coords) > 1:
            for coord in bomb_coords:
                if not coord == (-1, -1):
                    gd.draw_cell(coord[0], coord[1], "orange")
        else:
            gd.draw_cell(bomb_coords[0][0], bomb_coords[0][1], "red")

    if score >= 0:
        gd.show_score(score)


def check_out_of_bounds(obj: Union[Snake, Bomb]) -> bool:
    """
    check if the snake or the bomb_wave get out from the board bounds
    params: obj - Snake or Bomb
    :return: Ture if the objet get out of bound else False
    """
    if type(obj) == Snake:
        snake_head = obj.get_coords()[0]
        if check_coord_out_of_bounds(snake_head):
            return True

    elif type(obj) == Bomb:
        if len(obj.get_coords()) == 2:
            return False
        for coord in obj.get_coords():
            if check_coord_out_of_bounds(coord):
                return True

    return False


def check_coord_out_of_bounds(coord: Tuple[int, int]) -> bool:
    """
    check if single coord get out of the board bounds
    params: get coord (x,y)
    :return: True if get out else False
    """
    if coord[0] < 0 or coord[0] >= gp.WIDTH \
            or coord[1] < 0 or coord[1] >= gp.HEIGHT:
        return True

    return False

from typing import List, Tuple, Union
import game_parameters as gp
from game_display import GameDisplay
from snake import Snake
from bomb import Bomb
from apple import Apple
possible_directions = ["Up", "Down", "Left", "Right"]


def main_loop(gd: GameDisplay) -> None:
    score = 0
    snake = Snake()
    bomb = Bomb()
    apples: List[Apple] = []
    why_stoped = 0

    while bomb.is_touched(snake.get_coords()):
        bomb = Bomb()

    forbidden_coords = snake.get_coords()
    forbidden_coords.extend(bomb.get_coords())

    for i in range(0, 3):
        apples.append(generate_apple(forbidden_coords))
        forbidden_coords.extend(apples[i].get_coords())

    while why_stoped == 0:
        forbidden_coords = get_forbidden_coords(snake, bomb, apples)
        draw_objects(snake, gd, bomb, apples, score)

        key_clicked = gd.get_key_clicked()
        if key_clicked in possible_directions:
            snake.set_direction(key_clicked)

        # eating apple check
        for i in range(len(apples)):
            opp_score = apples[i].is_touched(snake.get_coords())
            if opp_score:
                score += opp_score
                snake.add_length(3)
                forbidden_coords.remove(apples[i].get_coords()[0])
                apples[i] = generate_apple(forbidden_coords)
            if apples[i].is_touched(bomb.get_coords()):
                forbidden_coords.remove(apples[i].get_coords()[0])
                apples[i] = generate_apple(forbidden_coords)
            if not apples[i]:
                why_stoped = 1

        # if touch bomb
        if(bomb.is_touched(snake.get_coords())):
            why_stoped = 2

        bomb.update()
        if check_out_of_bounds(bomb):
            bomb = Bomb()

        snake.update()
        if check_out_of_bounds(snake):
            break

        # TODO check snake is not touching itself
        gd.end_round()

    draw_objects(snake, gd, bomb, apples, score)


def get_forbidden_coords(snake, bomb, apples):
    forbidden_coords = snake.get_coords()
    forbidden_coords.extend(bomb.get_coords())
    forbidden_coords.extend([app.get_coords()[0] for app in apples])
    return forbidden_coords


def generate_apple(coords: List[Tuple[int, int]]) -> Union[Apple, None]:
    if len(coords) == gp.WIDTH * gp.HEIGHT:
        return None
    apple = Apple()
    while apple.is_touched(coords):
        apple = Apple()
    return apple


def draw_objects(s, gd, bomb, apples, score):
    for coord in s.get_coords():
        gd.draw_cell(coord[0], coord[1], "black")

    bomb_coords = bomb.get_coords()
    if len(bomb_coords) > 1:
        for coord in bomb_coords:
            gd.draw_cell(coord[0], coord[1], "orange")
    else:
        gd.draw_cell(bomb_coords[0][0], bomb_coords[0][1], "red")

    for apple in apples:
        coord = apple.get_coords()[0]
        gd.draw_cell(coord[0], coord[1], "green")

    gd.show_score(score)


def check_out_of_bounds(obj: Union[Snake, Bomb]):
    if type(obj) == Snake:
        snake_head = obj.get_coords()[0]
        if check_coord_out_of_bounds(snake_head):
            return True
    elif type(obj) == Bomb:
        for coord in obj.get_coords():
            if check_coord_out_of_bounds(coord):
                return True

    return False


def check_coord_out_of_bounds(coord: Tuple[int, int]):
    if coord[0] < 0 or coord[0] >= gp.WIDTH \
            or coord[1] < 0 or coord[1] >= gp.HEIGHT:
        return True
    return False

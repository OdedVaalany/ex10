from typing import List, Tuple, Union
import game_parameters as gp
from game_display import GameDisplay
from snake import Snake
from bomb import Bomb
from apple import Apple


def main_loop(gd: GameDisplay) -> None:
    score = 0
    snake = Snake()
    forbidden_coords = snake.get_coords()
    apples: List[Apple] = []
    game_end_reason = 0

    bomb = Bomb()
    while bomb.is_touched(forbidden_coords):
        bomb = Bomb()

    forbidden_coords.extend(bomb.get_coords())

    for i in range(3):
        apples.append(generate_apple(forbidden_coords))
        forbidden_coords.extend(apples[i].get_coords())
#############################################################
    flag = False
    forbidden_coords = get_forbidden_coords(snake, bomb, apples)
    for coord in snake.get_coords():
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

##############################################################
    while game_end_reason == 0:
        forbidden_coords = get_forbidden_coords(snake, bomb, apples)
        if flag:
            draw_objects(gd, score, snake, bomb, apples)
        else:
            flag = True

        key_clicked = gd.get_key_clicked()
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
                game_end_reason = 1

        # if touch bomb
        if(bomb.is_touched(snake.get_coords())):
            game_end_reason = 2

        bomb.update()
        if check_out_of_bounds(bomb):
            # TODO: remvoe bomb coords from forbidden
            bomb = generate_bomb(forbidden_coords)

        if not snake.update():
            game_end_reason = 3

        if check_out_of_bounds(snake):
            game_end_reason = 4

        gd.end_round()

    if game_end_reason == 2:
        draw_objects(gd, score, None, bomb, None)
        gd.end_round()

    # head = snake.get_head()
    if game_end_reason == 1:
        draw_objects(gd, score, snake, bomb, apples)
        gd.end_round()

    if game_end_reason == 3:
        draw_objects(gd, score, snake, bomb, apples)
        gd.end_round()

    if game_end_reason == 4:
        draw_objects(gd, score, snake, bomb, apples, [snake.get_head()])
        gd.end_round()


def get_forbidden_coords(snake, bomb, apples):
    forbidden_coords = snake.get_coords()
    forbidden_coords.extend(bomb.get_coords())
    forbidden_coords.extend([app.get_coords()[0] for app in apples])

    return forbidden_coords


def generate_bomb(coords: List[Tuple[int, int]]) -> Union[Bomb, None]:
    if len(coords) == gp.WIDTH * gp.HEIGHT:
        return None

    bomb = Bomb()
    while bomb.is_touched(coords):
        bomb = Bomb()

    return bomb


def generate_apple(coords: List[Tuple[int, int]]) -> Union[Apple, None]:
    # check if there's no cells left for the apple
    if len(coords) == gp.WIDTH * gp.HEIGHT:
        return None

    apple = Apple()
    while apple.is_touched(coords):
        apple = Apple()

    return apple


def draw_objects(gd, score, snake, bomb, apples, remove_cells_from_snake=[]):
    if apples:
        for apple in apples:
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
                gd.draw_cell(coord[0], coord[1], "orange")
        else:
            gd.draw_cell(bomb_coords[0][0], bomb_coords[0][1], "red")

    if score >= 0:
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

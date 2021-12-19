#################################################################
# FILE : snake_main.py
# WRITER : in the AUTHORS file
# EXERCISE : intro2cs2 ex10 2020
# DESCRIPTION: the main loop of the snake game
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one
# WEB PAGES I USED: None
# NOTES: ...
#################################################################
from typing import List
from snake_main_helper import *
from game_display import GameDisplay
from snake import Snake
from bomb import Bomb
from apple import Apple


def main_loop(gd: GameDisplay) -> None:

    # Define the game and it's variable
    score = 0
    snake = Snake()
    forbidden_coords = snake.get_coords()
    apples: List[Apple] = []
    game_end_reason = 0

    # reset the bomb
    bomb = Bomb()
    while bomb.is_touched(forbidden_coords):
        bomb = Bomb()
    forbidden_coords.extend(bomb.get_coords())

    # reset the apples
    for i in range(3):
        apples.append(generate_apple(forbidden_coords))
        forbidden_coords.extend(apples[i].get_coords())

    # draw the starting point
    gd.show_score(score)
    draw_objects(gd, score, snake, bomb, apples)
    gd.end_round()

    # game main loop
    while game_end_reason == 0:
        forbidden_coords = get_forbidden_coords(snake, bomb, apples)

        key_clicked = gd.get_key_clicked()
        snake.set_direction(key_clicked)

        # snake step forward and check if he's touching himself
        if not snake.update():
            game_end_reason = 3

        # update the bomb and check if it out of bounds
        bomb.update()
        if check_out_of_bounds(bomb):
            bomb = generate_bomb(forbidden_coords)

        # check if apple eaten by the snake or destroied by the bomb
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
                game_end_reason = 0

        # if touch bomb
        bomb_snake_touching_point = bomb.is_touched(snake.get_coords())
        if(bomb_snake_touching_point):
            game_end_reason = 4 if len(bomb.get_coords()) == 1 else 2

        # if snake get out of bounds
        if check_out_of_bounds(snake):
            game_end_reason = 4

        if game_end_reason == 2:
            draw_objects(
                gd, score, snake, apples=apples,
                remove_cells_from_snake=[bomb_snake_touching_point])
            draw_objects(
                gd, score, bomb=bomb)
        elif game_end_reason == 4:
            draw_objects(gd, score, snake, bomb, apples, [snake.get_head()])
        else:
            draw_objects(gd, score, snake, bomb, apples)
        gd.end_round()

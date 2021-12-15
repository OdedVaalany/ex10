import game_parameters
from game_display import GameDisplay
from snake import Snake

possible_directions = ["Up", "Down", "Left", "Right"]

def main_loop(gd: GameDisplay) -> None:
    s = Snake()
    gd.show_score(0)
    x, y = 15, 15
    
    counter = 1
    while True:
        key_clicked = gd.get_key_clicked()
        if key_clicked == "Left" or key_clicked == "Right":
            counter += 1
            print(counter)
        if counter % 5 == 0:
            s.add_length(3)
            counter += 1
            print(counter)
            
        if key_clicked in possible_directions:
            s.set_direction(key_clicked)
            
        for coord in s.get_coords():
            gd.draw_cell(coord[0], coord[1], "black")
        gd.draw_cell(x, y, "red")
        s.update()
        gd.end_round()

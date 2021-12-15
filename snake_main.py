import game_parameters
from game_display import GameDisplay


def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    x, y = 10, 10
    while True:
        x += 1
        gd.draw_cell(x, y, "red")
        gd.end_round()


if __name__ == "__main__":
    gd = GameDisplay()
    gd.start()
    main_loop(gd)

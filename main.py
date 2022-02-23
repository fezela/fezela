from Game import Game
from curses import wrapper

def main(stdscr):
    G = Game()
    G.start()


wrapper(main)

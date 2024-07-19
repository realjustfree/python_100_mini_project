import curses

WINDOW_HEIGHT = 20
WINDOW_HEIGHT = 60

def main(stdscr):
    stdscr.clear()

    win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH, 0, 0)




curses.wrapper(main)


import curses

WINDOW_WIDTH = 60
WINDOW_HEIGHT = 30
FOOD_CHAR = '#'
SNAKE_CHAR = '*'

def main(stdscr):
    #stdscr.clear()
    curses.noecho()
    curses.curs_set(0)



    # setup window
        # curses.newwin() ⇒ win 에 할당. 아직 그림 그린 상태 아님.
    win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH, 0, 0)
    win.keypad(True)
    win.border(0)
    win.nodelay(True)

    # snake set
    snake = [(4, 4), (4, 3), (4, 2)]
    food = (6, 6)

    # game settings
    score = 0
    ESC = 27
    key = curses.KEY_RIGHT

    win.addch(food[0], food[1], FOOD_CHAR)

    # loop
    while key != ESC:
        win.addstr(0, 2, "Score : " + str(score) + " ")
        win.addstr(0, WINDOW_WIDTH-15, " key : "+ str(key)+" ")
        win.timeout(1000)

        new_key = win.getch()

        if new_key in [curses.KEY_LEFT,
        curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
            key = new_key

    # next coordination
        y = snake[0][0]
        x = snake[0][1]

        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_LEFT:
            x -= 1
        if key == curses.KEY_RIGHT:
            x += 1

        snake.insert(0, (y, x))

        win.addstr(0,10, "snake : "+ str(snake[0]))

        # win.addch(snake[0][0], snake[0][1], SNAKE_CHAR)






curses.wrapper(main)


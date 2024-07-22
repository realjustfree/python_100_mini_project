import curses
import random

WINDOW_WIDTH = 60
WINDOW_HEIGHT = 30
FOOD_CHAR = '#'
SNAKE_CHAR = '*'

def break_count():

    return 1

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



    # loop
    while key != ESC:
        win.addch(food[0], food[1], FOOD_CHAR)
        win.addstr(0, 2, "Score : " + str(score) + " ")
        win.addstr(0, WINDOW_WIDTH-15, " key : "+ str(key)+" ")
        win.addstr(0, 20, "head : " + str(snake[0])) # snake head coordination

        # timeout(0)으로 하면 바로 오른쪽에 닿여서 끝나는 듯
        # 1000ms = 1s
        # speed control
        timeout_value = 10 if (1000 - 50*len(snake)//2 + 10*len(snake)//10 % 100) <= 5 else (1000 - 50*len(snake)//2 + 10*len(snake)//10 % 100)
        win.timeout(timeout_value)


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

        snake.insert(0, (y, x)) # add snake head
        win.addch(snake[0][0], snake[0][1], SNAKE_CHAR) # print snake head


        snake.pop() # delete snake tail
        win.addch(snake[-1][0], snake[-1][1], " ")

        if food in snake:
            score += 1

            y_last = snake[-1][0]
            x_last = snake[-1][1]

            if key == curses.KEY_DOWN:
                y_last -= 1
            if key == curses.KEY_UP:
                y_last += 1
            if key == curses.KEY_LEFT:
                x_last += 1
            if key == curses.KEY_RIGHT:
                x_last -= 1

            snake.insert(-1, (y_last, x_last ))


            # food generation
            food = ()
            while food == ():
                food = (random.randint(1, WINDOW_HEIGHT-2), random.randint(1, WINDOW_WIDTH-2))
                if food in snake:
                    food = ()

        # check the game-over condition

        # touching border line
        if snake[0][0] in [0, WINDOW_HEIGHT-1]:
            break
        if snake[0][1] in [0, WINDOW_WIDTH-1]:
            break
        # touching its own body
        if snake[0] in snake[1:]:
            break

    print(f"Final score = {score}")

curses.wrapper(main)
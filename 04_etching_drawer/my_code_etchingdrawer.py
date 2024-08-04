import shutil, sys

class lines:
    UP_DOWN_CHAR = chr(9474)  # Character 9474 is '│'
    LEFT_RIGHT_CHAR = chr(9472)  # Character 9472 is '─'
    DOWN_RIGHT_CHAR = chr(9484)  # Character 9484 is '┌'
    DOWN_LEFT_CHAR = chr(9488)  # Character 9488 is '┐'
    UP_RIGHT_CHAR = chr(9492)  # Character 9492 is '└'
    UP_LEFT_CHAR = chr(9496)  # Character 9496 is '┘'
    UP_DOWN_RIGHT_CHAR = chr(9500)  # Character 9500 is '├'
    UP_DOWN_LEFT_CHAR = chr(9508)  # Character 9508 is '┤'
    DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
    UP_LEFT_RIGHT_CHAR = chr(9524)  # Character 9524 is '┴'
    CROSS_CHAR = chr(9532)  # Character 9532 is '┼'
    CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()




def draw_canvas():
    pass

def main():
    canvas = {}
    cursor_x = 0
    cursor_y = 0
    moves = []

    while True:

        print("Input WASD keys to draw lines, C to clear, F to save or Q to quit.")
        respond = input("> ").lower()

        if respond == 'q' or respond == 'quit':
            print("Goodbye!")
            sys.exit()

        for command in respond:
            if command not in ('w', 'a', 's', 'd'):
                print("Invalid command. Please input WASD keys to draw lines")
                continue
            moves.append(command)





if __name__ == '__main__':
    main()
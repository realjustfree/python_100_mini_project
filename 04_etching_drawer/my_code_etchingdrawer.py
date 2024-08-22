# 2024-08-22
# 버그 있음. 10일 만에 다시 보면서 처음부터 파악하려니 스트레스
# 나중에 레벨 높아지면 다시 돌아올 것.
# 일단 pass

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
    # CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
    CANVAS_WIDTH, CANVAS_HEIGHT = 3, 2

def draw_canvas(canvas, cx, cy):
    canvaString = ""

    for rowNum in range(lines.CANVAS_HEIGHT):
        for colNum in range(lines.CANVAS_WIDTH):
            if rowNum == cy and colNum == cx:
                canvaString += '#'
                continue

            cell = canvas.get((colNum, rowNum))
            if cell in [set(['w','s']), set(['w']), set(['s'])]:
                canvaString += lines.UP_DOWN_CHAR
            elif cell in [set(['a','d']), set(['a']), set(['d'])]:
                canvaString += lines.LEFT_RIGHT_CHAR
            elif cell == set(['s', 'd']):
                canvaString += lines.DOWN_RIGHT_CHAR
            elif cell == set(['a', 's']):
                canvaString += lines.DOWN_LEFT_CHAR
            elif cell == set(['w', 'd']):
                canvaString += lines.UP_RIGHT_CHAR
            elif cell == set(['w', 'a']):
                canvaString += lines.UP_LEFT_CHAR
            elif cell == set(['w', 's', 'd']):
                canvaString += lines.UP_DOWN_RIGHT_CHAR
            elif cell == set(['w', 's', 'a']):
                canvaString += lines.UP_DOWN_LEFT_CHAR
            elif cell == set(['a', 's', 'd']):
                canvaString += lines.DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['w', 'a', 'd']):
                canvaString += lines.UP_LEFT_RIGHT_CHAR
            elif cell == set(['w', 'a', 's', 'd']):
                canvaString += lines.CROSS_CHAR
            elif cell == None:
                canvaString += ' '
        canvaString += '\n'

    print(canvaString)

def main():
    canvas = {}
    cursor_x = 0
    cursor_y = 0
    moves = []

    while True:

        draw_canvas(canvas, cursor_x, cursor_y)

        print("Input WASD keys to draw lines, C to clear, F to save or Q to quit.")
        #respond = input("> ").lower()
        respond = "ddsaaw"
        if respond == 'q' or respond == 'quit':
            print("Goodbye!")
            sys.exit()

        for command in respond:
            if command not in ('w', 'a', 's', 'd'):
                continue
            moves.append(command)

            # draw first when canvas in empty
            if canvas == {}:
                if command in ('w', 's'):
                    canvas[(cursor_x, cursor_y)] = set(['w','s'])
                elif command in ('a', 'd'):
                    canvas[(cursor_x, cursor_y)] = set(['a', 'd'])

            if command == 'w' and cursor_y > 0:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_y = cursor_y - 1
            elif command == 's' and cursor_y < lines.CANVAS_HEIGHT:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_y = cursor_y + 1
            elif command == 'a' and cursor_x > 0:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_x = cursor_x - 1
            elif command == 'd' and cursor_x < lines.CANVAS_WIDTH:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_x = cursor_x + 1
            else:
                continue

            # make empty set if cursor is not in canvas
            if (cursor_x, cursor_y) not in canvas:
                canvas[(cursor_x, cursor_y)] = set()

            # add direction to the set
            if command == 'w':
                canvas[(cursor_x, cursor_y)].add('s')
            elif command == 's':
                canvas[(cursor_x, cursor_y)].add('w')
            elif command == 'a':
                canvas[(cursor_x, cursor_y)].add('d')
            elif command == 'd':
                canvas[(cursor_x, cursor_y)].add('a')



if __name__ == '__main__':
    main()
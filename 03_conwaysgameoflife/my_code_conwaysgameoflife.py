# temp file for merging later
# 2024-07-29 15:39

import sys, time, random

# define CONSTANTS
HEIGHT = 90
WIDTH = 80

ALIVE = "#"
DEAD = " "


def main():
    life_cycle = 0 # how many times loops repeated
    cells = {}

    # make new cell first time
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cells[(x, y)] = random.choice([ALIVE, DEAD])

    # loop
    while True:
        life_cycle += 1
        for x in range(WIDTH):
            for y in range(HEIGHT):
                print(cells[(x, y)], end="")
            print("")

       # make new cell based on previous cell
        next_cells = {}
        for x in range(WIDTH):

            for y in range(HEIGHT):
                neighbor_cell = 0
                ABOVE = (y-1) % HEIGHT
                BELOW = (y+1) % HEIGHT
                LEFT = (x-1) % WIDTH
                RIGHT = (x+1) % WIDTH

                if cells[(x, ABOVE)] == ALIVE:
                    neighbor_cell += 1
                if cells[(x, BELOW)] == ALIVE:
                    neighbor_cell += 1
                if cells[(LEFT, y)] == ALIVE:
                    neighbor_cell += 1
                if cells[(RIGHT, y)] == ALIVE:
                    neighbor_cell += 1
                if cells[(LEFT, ABOVE)] == ALIVE:
                    neighbor_cell += 1
                if cells[(RIGHT, ABOVE)] == ALIVE:
                    neighbor_cell += 1
                if cells[(LEFT, BELOW)] == ALIVE:
                    neighbor_cell += 1
                if cells[(RIGHT, BELOW)] == ALIVE:
                    neighbor_cell += 1

                if cells[(x, y)] == ALIVE and (neighbor_cell == 2 or neighbor_cell == 3):
                    next_cells[(x, y)] = ALIVE
                elif cells[(x, y)] == DEAD and neighbor_cell == 3:
                    next_cells[(x, y)] = ALIVE
                else:
                    next_cells[(x, y)] = DEAD
        cells = next_cells


        try:
            # time.sleep(1)
            input("press enter to continue" )
            print("ctrl+c to exit")
            print("\n" * 10)
        except KeyboardInterrupt:
            print("you've made {} life cycles".format(life_cycle))
            sys.exit()


if __name__== "__main__":
    main()

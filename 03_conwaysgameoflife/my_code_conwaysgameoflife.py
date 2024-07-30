# temp file for merging later
# 2024-07-29 15:39

import sys, time, random

# define CONSTANTS
HEIGHT = 90
WIDTH = 80

ALIVE = "#"
DEAD = "."


def main():
    life_cycle = 0 # how many times loops repeated
    cells = {}

    # make new cell first time
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cells[(x, y)] = random.choice([ALIVE, DEAD])

    # loop
    while True:
        for x in range(WIDTH):
            for y in range(HEIGHT):
                print(cells[(x, y)], end="")
        print("\n")

       # make new cell based on previous cell
        for x in range(WIDTH):
            for y in range(HEIGHT):
                ABOVE = (y-1) % HEIGHT
                BELOW = (y+1) % HEIGHT
                LEFT = (x-1) % WIDTH
                RIGHT = (x+1) % WIDTH

                if cells[(x, ABOVE)] == ALIVE:
                    neighbour_cell += 1








        try:
            time.sleep(1)
            print("ctrl+c to exit")
            print("\n" * 10)
        except KeyboardInterrupt:
            print("you've made {} life cycles".format(life_cycle))
            sys.exit()


if __name__== "__main__":
    main()

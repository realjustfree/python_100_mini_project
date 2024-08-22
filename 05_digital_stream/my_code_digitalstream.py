import sys, random, shutil
import time

# Set up the constants:
MIN_LENGTH = 5
MAX_LENGTH = 10

DENSITY = 0.02
PAUSE = 0.5

STREAM_CHARS = ['#', '*', '+', '@', '$']

WIDTH = shutil.get_terminal_size()[0] # need to add -1

try:
    col = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if col[i] == 0:
                if random.random() <= DENSITY:
                    col[i] = random.randint(MIN_LENGTH, MAX_LENGTH)
            if col[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                col[i] -= 1
            else:
                print(" ", end='')
        print()
        #sys.stdout.flush()
        time.sleep(PAUSE)


except KeyboardInterrupt:
    sys.exit()
import sys
import random

chars = '\\|/'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars, seed) for _ in range(columns)))
        # return 

if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")
    # print(int(sys.argv[1]), int(sys.argv[2]))
    draw(int(sys.argv[1]), int(sys.argv[2]))
from detect_press import *
from newCoords import *

def draw_snake(x, y, width=10, height=10):
    for j in range(height):
        for i in range(width):
            if i == x and j == y:
                print("*", end="")
            else:
                print(".", end="")
        print()

def main():
    snake_coords = [5, 5]
    while True:
        print("#" * 10)
        draw_snake(snake_coords[0], snake_coords[1])
        print("#" * 10)
        direction = detect_press()
        if direction == "quit":
            break
        if direction is None:
            continue
        snake_coords[0], snake_coords[1] = newCoords(snake_coords[0], snake_coords[1], direction)
        snake_coords[0] = max(0, min(9, snake_coords[0]))
        snake_coords[1] = max(0, min(9, snake_coords[1]))

main()
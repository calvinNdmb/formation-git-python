


def draw_snake(x, y, width=10, height=10):
    for j in range(height):
        for i in range(width):
            if i == x and j == y:
                print("*", end="")
            else:
                print(".", end="")
        print()

def main():
    snake_coords = [9, 10]
    print("#" * 10)
    draw_snake(snake_coords[0], snake_coords[1])
    print("#" * 10)

main()
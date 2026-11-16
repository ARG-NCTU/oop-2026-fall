"""Calculate the total area and the frame area of a rectangular board."""


def framed_board_area(width, height, thickness):
    original_area = width * height
    outer_width = width + 2 * thickness
    outer_height = height + 2 * thickness
    total_area = outer_width * outer_height
    return total_area, total_area - original_area


if __name__ == "__main__":
    print(*framed_board_area(4, 3, 1))


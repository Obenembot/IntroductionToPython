def print_hollow_pyramid(rows):
    for i in range(rows):
        # Print leading spaces
        space = " " * (rows - i + 2)
        print(space, end=" ")

        # Print stars and spaces
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == rows - 1:
                print("*", end="")  # Print '*' at the borders
            else:
                print("*", end="")  # Print space inside
        print(end="\n")  # Move to the next line


# Set number of rows
rows = 5
print_hollow_pyramid(rows)


def printHollowBox(rows: int, width: int):
    for i in range(rows):
        spaces = " " * 5  # Increase spaces for indentation
        if (i != 5):
            print(spaces + "* " + (" ") * width + "*" + spaces)
        else:
            print(spaces + ("*" * 7) + spaces)


# Set parameters
rows: int = 6  # this is the number of horizontal stars
width: int = 4  # this refers to the distance or the empty spaces between the horizontal lines
printHollowBox(rows, width)

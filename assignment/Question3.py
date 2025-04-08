def print_hollow_pyramid(rows):
    for i in range(rows):
        # Print leading spaces
        space = " " * (rows - i + 2)
        print(space, end=" ")

        # Most Important is getting the leading space right.
        #next we are multiply our index position by 2 and adding 1.
        # Note even though our rows i 5, the first index will be 0.
        for j in range(2 * i + 1):
            print("*", end="")
        print(end="\n")  # Move to the next line


def print_hollow_box(rows: int, width: int):
    for i in range(rows):
        spaces = " " * 5  # Increase spaces for indentation
        if (i != 5):
            print(spaces + "* " + (" ") * width + "*" + spaces)
        else: # the else draws the vertical *
            print(spaces + ("*" * 7) + spaces)


# Set number of rows
rows = 5
print_hollow_pyramid(rows) # Draw or print the HollowPyramid

# Set parameters
rows: int = 6  # this is the number of horizontal stars
width: int = 4  # this refers to the distance or the empty spaces between the horizontal lines
print_hollow_box(rows, width) # Draw or print the HollowBox

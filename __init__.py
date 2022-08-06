offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()


def read_maze(file_name):
    try:
        with open(file_name) as fh:
            # list comprehension to remove new line characters in file
            maze = [[char for char in line.strip("\n")] for line in fh]
            no_col_top_row = len(maze[0])
            for row in maze:
                if len(row) != no_col_top_row:
                    print("The maze is not rectangular")
                    raise SystemExit
            return maze
    except OSError as err:
        print("Error encountered while reading maze")
        raise SystemExit

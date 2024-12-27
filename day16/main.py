from itertools import product
import numpy as np
from sortedcollections import SortedDict, SortedList

with open("day16/test.txt", "r") as f:
    lines = [list(line) for line in f.read().split("\n")]
    board = np.array(lines, dtype=str)


def pretty_print(board):
    for row in board:
        print("".join(row))
    print()


pretty_print(board)


def find(board, val):
    height, width = board.shape
    for pos in product(range(height), range(width)):
        if board[pos] == val:
            return pos
    return (-1, -1)


def rotate(direction, clockwise: bool):
    return (direction[1], -direction[0]) if clockwise else (-direction[1], direction[0])


def adj(board, node):
    position, direction = node
    ans = [
        ((position, rotate(direction, True)), 1000),
        ((position, rotate(direction, False)), 1000),
    ]
    new_pos = tuple(sum(x) for x in zip(position, direction))
    if board[new_pos] != "#":
        ans.append(((new_pos, direction), 1))
    return ans


def min_score(board):
    start_node = (find(board, "S"), (0, 1))
    queue = SortedList([(0, start_node)], key=lambda x: x[0])

    while queue:
        dist, node = queue.pop(0)
        print(f"{node = }, {dist = }")
        for node, dist_diff in adj(board, node):
            if node in queue:
                pass
            print(f"{node = }")
            print(f"{dist_diff = }")


min_score(board)

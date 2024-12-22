from itertools import product
import re

with open("day13/real.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def cheapest_prize(x, y, a_x, a_y, b_x, b_y):
    ans = float("inf")
    for n_a, n_b in product(range(101), range(101)):
        n_x = n_a * a_x + n_b * b_x
        n_y = n_a * a_y + n_b * b_y
        if x != n_x or y != n_y:
            continue
        ans = min(ans, 3 * n_a + n_b)
    return ans if ans < float("inf") else 0


ans = 0
for line in lines:
    if re.search("A", line):
        a_x, a_y = [int(x) for x in re.findall("\d+", line)]
    elif re.search("B", line):
        b_x, b_y = [int(x) for x in re.findall("\d+", line)]
    elif re.search("Prize", line):
        x, y = [int(x) for x in re.findall("\d+", line)]
        ans += cheapest_prize(x, y, a_x, a_y, b_x, b_y)

print(f"{ans = }")

"""
Project Euler Problem 28: Number Spiral Diagonals
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

The sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
"""


def solve(side=1001):
    # Track each of the four diagonals as its own list of corner values.
    # The center 1 is placed only in X so it isn't counted four times.
    #
    # Recurrences (using old_x = top-right of the previous ring):
    #     top-right    : new = old_x + 4*(d-1)
    #     top-left     : new = old_x + 3*(d-1)
    #     bottom-left  : new = old_x + 2*(d-1)
    #     bottom-right : new = old_x + 1*(d-1)
    # Pattern: the four offsets are 1, 2, 3, 4 times (d-1).

    X = [1, 9]   # center + top-right corners
    Y = [5]      # bottom-left corners
    Z = [7]      # top-left corners
    W = [3]      # bottom-right corners

    x = 9
    for d in range(5, side + 1, 2):
        old_x = x
        y = old_x + 2 * (d - 1)
        z = old_x + 3 * (d - 1)
        w = old_x + 1 * (d - 1)
        x = old_x + 4 * (d - 1)
        X.append(x)
        Y.append(y)
        Z.append(z)
        W.append(w)

    return sum(X) + sum(Y) + sum(Z) + sum(W)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    answer = solve()
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(f"Answer: {answer}")
    print(f"Time:   {elapsed_ms:.2f} ms")

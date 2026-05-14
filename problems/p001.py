"""
Project Euler Problem 1: Multiples of 3 or 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solve():
    # TODO: your solution here
    pass


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    answer = solve()
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(f"Answer: {answer}")
    print(f"Time:   {elapsed_ms:.2f} ms")

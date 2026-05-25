"""
Project Euler Problem 25: 1000-digit Fibonacci Number
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:
    F_n = F_{n-1} + F_{n-2},  where F_1 = 1 and F_2 = 1.

The 12th term, F_12 = 144, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to
contain 1000 digits?
"""


def solve(num_digits=1000):
    # Two rolling variables march up the sequence.
    # Start from F_11 = 89, F_12 = 144 (the first 3-digit term).
    i = 12
    x = 144  # F_12
    y = 89   # F_11
    while len(str(x)) < num_digits:
        x, y = x + y, x
        i += 1
    return i


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    answer = solve()
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(f"Answer: {answer}")
    print(f"Time:   {elapsed_ms:.1f} ms")

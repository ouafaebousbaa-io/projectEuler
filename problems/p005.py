"""
Project Euler Problem 5: Smallest Multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""


def prime_factors(n):
    """Return the prime factorization of n as {prime: power}.

    Example: prime_factors(24) -> {2: 3, 3: 1}   (since 24 = 2^3 * 3)
             prime_factors(16) -> {2: 4}         (since 16 = 2^4)
    """
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        # whatever's left over is itself prime
        factors[n] = factors.get(n, 0) + 1
    return factors


def solve(N=20):
    # Steps 1 & 2: factor each i in 2..N, and for each prime,
    # remember the highest power we've ever seen.
    max_powers = {}
    for i in range(2, N + 1):
        for prime, power in prime_factors(i).items():
            if power > max_powers.get(prime, 0):
                max_powers[prime] = power

    # Step 3: multiply p^k for each (prime, max_power) pair.
    result = 1
    for prime, power in max_powers.items():
        result *= prime ** power
    return result


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    answer = solve()
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(f"Answer: {answer}")
    print(f"Time:   {elapsed_ms:.2f} ms")

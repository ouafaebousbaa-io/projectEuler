"""
Project Euler Problem 10: Summation of Primes
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

LIMIT = 2_000_000


def solve(N=LIMIT):
    """Sieve of Eratosthenes: cross out composites, sum what survives."""
    sieve = [True] * N
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    for p in range(2, int(N ** 0.5) + 1):
        if sieve[p]:
            # multiples below p*p were already crossed by smaller primes
            for multiple in range(p * p, N, p):
                sieve[multiple] = False

    return sum(i for i, is_prime in enumerate(sieve) if is_prime)


def solve_trial_division(N=LIMIT):
    """Trial division: test each candidate against the primes found so far.

    Same algorithm shape that we worked through by hand. Kept for a
    side-by-side runtime comparison against the sieve.
    """
    primes = [2, 3, 5, 7]
    total = 2 + 3 + 5 + 7

    for i in range(8, N):
        is_prime = True
        for j in primes:
            if j * j > i:        # only need to test divisors up to sqrt(i)
                break
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            total += i

    return total


if __name__ == "__main__":
    import time

    for name, fn in (("sieve", solve), ("trial division", solve_trial_division)):
        start = time.perf_counter()
        answer = fn()
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"{name:>16}:  answer = {answer}   ({elapsed_ms:.1f} ms)")

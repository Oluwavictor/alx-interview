#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game.Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a
    prime number from the set and removing that number and its
    multiples from the set.
    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True] * n
    primes[0] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i - 1]:
            for j in range(i * i, n, i):
                primes[j - 1] = False

    # Count the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = sum(1 for i in range(n) if primes[i])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'

from collections.abc import Iterable
from string import ascii_lowercase


def multiply_recursive(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if b < 0:
        raise ValueError("b must be non-negative")
    if b == 0:
        return 0
    return a + multiply_recursive(a, b - 1)


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def hanoi_moves(
    n: int, source: str, target: str, spare: str
) -> list[tuple[str, str]]:
    if n < 1:
        raise ValueError("n must be at least 1")

    if n == 1:
        return [(source, target)]

    return (
        hanoi_moves(n - 1, source, spare, target)
        + [(source, target)]
        + hanoi_moves(n - 1, spare, target, source)
    )


def fibonacci_rabbits(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return fibonacci_rabbits(n - 1) + fibonacci_rabbits(n - 2)


def fibonacci_memo(
    n: int, memo: dict[int, int] | None = None
) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    if memo is None:
        memo = {0: 1, 1: 1}

    if n in memo:
        return memo[n]

    memo[n] = (
        fibonacci_memo(n - 1, memo)
        + fibonacci_memo(n - 2, memo)
    )

    return memo[n]


def is_palindrome(text: str) -> bool:
    normalized = "".join(
        char.lower()
        for char in text
        if char.lower() in ascii_lowercase
    )

    def check(value: str) -> bool:
        if len(value) <= 1:
            return True

        return (
            value[0] == value[-1]
            and check(value[1:-1])
        )

    return check(normalized)


def lyrics_to_frequencies(
    lyrics: Iterable[str],
) -> dict[str, int]:
    frequencies = {}

    for word in lyrics:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def most_common_words(
    frequencies: dict[str, int],
) -> tuple[list[str], int]:
    if not frequencies:
        raise ValueError("frequencies must not be empty")

    highest = max(frequencies.values())

    words = [
        word
        for word, count in frequencies.items()
        if count == highest
    ]

    return words, highest


def words_often(
    frequencies: dict[str, int],
    min_times: int,
) -> list[tuple[list[str], int]]:
    if min_times < 1:
        raise ValueError("min_times must be at least 1")

    remaining = dict(frequencies)
    result = []

    while remaining:
        words, frequency = most_common_words(remaining)

        if frequency < min_times:
            break

        result.append((words, frequency))

        for word in words:
            del remaining[word]

    return result


if __name__ == "__main__":
    print("6 * 4 =", multiply_recursive(6, 4))
    print("5! =", factorial(5))
    print("Hanoi:", hanoi_moves(3, "A", "C", "B"))
    print("Fibonacci:", fibonacci_rabbits(6))
    print("Fast Fibonacci:", fibonacci_memo(34))
    print(is_palindrome("Able was I, ere I saw Elba"))

    lyrics = [
        "hello",
        "world",
        "hello",
        "python",
        "world",
        "hello",
    ]

    frequencies = lyrics_to_frequencies(lyrics)
    print(frequencies)
    print(most_common_words(frequencies))
    print(words_often(frequencies, 2))
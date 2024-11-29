def prime_factorization(n):
    """Helper function to get the prime factorization of a number."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)

    return factors


def get_sum_of_digits(l: list[int]) -> int:
    total = 0
    for val in l:
        _n = val
        while _n > 0:
            div, mod = divmod(_n, 10)
            total += mod
            _n = div

    return total


def is_smith_number_02(n: int) -> bool:
    local_array = prime_factorization(n)
    if len(local_array) == 1:
        return False

    total = get_sum_of_digits(local_array)
    n_total = get_sum_of_digits([n])
    if total == n_total:
        return True

    return False


def main() -> None:
    for val in range(1, 500):
        if is_smith_number_02(val):
            print(val)


if __name__ == '__main__':
    main()

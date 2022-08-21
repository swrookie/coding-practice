def solve(M: int, N: int) -> str:
    primes = [0] * (N + 1)
    primes[1] = -1

    total = 0
    min_num = N + 1
    for i in range(M, N + 1):
        if primes[i] == -1:
            continue

        divisible = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                divisible = j

        if divisible == 1:
            total += i
            min_num = min(i, min_num)
            for j in range(i + i, N + 1, i):
                primes[i] = -1

    if total == 0 and min_num == N + 1:
        return str(-1)

    return str(total) + "\n" + str(min_num)


def main():
    M = int(input())
    N = int(input())

    print(solve(M, N))


if __name__ == "__main__":
    main()

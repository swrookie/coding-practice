def solve(n: int) -> str:
    fibs = [0, 1]
    if n == 0 or n == 1:
        return str(fibs[n])

    sum = 0
    for i in range(2, n + 1, 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return str(fibs[n])


def main():
    n = int(input())
    print(solve(n))


if __name__ == "__main__":
    main()

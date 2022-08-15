def solve(N: int, K: int) -> str:
    answer = 0
    k = 0
    for i in range(1, N + 1, 1):
        if N % i == 0:
            k += 1
            if k == K:
                return str(i)

    return str(answer)


def main():
    N, K = map(int, input().split())

    print(solve(N, K))


if __name__ == "__main__":
    main()

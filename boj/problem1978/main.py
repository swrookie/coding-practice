from typing import List


def solve(arr: List[int]) -> str:
    answer = 0
    max_num = max(arr)
    primes = [0] * (max_num + 1)

    primes[1] = -1

    cnt = 0
    for num in arr:
        if primes[num] == -1:
            continue

        divisible = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisible = i

        if divisible == 1:
            cnt += 1
            for i in range(num, max_num + 1, num):
                primes[i] = -1

    answer = cnt

    return str(answer)


def main():
    N = int(input())
    arr = list(map(int, input().split()))

    print(solve(arr))


if __name__ == "__main__":
    main()

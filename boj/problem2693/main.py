from typing import List


def solve(arrs: List[List[int]]) -> str:
    answer = []
    for arr in arrs:
        arr.sort()
        answer.append(arr[-3])

    return "\n".join(map(str, answer))


def main():
    T = int(input())

    arrs = []
    for i in range(T):
        arr = list(map(int, input().split()))
        arrs.append(arr)

    print(solve(arrs))


if __name__ == "__main__":
    main()

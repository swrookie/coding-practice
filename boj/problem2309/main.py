from typing import List


N = 9
real_N = 7
answers = []


def backtrack(depth: int, visited: List[bool], arr: List[int], combs: List[int]):
    if depth == real_N:
        temp = [v for v in combs]

        if sum(temp) == 100:
            answers.append(temp)

        return

    for i in range(depth, len(arr)):
        if not visited[i]:
            visited[i] = True
            combs.append(arr[i])
            backtrack(depth + 1, visited, arr, combs)
            combs.pop()
            visited[i] = False


def solve(arr: List[int]):
    visited = [False] * N
    combs = []

    backtrack(0, visited, arr, combs)

    return "\n".join(map(str, sorted(answers[0])))


def main():
    arr = []
    for i in range(N):
        height = int(input())
        arr.append(height)

    print(solve(arr))


if __name__ == "__main__":
    main()

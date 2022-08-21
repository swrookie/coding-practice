MAX_NUM = 1000


def solve(A: int, B: int) -> str:
    arr = [0] * (MAX_NUM + 1)

    num = 1
    counter = 0
    for i in range(1, MAX_NUM + 1):
        arr[i] = num
        counter += 1
        if num == counter:
            num += 1
            counter = 0

    return str(sum(arr[A : B + 1]))


def main():
    A, B = map(int, input().split())

    print(solve(A, B))


if __name__ == "__main__":
    main()

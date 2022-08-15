from typing import List


def solve(nums: List[int]):
    max_num = -1000000
    min_num = 1000000

    for num in nums:
        min_num = min(num, min_num)
        max_num = max(num, max_num)

    return " ".join([str(min_num), str(max_num)])


def main():
    N = int(input())
    nums = map(int, input().split())

    print(solve(nums))


if __name__ == "__main__":
    main()

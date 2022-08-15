from typing import List


def solve(people_cnts: List[List[int]]) -> str:
    curr_cnt = 0
    max_cnt = -1
    for cnts in people_cnts:
        curr_cnt = curr_cnt - cnts[0] + cnts[1]
        max_cnt = max(curr_cnt, max_cnt)

    return str(max_cnt)


def main():
    people_cnts = []
    for i in range(10):
        offboard, onboard = map(int, input().split())
        people_cnts.append([offboard, onboard])

    print(solve(people_cnts))


if __name__ == "__main__":
    main()

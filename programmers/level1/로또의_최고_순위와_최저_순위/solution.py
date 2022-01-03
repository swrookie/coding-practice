def solution(lottos, win_nums):
    answer = [0, 0]

    match = 0
    zeros = lottos.count(0)

    for win_num in win_nums:
        if win_num in lottos:
            match += 1

    answer[0] = 7 - (match + zeros) if 7 - (match + zeros) < 7 else 6
    answer[1] = 7 - match if 7 - match < 7 else 6

    return answer


if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    print(solution(lottos, win_nums))

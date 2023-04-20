def solution(n):
    answer = 0

    nums = [0] * (n + 1)
    #     for i in range(2, n):
    #         if nums[i]:
    #             continue

    #         divisible_cnt = 0
    #         for j in range(1, i // 2):
    #             if i % j == 0:
    #                 divisible_cnt += 1
    #         if divisible_cnt >= 3:
    #             answer += 1
    #         for k in range(i + i, n + 1, i):
    #             if nums[k]:
    #                 continue
    #             nums[k] = 1
    #             answer += 1

    for i in range(2, n + 1):
        for j in range(i + i, n + 1, i):
            if nums[j]:
                continue
            nums[j] = 1
            answer += 1

    return answer


if __name__ == "__main__":
    test_cases = (10, 15)
    for case in test_cases:
        print(solution(case))

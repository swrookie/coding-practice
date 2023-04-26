def solution(num_list, n):
    answer = [num_list[i : i + n] for i in range(0, len(num_list), n)]
    return answer


if __name__ == "__main__":
    test_cases = (([1, 2, 3, 4, 5, 6, 7, 8], 2), ([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))
    for case in test_cases:
        num_list, n = case
        print(solution(num_list, n))

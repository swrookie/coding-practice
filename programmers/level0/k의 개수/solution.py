def solution(i, j, k):
    answer = "".join(str(i) for i in range(i, j + 1)).count(str(k))
    # answer = sum(str(i).count(str(k)) for i in range(i, j + 1))
    return answer


if __name__ == "__main__":
    test_cases = ((1, 3, 1), (10, 50, 5), (3, 10, 2))
    for case in test_cases:
        print(solution(case[0], case[1], case[2]))

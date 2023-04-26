def solution(numbers, k):
    answer = (numbers * k)[::2][k - 1]
    # answer = numbers[2 * (k - 1) % len(numbers)] 한사람 건너뛰니까 k - 1인덱스에서 2 곱하고 배열 길이로 나눈 몫
    return answer


if __name__ == "__main__":
    test_cases = (([1, 2, 3, 4], 2), ([1, 2, 3, 4, 5, 6], 5), ([1, 2, 3], 3))
    for case in test_cases:
        numbers, k = case
        print(solution(numbers, k))

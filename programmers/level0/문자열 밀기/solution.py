def solution(A, B):
    answer = 0
    if A == B:
        return answer

    size = len(A)

    cnt = 0
    for i in range(size):
        A = "".join([A[size - 1], A[: size - 1]])

        cnt += 1
        if A == B:
            return cnt

    answer = -1
    return answer

if __name__ == "__main__":
    test_cases = [("hello", "ohell"), ("apple", "elppa"), ("atat", "tata"), ("abc", "abc")]
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
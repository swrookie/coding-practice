def solution(box, n):
    answer = 0
    x, y, z = box
    x, y, z = x // n, y // n, z // n
    answer = x * y * z

    return answer


if __name__ == "__main__":
    test_cases = (([1, 1, 1], 1), ([10, 8, 6], 3))

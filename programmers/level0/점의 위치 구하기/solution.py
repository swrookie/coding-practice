def solution(dot):
    answer = 0

    # quad = [(3,2),(4,1)]
    # return quad[dot[0] > 0][dot[1] > 0]
    x, y = dot
    if x > 0 and y > 0:
        answer = 1
    elif x < 0 and y > 0:
        answer = 2
    elif x < 0 and y < 0:
        answer = 3
    else:
        answer = 4

    return answer


if __name__ == "__main__":
    test_cases = ([2, 4], [-7, 9])
    for case in test_cases:
        print(solution(case))

def solution(dots):
    answer = 0

    dot1, dot2, dot3, dot4 = dots
    width, height = 0, 0

    if dot1[0] != dot2[0] and dot1[1] == dot2[1]:
        width = abs(dot1[0] - dot2[0])
    elif dot1[0] != dot3[0] and dot1[1] == dot3[1]:
        width = abs(dot1[0] - dot3[0])
    elif dot1[0] != dot4[0] and dot1[1] == dot4[1]:
        width = abs(dot1[0] - dot4[0])

    if dot1[0] == dot2[0] and dot1[1] != dot2[1]:
        height = abs(dot1[1] - dot2[1])
    elif dot1[0] == dot3[0] and dot1[1] != dot3[1]:
        height = abs(dot1[1] - dot3[1])
    elif dot1[0] == dot4[0] and dot1[1] != dot4[1]:
        height = abs(dot1[1] - dot4[1])

    answer = width * height

    # 변이 축과 평행해서 좌표들의 최대와 최소의 좌표의 x, y의 차를 곱하면 된다..
    # return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

    return answer


if __name__ == "__main__":
    test_cases = ([[1, 1], [2, 1], [2, 2], [1, 2]], [[-1, -1], [1, 1], [1, -1], [-1, 1]])

    for case in test_cases:
        print(solution(case))

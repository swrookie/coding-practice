def solution(lines):
    answer = 0

    N = 3
    M = 2
    visited = [False] * N
    temp = [0] * M
    result = []  # 겹치는 구간

    def combination(N, M, depth, idx):
        if depth == M:
            print("temp", temp)
            line1, line2 = temp

            if line1[0] > line2[0]:
                line1, line2 = line2, line1

            if line1[1] == line2[0]:
                return

            temp_line = []
            coords1 = range(line1[0], line1[1] + 1)
            for i in range(line2[0], line2[1] + 1):
                if i in coords1:
                    temp_line.append(i)

            if temp_line:
                result.append([min(temp_line), max(temp_line)])
            return

        for i in range(idx, N):
            temp[depth] = lines[i]
            combination(N, M, depth + 1, i + 1)

    combination(N, M, 0, 0)
    print("final result: ", result)
    # answer = sum(result) - 1 if sum(result) != 0 else 0

    if not result:
        return 0

    lines = sorted(lines, key=lambda x: (x[0], x))
    # print(lines)
    result = sorted(result, key=lambda x: (x[0], x))
    # line1, line2, line3 = result
    # if line1[1] == line2[0] and line2[1] == line3[0]:
    #     return answer

    processed = []
    lines = result

    # print("lines: ", lines)
    for line in lines:
        start, end = line
        for idx, i in enumerate(range(start, end + 1)):
            if i in processed:
                continue
            if idx > 0:
                answer += 1
            processed.append(i)
        # print(answer)

    return answer

# 순열: 순서가 있는 조합
# 조합: 순서가 없는 조합
# 백트래킹: 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾는 기법 (모든 경우의 수를 전부 고려하는 알고리즘)
# 참고: https://velog.io/@1998yuki0331/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
def solution(babbling):
    answer = 0

    possibles = ["aya", "ye", "woo", "ma"]  # 목록
    N = len(possibles)  # 목록 개수
    result = []  # 결과들
    temp_result = []  # 임시 연산 결과
    visited = [False] * N  # 백트래킹 추적

    # 백트래킹 순열
    def permutation(N, M, depth):
        if depth == M:
            temp = "".join([r for r in temp_result])
            result.append(temp)
            return

        for i in range(N):
            if visited[i] is False:
                visited[i] = True
                temp_result[depth] = possibles[i]
                permutation(N, M, depth + 1)
                visited[i] = False  # 백트래킹 추적 안하면 중복 허용

    for i in range(1, N + 1):
        temp_result = [0] * i
        permutation(N, i, 0)

    for babble in babbling:
        if babble in result:
            answer += 1

    return answer


if __name__ == "__main__":
    test_cases = [["aya", "yee", "u", "maa", "wyeoo"], ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]]
    for test_case in test_cases:
        print(solution(test_case))

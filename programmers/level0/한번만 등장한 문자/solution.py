def solution(s):
    answer = ''
#     d = {}
#     for c in s:
#         d[c] = d.setdefault(c, 0) + 1
    
#     answer = "".join(sorted([k for k, v in d.items() if v == 1]))
    # dict 생성 필요 없이 (문자열안에 문자가 몇개 있는지 카운트하는 함수 사용) 해결 가능한 솔루션 참고함
    answer = "".join(sorted([c for c in s if s.count(c) == 1]))
    
    return answer

if __name__ == "__main__":
    test_cases = ("abcabcadc", "abdc", "hello")
    for case in test_cases:
        print(solution(case))
def solution(hp):
    answer = 0
    def cnt_remain(x):
        if x < 1:
            return 0
        elif x < 3:
            return x // 1
        elif x < 5:
            div, mod = divmod(x, 3)
            return div + mod
    
    if hp < 5:
        answer = cnt_remain(hp)
        return answer
    
    div, mod = divmod(hp, 5)
    answer += div
    answer += cnt_remain(mod)

    # return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3) 그냥 개미종류별로 계속 나누는 모수 합하면 됐었다..
    return answer

if __name__ == "__main__":
    test_cases = (23, 24, 999)
    for case in test_cases:
        print(solution(case))
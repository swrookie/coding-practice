def solution(spell, dic):
    answer = 2
    spelled = "".join(sorted(spell))

    for word in dic:
        if spelled == "".join(sorted(word)):
            answer = 1
            break

    # 정렬 불필요, set활용, -는 차집합
    # spelled = set(spell)
    # for word in dic:
    #     if not spelled - set(word):
    #         answer = 1
    #         break

    return answer


if __name__ == "__main__":
    test_cases = (
        (["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]),
        (["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]),
        (["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]),
    )
    for case in test_cases:
        spell, dic = case
        print(solution(spell, dic))

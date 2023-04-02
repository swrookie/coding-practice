def solution(id_pw, db):
    answer = ""

    if id_pw in db:
        return "login"
    elif id_pw[0] in [info[0] for info in db]:
        return "wrong pw"
    else:
        return "fail"

    # return answer


if __name__ == "__main__":
    test_cases = (["meosseugi", "1234"], ["programmer01", "15789"], ["rabbit04", "98761"])
    for case in test_cases:
        print(solution(case[0], case[1]))

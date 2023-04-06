def solution(polynomial):
    answer = ""
    x_cnt = 0
    num = 0

    for c in polynomial.split(" + "):
        if c != "x" and not c.isdigit():
            x_cnt += int(c.replace("x", ""))
        elif c != "x" and c.isdigit():
            num += int(c)
        else:
            x_cnt += 1

    x = ""
    if x_cnt == 1:
        x = x.join(["x"])
    elif x_cnt > 1:
        x = x.join([str(x_cnt), "x"])

    var_addition = ""
    if num > 0:
        var_addition = var_addition.join([str(num)])

    answer = answer.join([x, " + ", var_addition]) if x_cnt > 0 and num > 0 else answer.join([x, var_addition])

    return answer


if __name__ == "__main__":
    test_cases = ("3x + 7 + x", "x + x + x")
    for case in test_cases:
        print(solution(case))

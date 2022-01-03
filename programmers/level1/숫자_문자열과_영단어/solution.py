def solution(s):
    answer = 0

    num_eng_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    if not s.isdigit():
        num_eng_keys = num_eng_dict.keys()
        eng_num = []
        temp = ""

        for c in s:
            if c.isdigit():
                eng_num.append(c)
            else:
                temp = "".join([temp, c])

                if temp in num_eng_keys:
                    eng_num.append(num_eng_dict[temp])
                    temp = ""
                else:
                    continue

        answer = int("".join(eng_num))

    else:
        answer = int(s)

    return answer


if __name__ == "__main__":
    print(solution("one4seveneight"))

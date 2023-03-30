def solution(numbers):
    answer = 0
    d = {
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

    for k, v in d.items():
        numbers = numbers.replace(k, v)
        # print(k, v)

    answer = int(numbers)

    #     l = []
    #     l2 = []
    #     for c in numbers:
    #         l.append(c)
    #         num = "".join(l)
    #         if num in d.keys():
    #             l2.append(d.get(num))
    #             l.clear()

    #     answer = sum(num * pow(10, len(l2) - idx - 1) for idx, num in enumerate(l2))

    return answer

if __name__ == "__main__":
    test_cases = ("onetwothreefourfivesixseveneightnine", "onefourzerosixseven")
    for case in test_cases:
        print(solution(case))
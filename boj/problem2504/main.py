# 분배 법칙
def solve(brackets: str) -> str:
    answer = 0
    st = []

    temp = 1
    for idx, bracket in enumerate(brackets):
        if bracket == "(":
            temp *= 2
            st.append(bracket)
        elif bracket == "[":
            temp *= 3
            st.append(bracket)
        elif bracket == ")":
            if not st or st[-1] != "(":
                answer = 0
                break
            elif brackets[idx - 1 : idx] == "(":
                answer += temp
                temp //= 2
                st.pop()
            elif brackets[idx - 1 : idx] != "(":
                temp //= 2
                st.pop()
        elif bracket == "]":
            if not st or st[-1] != "[":
                answer = 0
                break
            elif brackets[idx - 1 : idx] == "[":
                answer += temp
                temp //= 3
                st.pop()
            elif brackets[idx - 1 : idx] != "[":
                temp //= 3
                st.pop()

    if st:
        return "0"

    return str(answer)


def main():
    brackets = input()

    print(solve(brackets))


if __name__ == "__main__":
    main()

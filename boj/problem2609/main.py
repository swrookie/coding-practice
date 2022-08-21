def solve(num1: int, num2: int) -> str:
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    gcd = 0
    lcm = 0

    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break

    increment = max_num
    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            lcm = max_num
            break

        max_num += increment

    return "\n".join(map(str, [gcd, lcm]))


def main():
    num1, num2 = map(int, input().split())

    print(solve(num1, num2))


if __name__ == "__main__":
    main()

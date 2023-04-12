def solution(n):
    answer = []

    prime_net = [0] * (n + 1)

    def is_prime(num):
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False

        return True

    for i in range(2, n + 1):
        if prime_net[i] != -1 and is_prime(i) and n % i == 0:
            answer.append(i)
            for j in range(i, n + 1, i):
                prime_net[j] = -1

    # answer = [i for i in range(2, n + 1) if is_prime(i) and n % i == 0]

    return answer


if __name__ == "__main__":
    test_cases = (12, 17, 420)
    for case in test_cases:
        print(solution(case))

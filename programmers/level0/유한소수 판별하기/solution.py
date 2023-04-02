def solution(a, b):
    answer = 1

    # 유클리드 호제법 활용한 최대공약수 구하기
    # math 모듈의 gcd함수 활용해서 구하는 것도 가능
    # 참고: https://brownbears.tistory.com/454
    def get_gcd(a, b):
        while b:
            a, b = b, a % b

        return a

    gcd = get_gcd(a, b)
    b = b // gcd

    for i in range(2, b + 1):
        if b % i == 0:
            is_prime = True
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime and i not in (2, 5):
                return 2

    # 분모를 2나 5인 소인수로 계속 나눴을 때 최종값이 1이 아니면 해당 소인수로만 나눠지진 않기 때문?
    # while b%2==0:
    #     b//=2
    # while b%5==0:
    #     b//=5
    # return 1 if b==1 else 2

    return answer


if __name__ == "__main__":
    test_cases = (([1, 2, 3, 4, 5, 6], 4), ([10000, 20, 36, 47, 40, 6, 10, 7000], 30))
    for case in test_cases:
        print(solution(case[0], case[1]))

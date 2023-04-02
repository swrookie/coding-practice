def solution(chicken):
    answer = 0

    # coupon = 0
    while chicken >= 10:
        chicken, coupon_left = divmod(chicken, 10)
        print(chicken, coupon_left)
        answer += chicken
        chicken += coupon_left

        # if coupon > 9:
        #     extra_chicken, coupon = divmod(coupon, 10)
        #     answer += extra_chicken
        #     chicken += extra_chicken

    # return int(chicken*0.11111111111) 이런 방법도 있네..
    return answer


if __name__ == "__main__":
    test_cases = (100, 1081)
    for case in test_cases:
        print(solution(case))

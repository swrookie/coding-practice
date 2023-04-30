def solution(num_list):
    answer = []
    even_cnt, odd_cnt = 0, 0
    for num in num_list:
        if num % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    answer.append(even_cnt)
    answer.append(odd_cnt)
    # 인덱스를 짝수, 홀수에 대한 카운트로 활용
    # answer = [0,0]
    # for n in num_list:
    #     answer[n%2]+=1
    return answer


if __name__ == "__main__":
    test_cases = ([1, 2, 3, 4, 5], [1, 3, 5, 7])
    for case in test_cases:
        print(solution(case))

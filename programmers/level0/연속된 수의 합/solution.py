def solution(num, total):
    answer = []
    
    answer.append(total // num)
    
    while len(answer) < num:
        first_num = answer[0]
        last_num = answer[-1]
        answer.insert(0, first_num - 1)
        answer.append(last_num + 1)
    
    sum_num = sum(answer)
    if sum_num != total:
        if sum_num - answer[0] == total:
            answer.pop(0)
        else:
            answer.pop(-1)
        
    return answer

if __name__ == "__main__":
    test_cases = [[3, 12], [5, 15], [4, 14], [5, 5]]
    for test_case in test_cases:
        print(solution(test_case[0], test_case[1]))
def solution(rsp):
    counter_rsp = {"2": "0", "0": "5", "5": "2"}
    answer = "".join([counter_rsp.get(c) for c in rsp])
    
    return answer

if __name__ == "__main__":
    test_cases = ("2", "205")
    for case in test_cases:
        print(solution(case))
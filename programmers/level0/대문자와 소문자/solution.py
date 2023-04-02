def solution(my_string):
#     def convert_case(c):
#         return c.upper() if c.islower() else c.lower()
    
#     answer = "".join([convert_case(c) for c in my_string])
    answer = my_string.swapcase()
    return answer

if __name__ == "__main__":
    test_cases = ("cccCCC", "abCdEfghIJ")
    for case in test_cases:
        print(solution(case))
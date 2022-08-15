def solve(N: int) -> str:
    answer = 0
    one_start_arr = [0, 1]
    zero_start_arr = [0, 1]

    if N == 1 or N == 2:
        return str(one_start_arr[N - 1])

    for i in range(2, N, 1):
        prev_one_start_zero_cnt = one_start_arr[1]
        prev_zero_start_zero_cnt = zero_start_arr[1]

        if (i - 1) % 2 != 0:
            one_start_arr[1] = prev_one_start_zero_cnt + prev_zero_start_zero_cnt - 1
            one_start_arr[0] = prev_one_start_zero_cnt
            zero_start_arr[1] = prev_one_start_zero_cnt + prev_zero_start_zero_cnt
            zero_start_arr[0] = prev_zero_start_zero_cnt
        else:
            one_start_arr[1] = prev_one_start_zero_cnt + prev_zero_start_zero_cnt
            one_start_arr[0] = prev_one_start_zero_cnt
            zero_start_arr[1] = prev_one_start_zero_cnt + prev_zero_start_zero_cnt
            zero_start_arr[0] = prev_zero_start_zero_cnt

    answer = one_start_arr[1]

    return str(answer)


def main():
    N = int(input())

    print(solve(N))


if __name__ == "__main__":
    main()

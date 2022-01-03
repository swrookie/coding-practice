import math

# 유클리드 거리 구하기 (피타고라스 공식이랑 비슷한 것 같다)
def euclidean_distance(coord_one, coord_two):
    return math.sqrt(abs(coord_one[0] - coord_two[0]) + abs(coord_one[1] - coord_two[1]))


# 맨해튼 거리 (이 문제에선 이 공식이 맞는 것 같다)
def manhattan_distance(coord_one, coord_two):
    return abs(coord_one[0] - coord_two[1]) + abs(coord_one[1] + coord_two[1])


def solution(numbers, hand):
    answer = ""

    right_thumb_loc = "#"
    left_thumb_loc = "*"

    key_pad = {
        "1": [0, 0],
        "2": [0, 1],
        "3": [0, 2],
        "4": [1, 0],
        "5": [1, 1],
        "6": [1, 2],
        "7": [2, 0],
        "8": [2, 1],
        "9": [2, 2],
        "*": [3, 0],
        "0": [3, 1],
        "#": [3, 2],
    }

    thumbs = []
    for number in numbers:
        if number in [1, 4, 7]:
            left_thumb_loc = str(number)
            thumbs.append("L")
        elif number in [3, 6, 9]:
            right_thumb_loc = str(number)
            thumbs.append("R")
        else:
            right_dist = manhattan_distance(key_pad.get(right_thumb_loc), key_pad.get(str(number)))
            left_dist = manhattan_distance(key_pad.get(left_thumb_loc), key_pad.get(str(number)))

            if right_dist < left_dist:
                thumbs.append("R")
                right_thumb_loc = str(number)
            elif left_dist < right_dist:
                thumbs.append("L")
                left_thumb_loc = str(number)
            else:
                if hand == "right":
                    thumbs.append("R")
                    right_thumb_loc = str(number)
                else:
                    thumbs.append("L")
                    left_thumb_loc = str(number)

    answer = "".join(thumbs)

    return answer


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

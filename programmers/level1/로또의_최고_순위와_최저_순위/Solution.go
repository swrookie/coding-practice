package main

import "fmt"

func solution(lottos []int, win_nums []int) []int {
	match, zeros := 0, 0

	for _, e := range lottos {
		if e == 0 {
			zeros++
		}
	}

	for _, e1 := range win_nums {
		for _, e2 := range lottos {
			if e1 == e2 {
				match++
				break
			}
		}
	}

	maxRank, minRank := 0, 0

	if 7-(match+zeros) < 7 {
		maxRank = 7 - (match + zeros)
	} else {
		maxRank = 6
	}

	if 7-match < 7 {
		minRank = 7 - match
	} else {
		minRank = 6
	}

	return []int{maxRank, minRank}
}

func main() {
	lottos := []int{44, 1, 0, 0, 31, 25}
	win_nums := []int{31, 10, 45, 1, 6, 19}

	fmt.Println(solution(lottos, win_nums))
}

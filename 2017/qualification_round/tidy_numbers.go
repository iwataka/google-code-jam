package main

import (
	"fmt"
	"strconv"
)

func main() {
	var numOfTestCases int
	fmt.Scanf("%d", &numOfTestCases)
	for i := 0; i < numOfTestCases; i++ {
		var line string
		fmt.Scanf("%s", &line)
		arr, err := ConvertLineToIntArr(line)
		if err != nil {
			panic(err)
		}
		Solve(arr)
		answer, err := CombineIntArrToInt(arr)
		if err != nil {
			panic(err)
		}
		fmt.Printf("Case #%d: %d\n", i+1, answer)
	}
}

func ConvertLineToIntArr(line string) ([]int, error) {
	arr := []int{}
	for _, c := range line {
		i, err := strconv.Atoi(string(c))
		if err != nil {
			return nil, err
		}
		arr = append(arr, i)
	}
	return arr, nil
}

func CombineIntArrToInt(max []int) (int, error) {
	result := ""
	reachOtherThan0 := false
	for _, i := range max {
		if i == 0 && !reachOtherThan0 {
			continue
		} else {
			reachOtherThan0 = true
		}
		result += strconv.Itoa(i)
	}
	resultInt, err := strconv.Atoi(result)
	if err != nil {
		return -1, err
	}
	return resultInt, nil
}

func Solve(max []int) {
	len := len(max)
	for i := len - 1; i > 0; i-- {
		onCursor := max[i]
		left := max[i-1]
		if left > onCursor {
			max[i] = 9
			max[i-1] = max[i-1] - 1
			for j := 1; i+j < len; j++ {
				max[i+j] = 9
			}
		}
	}
}

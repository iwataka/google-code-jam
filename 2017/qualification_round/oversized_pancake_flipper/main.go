package main

import (
	"fmt"
)

func main() {
	var numOfTestCases int
	fmt.Scanf("%d", &numOfTestCases)
	for i := 0; i < numOfTestCases; i++ {
		var initialPancakesStr string
		var flipperSize int
		fmt.Scanf("%s %d", &initialPancakesStr, &flipperSize)
		initialPancakes := convertStringToInitialPancakeStates(initialPancakesStr)
		answer := Solve(initialPancakes, flipperSize)
		if answer == -1 {
			fmt.Printf("Case #%d: IMPOSSIBLE\n", i+1)
		} else {
			fmt.Printf("Case #%d: %d\n", i+1, answer)
		}
	}
}

func convertStringToInitialPancakeStates(str string) []bool {
	pancakeStates := []bool{}
	for _, c := range str {
		if c == '+' {
			pancakeStates = append(pancakeStates, true)
		} else if c == '-' {
			pancakeStates = append(pancakeStates, false)
		}
	}
	return pancakeStates
}

func Solve(pancakeStates []bool, flipperSize int) int {
	count := 0
	for i := 0; i <= len(pancakeStates)-flipperSize; i++ {
		if pancakeStates[i] {
			continue
		}
		for j := 0; j < flipperSize; j++ {
			pancakeStates[i+j] = !pancakeStates[i+j]
		}
		count++
	}

	for i := 1; i <= flipperSize; i++ {
		if len(pancakeStates)-i < 0 {
			break
		}
		if !pancakeStates[len(pancakeStates)-i] {
			return -1
		}
	}

	return count
}

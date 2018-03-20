package main

import (
	"fmt"
)

func main() {
	var numOfTestCases int
	fmt.Scanf("%d", &numOfTestCases)
	for i := 0; i < numOfTestCases; i++ {
		var nStalls, nPerson int
		fmt.Scanf("%d %d", &nStalls, nPerson)
		max, min := Solve(nStalls, nPerson)
		fmt.Printf("Case #%d: %d %d\n", i+1, max, min)
	}
}

func divideAll(max int, largerCount int, smallerCount int) (int, int, int) {
	if max%2 == 0 {
		newMax := max / 2
		newLargerCount := largerCount
		newSmallerCount := largerCount + smallerCount*2
		return newMax, newLargerCount, newSmallerCount
	} else {
		newMax := (max - 1) / 2
		newLargerCount := largerCount*2 + smallerCount
		newSmallerCount := smallerCount
		return newMax, newLargerCount, newSmallerCount
	}
}

func Solve(nStalls int, nPersons int) (int, int) {
	max := nStalls
	largerCount := 1
	smallerCount := 0
	for nPersons > largerCount+smallerCount {
		nPersons -= largerCount
		nPersons -= smallerCount
		max, largerCount, smallerCount = divideAll(max, largerCount, smallerCount)
	}

	return divide(max, largerCount, smallerCount, nPersons)
}

func divide(max, largerCount, smallerCount, nPersons int) (int, int) {
	if nPersons <= largerCount {
		if max%2 == 0 {
			return max / 2, (max / 2) - 1
		} else {
			return (max - 1) / 2, (max - 1) / 2
		}
	} else {
		if max%2 == 0 {
			return (max / 2) - 1, (max / 2) - 1
		} else {
			return (max - 1) / 2, ((max - 1) / 2) - 1
		}
	}
}

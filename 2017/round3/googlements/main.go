package main

import (
	"fmt"
	"reflect"
	"sort"
	"strconv"
)

func main() {
	var nTests int
	fmt.Scanf("%d\n", &nTests)
	for i := 0; i < nTests; i++ {
		var val string
		fmt.Scanf("%s\n", &val)
		fmt.Println(val)
		vs := val2IntArr(val)
		count := solve(vs)
		fmt.Printf("Case #%d: %d\n", i+1, count)
	}
}

func val2IntArr(val string) []int {
	result := []int{}
	for _, c := range val {
		i, _ := strconv.Atoi(string(c))
		result = append(result, i)
	}
	return result
}

func solve(vs []int) int {
	if !isValidGooglement(vs) {
		return 1
	}

	count := 0
	perms := permutations(getAncestorNums(vs))
	for _, perm := range perms {
		if reflect.DeepEqual(perm, vs) {
			continue
		}
		c := solve(perm)
		count += c
	}

	return count
}

func getAncestorNums(vs []int) []int {
	var result []int
	for num, count := range vs {
		for i := 0; i < count; i++ {
			result = append(result, num)
		}
	}
	return result
}

func isValidGooglement(vs []int) bool {
	sum := 0
	for _, v := range vs {
		sum += v
	}
	if sum > len(vs) {
		return false
	}
	return true
}

func permutations(arr []int) [][]int {
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int) {
		if n == 1 {
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}

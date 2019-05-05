// Test set 1: Pass
// Test set 2: RE
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func factor(n int, N int) (int, int) {
	if n%2 == 0 {
		return 2, n / 2
	}

	min := 3

	for i := min; i < N; i += 2 {
		if n%i == 0 {
			return i, n / i
		}
	}

	panic("factor panic")
}

func startpos(nums []int) int {
	for i, n := range nums {
		if n != nums[i+1] {
			return i
		}
	}

	panic("panic startpos")
}

func decrypt(nums []int) []string {
	copied := make([]int, len(nums))
	copy(copied, nums)
	sort.Sort(sort.IntSlice(copied))
	n2c := map[int]string{}
	count := 0
	for _, n := range copied {
		if _, exists := n2c[n]; !exists {
			n2c[n] = string('A' + count)
			count += 1
		}
	}
	result := []string{}
	for _, n := range nums {
		result = append(result, n2c[n])
	}
	return result
}

func solve(N int, L int, nums []int) string {
	result := make([]int, len(nums)+1)
	var index int

	start := startpos(nums)
	index = start

	a, b := factor(nums[start], N)
	nextn := nums[start+1]
	var now int
	if nextn%a == 0 {
		result[index] = b
		result[index+1] = a
		now = nextn / a
	} else {
		result[index] = a
		result[index+1] = b
		now = nextn / b
	}
	result[index+2] = now
	index += 3

	for _, n := range nums[start+2:] {
		now = n / now
		result[index] = now
		index += 1
	}

	now = result[start]
	rest := nums[:start]
	copiedRest := make([]int, len(rest))
	copy(copiedRest, rest)
	sort.Sort(sort.Reverse(sort.IntSlice(copiedRest)))
	index = start - 1
	for _, n := range copiedRest {
		now = n / now
		result[index] = now
		index -= 1
	}

	decrypted := decrypt(result)
	return strings.Join(decrypted, "")
}

func main() {
	stdin := bufio.NewScanner(os.Stdin)
	stdin.Scan()
	nTests, _ := strconv.Atoi(stdin.Text())
	for i := 0; i < nTests; i++ {
		stdin.Scan()
		nlTexts := strings.Fields(stdin.Text())
		N, _ := strconv.Atoi(nlTexts[0])
		L, _ := strconv.Atoi(nlTexts[1])
		nums := []int{}
		stdin.Scan()
		numTexts := strings.Fields(stdin.Text())
		for _, t := range numTexts {
			n, _ := strconv.Atoi(t)
			nums = append(nums, n)
		}
		ans := solve(N, L, nums)
		fmt.Printf("Case #%d: %s\n", i+1, ans)
	}
}

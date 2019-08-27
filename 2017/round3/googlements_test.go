package main

import (
	"testing"
)

func TestSolve(t *testing.T) {
	count := 0
	count = solve([]int{2, 0})
	if count != 4 {
		t.Fatal(count)
	}
	count = solve([]int{1})
	if count != 1 {
		t.Fatal(count)
	}
	count = solve([]int{1, 2, 3})
	if count != 1 {
		t.Fatal(count)
	}
}

func TestPermutation(t *testing.T) {
	perms := [][]int{}
	perms = permutations([]int{1, 2, 2})
	if len(perms) != 3 {
		t.Fatal(len(perms))
	}
}

func TestVal2IntArr(t *testing.T) {
	var vs []int
	vs = val2IntArr("0305")
	if len(vs) != 4 {
		t.Fatal(len(vs))
	}
}

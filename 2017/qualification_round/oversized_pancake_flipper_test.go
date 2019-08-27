package main

import (
	"testing"
)

func TestSolve(t *testing.T) {
	var ans int
	ans = Solve([]bool{false, false, false}, 3)
	if ans != 1 {
		t.Fatal(ans)
	}
}

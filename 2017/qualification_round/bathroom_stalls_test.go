package main

import (
	"testing"
)

func TestDivideAll(t *testing.T) {
	var max, largerCount, smallerCount int
	max, largerCount, smallerCount = divideAll(4, 2, 3)
	if max != 2 || largerCount != 2 || smallerCount != 8 {
		t.Fail()
	}
	max, largerCount, smallerCount = divideAll(5, 2, 3)
	if max != 2 || largerCount != 7 || smallerCount != 3 {
		t.Fail()
	}
}

func TestDivide(t *testing.T) {
	var left, right int

	left, right = divide(3, 2, 1, 1)
	if left != 1 || right != 1 {
		t.Fatal(left, right)
	}

	left, right = divide(4, 2, 1, 1)
	if left != 2 || right != 1 {
		t.Fatal(left, right)
	}

	left, right = divide(3, 2, 1, 3)
	if left != 1 || right != 0 {
		t.Fatal(left, right)
	}

	left, right = divide(4, 2, 1, 3)
	if left != 1 || right != 1 {
		t.Fatal(left, right)
	}
}

func TestSolve(t *testing.T) {
	var left, right int
	left, right = Solve(10, 2)
	if left != 2 || right != 2 {
		t.Fatal(left, right)
	}
}

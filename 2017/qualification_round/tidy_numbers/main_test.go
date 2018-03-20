package main

import (
	"reflect"
	"testing"
)

func TestConvertLineToIntArr(t *testing.T) {
	var arr []int
	var err error
	arr, err = ConvertLineToIntArr("0123456789")
	if err != nil {
		t.Fatal(err)
	}
	for i, ele := range arr {
		if i != ele {
			t.Fatal(i, ele)
		}
	}
}

func TestCombineIntArrToInt(t *testing.T) {
	var ans int
	var err error

	ans, err = CombineIntArrToInt([]int{0, 1, 2, 0})
	if err != nil {
		t.Fatal(err)
	}
	if ans != 120 {
		t.Fatal(ans, 120)
	}

	ans, err = CombineIntArrToInt([]int{1, 1, 2, 0})
	if err != nil {
		t.Fatal(err)
	}
	if ans != 1120 {
		t.Fatal(ans, 1120)
	}
}

func TestSolve(t *testing.T) {
	max := []int{8, 7, 5, 3, 9}
	Solve(max)
	if !reflect.DeepEqual(max, []int{7, 9, 9, 9, 9}) {
		t.Fail()
	}
}

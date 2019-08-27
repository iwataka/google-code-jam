package main

import (
	"testing"
)

func TestPositionMap(t *testing.T) {
	m := map[Position]string{}
	m[Position{0, 0}] = "o"
	m[Position{0, 0}] = "x"
	m[Position{0, 1}] = "+"
	if len(m) != 2 {
		t.Fail()
	}
	if m[Position{0, 0}] != "x" {
		t.Fail()
	}
}

func TestSolveRooks(t *testing.T) {
	var ps []Position
	ps = solveRooks(8, []Position{})
	if len(ps) != 8 {
		t.Fatal(len(ps))
	}
	ps = solveRooks(1, []Position{})
	if len(ps) != 1 {
		t.Fatal(len(ps))
	}
	ps = solveRooks(2, []Position{Position{0, 0}})
	if len(ps) != 1 {
		t.Fatal(len(ps))
	}
}

func TestSolveBishops(t *testing.T) {
	var ps []Position
	ps = solveBishops(3, []Position{})
	if len(ps) != 4 {
		t.Fatal(len(ps))
	}
	ps = solveBishops(3, []Position{Position{1, 1}})
	if len(ps) != 2 {
		t.Fatal(len(ps))
	}
}

func TestCombine(t *testing.T) {
	var pos2mark map[Position]string
	var l int
	var mark string
	pos2mark = combine([]Position{}, []Position{}, []Position{Position{1, 1}}, []Position{Position{1, 1}})
	l = len(pos2mark)
	if l != 1 {
		t.Fatal(l)
	}
	mark = pos2mark[Position{1, 1}]
	if mark != "o" {
		t.Fatal(mark)
	}
}

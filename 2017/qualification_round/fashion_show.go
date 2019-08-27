package main

import (
	"fmt"
	"reflect"
)

type Position struct {
	x int
	y int
}

func main() {
	var nTests int
	fmt.Scanf("%d\n", &nTests)
	for i := 0; i < nTests; i++ {
		var nLines, nPrePlaces int
		fmt.Scanf("%d %d\n", &nLines, &nPrePlaces)
		rooks, bishops := loadPrePlaces(nPrePlaces)
		score, addedMarks := solve(nLines, rooks, bishops)
		fmt.Printf("Case #%d: %d %d\n", i+1, score, len(addedMarks))
		for pos, mark := range addedMarks {
			fmt.Printf("%s %d %d\n", mark, pos.x+1, pos.y+1)
		}
	}
}

func solve(nLines int, rooks, bishops []Position) (int, map[Position]string) {
	addedRooks := solveRooks(nLines, rooks)
	addedBishops := solveBishops(nLines, bishops)
	score := len(rooks) + len(addedRooks) + len(bishops) + len(addedBishops)
	return score, combine(rooks, bishops, addedRooks, addedBishops)
}

func combine(rooks, bishops, addedRooks, addedBishops []Position) map[Position]string {
	addedMarks := map[Position]string{}

	for _, pos := range addedRooks {
		if contains(addedBishops, pos) || contains(bishops, pos) {
			addedMarks[pos] = "o"
		} else {
			addedMarks[pos] = "x"
		}
	}

	for _, pos := range addedBishops {
		if contains(addedRooks, pos) || contains(rooks, pos) {
			addedMarks[pos] = "o"
		} else {
			addedMarks[pos] = "+"
		}
	}

	return addedMarks
}

func contains(ps []Position, pos Position) bool {
	for _, p := range ps {
		if reflect.DeepEqual(pos, p) {
			return true
		}
	}
	return false
}

func solveRooks(nLines int, prePositions []Position) []Position {
	addedRooks := []Position{}

	vertLines := make([]bool, nLines)
	horiLines := make([]bool, nLines)
	for _, pos := range prePositions {
		vertLines[pos.x] = true
		horiLines[pos.y] = true
	}

	xs := []int{}
	ys := []int{}
	for i := 0; i < nLines; i++ {
		if !vertLines[i] {
			xs = append(xs, i)
		}
		if !horiLines[i] {
			ys = append(ys, i)
		}
	}

	for i := 0; i < len(xs); i++ {
		addedRooks = append(addedRooks, Position{xs[i], ys[i]})
	}

	return addedRooks
}

func solveBishops(nLines int, prePositions []Position) []Position {
	addedBishops := []Position{}
	for i := nLines; i >= 0; i-- {
		left := Position{0, i}
		fromLeft := solveBishopOnDiagonal(left, nLines, prePositions, addedBishops)
		if fromLeft.x != -1 {
			addedBishops = append(addedBishops, fromLeft)
		}
		if i != 0 {
			upper := Position{i, 0}
			fromUpper := solveBishopOnDiagonal(upper, nLines, prePositions, addedBishops)
			if fromUpper.x != -1 {
				addedBishops = append(addedBishops, fromUpper)
			}
		}
	}
	return addedBishops
}

func solveBishopOnDiagonal(start Position, nLines int, prePositions, addedBishops []Position) Position {
	sub := start.x - start.y
	for _, prePos := range prePositions {
		if sub == prePos.x-prePos.y {
			return Position{-1, -1}
		}
	}

	p := start
	for p.x >= 0 && p.x < nLines && p.y >= 0 && p.y < nLines {
		overlaped := false
		sum := p.x + p.y
		for _, prePos := range append(prePositions, addedBishops...) {
			if sum == prePos.x+prePos.y {
				overlaped = true
				break
			}
		}
		if !overlaped {
			return p
		}
		p.x += 1
		p.y += 1
	}
	return Position{-1, -1}
}

func loadPrePlaces(nPrePlaces int) ([]Position, []Position) {
	rooks := []Position{}
	bishops := []Position{}
	for i := 0; i < nPrePlaces; i++ {
		var mark string
		var row, col int
		fmt.Scanf("%s %d %d", &mark, &row, &col)
		pos := Position{row - 1, col - 1}
		switch mark {
		case "o":
			rooks = append(rooks, pos)
			bishops = append(bishops, pos)
		case "x":
			rooks = append(rooks, pos)
		case "+":
			bishops = append(bishops, pos)
		}
	}
	return rooks, bishops
}

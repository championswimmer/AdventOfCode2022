package main

import (
	cio "commons"
	"fmt"
	"strings"
)

func main() {
	lines := cio.ReadLines("day-03/input.txt")
	const ALPHABET = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	// PART 01

	prioritySum1 := 0

	for _, line := range lines {
		// split line into 2 parts at mid point
		first := line[:len(line)/2]
		second := line[len(line)/2:]

		// find elements that are present in both parts

		intersection := []rune{}
		for _, char := range first {
			if strings.ContainsRune(second, char) {
				intersection = append(intersection, char)
			}
		}
		priority := strings.IndexRune(ALPHABET, intersection[0])
		prioritySum1 += priority

	}

	// PART 02

	prioritySum2 := 0

	// group lines into groups of 3
	for i := 0; i < len(lines); i += 3 {
		first := lines[i]
		second := lines[i+1]
		third := lines[i+2]

		// find elements that are present in all 3 parts

		intersection := []rune{}
		for _, char := range first {
			if strings.ContainsRune(second, char) && strings.ContainsRune(third, char) {
				intersection = append(intersection, char)
			}
		}
		priority := strings.IndexRune(ALPHABET, intersection[0])
		prioritySum2 += priority
	}

	fmt.Println("Part 1:", prioritySum1)
	fmt.Println("Part 2:", prioritySum2)

}

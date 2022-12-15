package main

import (
	cio "commons"
	"fmt"
	"sort"
	"strconv"
)

func main() {
	lines := cio.ReadLines("day-01/input.txt")
	elfCalories := []int{}
	currCalories := 0

	for _, line := range lines {
		if line == "" {
			elfCalories = append(elfCalories, currCalories)
			currCalories = 0
		} else {
			num, _ := strconv.Atoi(line)
			currCalories += num
		}
	}
	// sort elfCalories in descending order
	sort.Sort(sort.Reverse(sort.IntSlice(elfCalories)))
	fmt.Println(elfCalories[0] + elfCalories[1] + elfCalories[2])
}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

// 1 4 3 4 -- must delte 4 (front)
// 1 4 7 11 -- must delete 11 (back)

func isSafe(numbers []int) bool {
	// Check if slice is empty or has only one number
	if len(numbers) <= 1 {
		return true
	}

	// Check first two numbers to determine if sequence should be increasing or decreasing
	isIncreasing := numbers[1] > numbers[0]

	// Check each pair of adjacent numbers
	for i := 0; i < len(numbers)-1; i++ {
		diff := numbers[i+1] - numbers[i]

		// Check if difference is between 1 and 3 (inclusive)
		if diff < -3 || diff > 3 || diff == 0 {
			return false
		}

		// Check if direction matches the initial direction
		if isIncreasing && diff < 0 {
			return false
		}
		if !isIncreasing && diff > 0 {
			return false
		}
	}

	return true
}

func isSafe2(numbers []int) bool {
	if isSafe(numbers) {
		return true
	}

	var wg sync.WaitGroup
	results := make(chan bool, 10)
	for i := 0; i < len(numbers); i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			removed := make([]int, len(numbers)-1)
			copy(removed, numbers[:i])
			copy(removed[i:], numbers[i+1:])
			results <- isSafe(removed)
		}(i)
	}
	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		if result {
			return true
		}
	}
	return false
}

func readInput() [][]int {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return [][]int{}
	}
	defer file.Close()

	var lines [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		strNumbers := strings.Fields(scanner.Text())
		numbers := make([]int, len(strNumbers))

		for i, str := range strNumbers {
			num, err := strconv.Atoi(str)
			if err != nil {
				fmt.Printf("Error converting string to integer: %v\n", err)
				continue
			}
			numbers[i] = num
		}
		lines = append(lines, numbers)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
	return lines
}

func main() {
	lines := readInput()

	var wg sync.WaitGroup
	results := make(chan bool, 1000)
	for _, numbers := range lines {
		wg.Add(1)
		go func(numbers []int) {
			defer wg.Done()
			results <- isSafe2(numbers)
		}(numbers)
	}
	go func() {
		wg.Wait()
		close(results)
	}()

	safeCount := 0
	for result := range results {
		if result {
			safeCount++
		}
	}

	fmt.Println("Part 2:", safeCount)
}

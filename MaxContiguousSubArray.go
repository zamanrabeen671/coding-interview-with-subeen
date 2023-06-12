package main

import (
	"fmt"
	"math"
)

func maxSubArray(A []int) int {
	maxSum := math.MinInt32
	currentSum := 0
	n := len(A)
	for i := 0; i < n; i++ {
		currentSum += A[i]
		if currentSum > maxSum {
			maxSum = currentSum
		}
		if currentSum < 0 {
			currentSum = 0
		}
	}
	return maxSum
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
	fmt.Println(maxSubArray([]int{-1, -2, 1, 2, 3, -5, 4, 5}))

}

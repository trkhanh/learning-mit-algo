package main

import "fmt"

func main() {
	fmt.Println(maxCoins([]int{3, 1, 5, 8}))
}
func maxCoins(nums []int) int {
	n := len(nums)

	p := make([]int, 0, n+2)
	p = append(append(append(p, 1), nums...), 1)

	dp := make([][]int, n+2)
	dp[n+1] = make([]int, n+2)

	for i := len(nums); i >= 0; i-- {
		dp[i] = make([]int, n+2)
		// fmt.Println("x", dp[i])
		for j := i + 1; j <= n+1; j++ {
			for k := i + 1; k < j; k++ {
				dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+p[i]*p[k]*p[j])
				fmt.Println("->", dp[i][j])

			}
		}
	}
	return dp[0][n+1]
}

func max(x, y int) int {
	fmt.Println("->", x, y)
	if x > y {
		return x
	}
	return y
}

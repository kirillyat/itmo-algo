package main

import "fmt"

func Bmain() {
	var n int
	fmt.Scan(&n)
	var s string
	fmt.Scan(&s)

	var dp []int
	ans := 0

	for i := n - 1; i >= 0; i-- {
		newDp := make([]int, n)

		for j := i; j < n; j++ {
			if i == j {
				newDp = append(newDp, 1)
			} else if s[i] == s[j] {
				if j-i == 1 {
					newDp = append(newDp, 2)
				} else {
					newDp = append(newDp, dp[j]-1+2)
				}
			} else {
				newDp = append(newDp, Max(dp[j], newDp[j]-1))
			}
			ans = Max(ans, newDp[j])
		}

		dp = newDp
	}

	fmt.Println(ans)
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

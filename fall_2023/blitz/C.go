package main

import (
	"fmt"
)

func main() {
	var n, m, x, y, r int
	fmt.Scanf("%d %d", &n, &m)
	fmt.Scanf("%d %d %d", &x, &y, &r)
	sx := Max(0, x-r)
	sy := Max(0, y-r)
	ex := Min(n-1, x+r)
	ey := Min(m-1, y+r)
	ans := 0

	for i := sx; i <= ex; i++ {
		for j := sy; j <= ey; j++ {

			if Dist(float64(i), float64(j), float64(x), float64(y)) <= float64(r*r) {
				ans++
			}
		}
	}

	fmt.Printf("%d", ans)
}

func Dist(a, b, x, y float64) float64 {
	return (a-x)*(a-x) + (b-y)*(b-y)
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

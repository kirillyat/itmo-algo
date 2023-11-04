package main

import (
	"fmt"
)

func main() {
	var n, t int
	d := make(map[int]bool)

	fmt.Scan(&n, &t)
	out, _ := intScanln(t)
	queue := make([]int, n)
	k := n - 1
	for i := len(out) - 1; i >= 0; i-- {
		_, ok := d[out[i]]
		if ok {
			continue
		}
		queue[k] = out[i]
		d[out[i]] = true
		k--
	}
	for i := n; i > 0; i-- {
		_, ok := d[i]
		if ok {
			continue
		}
		queue[k] = i
		k--
	}

	for i := 0; i < n; i++ {
		fmt.Printf("%d ", queue[i])
	}
}

func intScanln(n int) ([]int, error) {
	x := make([]int, n)
	for i := 0; i < n; i++ {
		_, err := fmt.Scan(&x[i])
		if err != nil {
			return nil, err
		}
	}
	return x, nil
}

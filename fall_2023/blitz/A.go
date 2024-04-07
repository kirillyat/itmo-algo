package main

import (
	"fmt"
)

func Amain() {
	var n, s int

	fmt.Scan(&n)
	fmt.Scan(&s)
	fmt.Println("YES")

	arr := make([]int, 0)

	if s == 0 {
		if n%2 == 1 {
			arr = append(arr, 0)
		}
		i := 1
		for len(arr) < n {
			arr = append(arr, i, -i)
			i++
		}
	} else {
		arr = append(arr, s)
		if n%2 == 0 {
			arr = append(arr, 0)
		}
		i := 1
		for len(arr) < n {
			if i == s || i == -s {
				i++
				continue
			}
			arr = append(arr, i, -i)
			i++
		}
	}

	for _, i := range arr {
		fmt.Printf("%d ", i)
	}

}

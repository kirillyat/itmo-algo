package main

import (
	"fmt"
	"strconv"
	"strings"
)

type StackItem struct {
	Operation string
	Value     int
}

func main() {
	var s []StackItem
	var input string
	fmt.Scanln(&input)
	n, _ := strconv.Atoi(input)

	for i := 0; i < n; i++ {
		fmt.Scanln(&input)
		parts := strings.Split(input, " ")
		cmd, _ := strconv.Atoi(parts[0])
		v, _ := strconv.Atoi(parts[1])

		switch cmd {
		case 1: //max
			for len(s) > 0 && s[len(s)-1].Operation == "min" && s[len(s)-1].Value <= v {
				s = s[:len(s)-1]
			}
			if len(s) == 0 || (s[len(s)-1].Operation == "max" && s[len(s)-1].Value < v) {
				s = append(s, StackItem{"max", v})
			}
		case 2: //min
			for len(s) > 0 && s[len(s)-1].Operation == "max" && s[len(s)-1].Value >= v {
				s = s[:len(s)-1]
			}
			if len(s) == 0 || (s[len(s)-1].Operation == "min" && s[len(s)-1].Value > v) {
				s = append(s, StackItem{"min", v})
			}
		case 3:
			fmt.Println(s[len(s)-1].Value)
		}
	}
}

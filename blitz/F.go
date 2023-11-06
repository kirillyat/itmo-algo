package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Stack []interface{}

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) Push(v interface{}) {
	*s = append(*s, v)
}

func (s *Stack) Pop() interface{} {
	if s.IsEmpty() {
		return nil
	}
	index := len(*s) - 1
	element := (*s)[index]
	*s = (*s)[:index]
	return element
}

func main() {
	var s Stack
	var cmd, v int
	var a bool

	for {
		input := ""
		fmt.Print("Enter command and value: ")
		fmt.Scanln(&input)

		if input == "q" {
			break
		}

		parts := strings.Split(input, " ")
		cmd, _ = strconv.Atoi(parts[0])
		v, _ = strconv.Atoi(parts[1])

		s.Push(((func(x, y int) int { return x }), 0))
		a = true

		if cmd == 1 {
			for !s.IsEmpty() {
				f, _ := s[len(s)-1].(func(int, int) int)
				if f == nil {
					break
				}
				if f(v, 0) <= v {
					s.Pop()
				} else if f == min {
					s = nil
					s.Push((func(x, y int) int { return y }, v))
					a = false
					break
				} else if f == max && f(v, 0) >= v {
					a = false
					break
				}
				break
			}
			if a {
				s.Push(max)
			}
		} else if cmd == 2 {
			for !s.IsEmpty() {
				f, _ := s[len(s)-1].(func(int, int) int)
				if f == nil {
					break
				}
				if f == max && f(v, 0) <= v {
					break
				} else if f == min && f(v, 0) <= v {
					a = false
					break
				} else if f == min && f(v, 0) > v {
					s.Pop()
				} else if f == max && f(v, 0) >= v {
					s = nil
					s.Push((func(x, y int) int { return y }, v))
					a = false
					break
				}
				break
			}
			if a {
				s.Push(min)
			}
		} else if cmd == 3 {
			for _, f := range s {
				v = f.(func(int, int) int)(v, 0)
			}
			fmt.Println(v)
		}
	}
}

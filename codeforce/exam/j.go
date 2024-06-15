package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func mains() {
	// Ввод данных
	reader := bufio.NewReader(os.Stdin)
	s, _ := reader.ReadString('\n')
	t, _ := reader.ReadString('\n')

	s = strings.TrimSpace(s)
	t = strings.TrimSpace(t)

	hashPos := len(s)
	s = s + "#" + t + "$"
	n := len(s)

	p := make([]int, 0)
	c := make([]int, n)

	// Начальная сортировка по первому символу
	alpha := "$abcdefghijklmnopqrstuvwxyz#"
	a := make([][]int, 28)

	for i := 0; i < n; i++ {
		pos := strings.Index(alpha, string(s[i]))
		a[pos] = append(a[pos], i)
	}

	for i := 0; i < 28; i++ {
		for j := 0; j < len(a[i]); j++ {
			p = append(p, a[i][j])
			if i+j == 0 {
				c[p[0]] = 0
			} else {
				c[p[len(p)-1]] = c[p[len(p)-2]] + toInt(j == 0)
			}
		}
	}

	// Сортировка по первым 2^k символам
	k := 0
	for (1 << k) < n {
		b := make([][][]int, n)
		for j := 0; j < n; j++ {
			i := (p[j] - (1 << k) + n) % n
			b[c[i]] = append(b[c[i]], []int{c[p[j]], i})
		}

		p = make([]int, 0)
		for i := 0; i < n; i++ {
			for j := 0; j < len(b[i]); j++ {
				p = append(p, b[i][j][1])
				if i+j == 0 {
					c[p[0]] = 0
				} else {
					c[p[len(p)-1]] = c[p[len(p)-2]] + toInt(j == 0 || b[i][j][0] != b[i][j-1][0])
				}
			}
		}
		k++
	}

	// Подсчет LCP массива
	lcp := make([]int, n)
	k = 0
	for i := 0; i < n-1; i++ {
		pos := c[i]
		j := p[pos-1]
		for s[i+k] == s[j+k] {
			k++
		}
		lcp[pos] = k
		if k > 0 {
			k--
		}
	}

	// Поиск наибольшей общей подстроки
	res := 0
	sRes := ""
	fc := make([]bool, n)
	for i := 0; i < n; i++ {
		fc[i] = p[i] < hashPos
	}

	for i := 2; i < n; i++ {
		if fc[i] != fc[i-1] {
			if res < lcp[i] {
				res = lcp[i]
				sRes = s[p[i] : p[i]+lcp[i]]
			}
		}
	}

	fmt.Println(sRes)
}

func toInt(b bool) int {
	if b {
		return 1
	}
	return 0
}

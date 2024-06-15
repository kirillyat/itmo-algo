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

	// Удаляем невидимые символы и символы новой строки
	s = strings.TrimSpace(s)
	t = strings.TrimSpace(t)

	// Создаем множество уникальных комбинаций
	combSet := make(map[string]struct{})

	// Первый цикл для строк s и t
	for i := 1; i <= len(s); i++ {
		for j := 1; j <= len(t); j++ {
			comb1 := s[:i] + t[:j]
			combSet[comb1] = struct{}{}

			comb2 := t[:j] + s[:i]
			combSet[comb2] = struct{}{}
		}
	}

	// Количество уникальных комбинаций
	fmt.Println(len(combSet))
}

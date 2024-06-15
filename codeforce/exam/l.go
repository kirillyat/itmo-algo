package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Edge struct {
	from int
	to   int
	flow int
}

type Graph struct {
	vNum    int
	height  int
	width   int
	checked []bool
	edge    [][]Edge
}

var maxFlow = 0
var startSum = 0
var targetSum = 0

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	var height, width int
	fmt.Sscanf(input, "%d %d", &height, &width)

	G := NewGraph(height, width)
	G.Init(height, width)

	for tryPushFlow(G, 0, 5) > 0 {
		G.UncheckAll()
	}

	if maxFlow == startSum && maxFlow == targetSum && maxFlow != 0 {
		fmt.Println("Valid")
	} else {
		fmt.Println("Invalid")
	}
}

func NewGraph(height, width int) *Graph {
	G := &Graph{
		height:  height,
		width:   width,
		vNum:    height*width + 2,
		checked: make([]bool, height*width+2),
		edge:    make([][]Edge, height*width+2),
	}
	return G
}

func (G *Graph) AddEdge(from, to, flow int) {
	G.edge[from] = append(G.edge[from], Edge{from, to, flow})
}

func (G *Graph) UncheckAll() {
	for i := range G.checked {
		G.checked[i] = false
	}
}

func (G *Graph) ToVertNum(i, j int) int {
	return i*G.width + j + 1
}

func (G *Graph) Init(height, width int) {
	reader := bufio.NewReader(os.Stdin)
	for i := 0; i < height; i++ {
		for j := 0; j < width; j++ {
			atom, _ := reader.ReadString(' ')
			atom = strings.TrimSpace(atom)
			val := valence(atom[0])
			if (i%2+j%2)%2 == 0 {
				G.AddEdge(0, G.ToVertNum(i, j), val)
				startSum += val
				if i+1 < height {
					G.AddEdge(G.ToVertNum(i, j), G.ToVertNum(i+1, j), 1)
				}
				if j+1 < width {
					G.AddEdge(G.ToVertNum(i, j), G.ToVertNum(i, j+1), 1)
				}
				if i-1 >= 0 {
					G.AddEdge(G.ToVertNum(i, j), G.ToVertNum(i-1, j), 1)
				}
				if j-1 >= 0 {
					G.AddEdge(G.ToVertNum(i, j), G.ToVertNum(i, j-1), 1)
				}
			} else {
				G.AddEdge(G.ToVertNum(i, j), G.vNum-1, val)
				targetSum += val
			}
		}
	}
}

func valence(atom byte) int {
	switch atom {
	case 'H':
		return 1
	case 'O':
		return 2
	case 'N':
		return 3
	case 'C':
		return 4
	}
	return 0
}

func findBackEdge(G *Graph, edge Edge) int {
	for idx, e := range G.edge[edge.to] {
		if e.to == edge.from {
			return idx
		}
	}
	return -1
}

func tryPushFlow(G *Graph, current, capacity int) int {
	G.checked[current] = true
	if current == G.vNum-1 {
		maxFlow += capacity
		return capacity
	}
	for i := range G.edge[current] {
		edge := G.edge[current][i]
		if G.checked[edge.to] || edge.flow == 0 {
			continue
		}
		minCapacity := tryPushFlow(G, edge.to, min(edge.flow, capacity))
		if minCapacity > 0 {
			G.edge[current][i].flow -= minCapacity
			backEdgeNum := findBackEdge(G, edge)
			if backEdgeNum != -1 {
				G.edge[edge.to][backEdgeNum].flow += minCapacity
			} else {
				G.edge[edge.to] = append(G.edge[edge.to], Edge{edge.to, edge.from, minCapacity})
			}
			return minCapacity
		}
	}
	return 0
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

package main

import (
	"fmt"
)

type SegmentTree struct {
	segmentTree []Node
	size        int
}

type Node struct {
	sum  int64
	add  int64
	set  *int64
	size int
}

func NewSegmentTree(size int) *SegmentTree {
	st := &SegmentTree{}
	st.size = 1
	for st.size < size {
		st.size *= 2
	}
	st.segmentTree = make([]Node, 2*st.size-1)
	st.build(0, st.size, 0)
	return st
}

func (st *SegmentTree) Set(l, r int, x int) {
	st.set(l, r, int64(x), 0, st.size, 0)
}

func (st *SegmentTree) Sum(l, r int) int64 {
	return st.sum(l, r, 0, st.size, 0)
}

func (st *SegmentTree) Add(l, r int, x int) {
	st.add(l, r, int64(x), 0, st.size, 0)
}

func (st *SegmentTree) add(l, r int, x int64, lx, rx, v int) {
	if r <= lx || rx <= l {
		return
	}

	if l <= lx && rx <= r {
		if rx-lx != 1 {
			st.push(v)
		}
		st.segmentTree[v].add += x
		return
	}

	st.push(v)

	m := (lx + rx) / 2
	st.add(l, r, x, lx, m, 2*v+1)
	st.add(l, r, x, m, rx, 2*v+2)

	st.segmentTree[v].sum = st.segmentTree[2*v+1].sum + st.segmentTree[2*v+2].sum +
		st.segmentTree[2*v+1].add*int64(st.segmentTree[2*v+1].size) +
		st.segmentTree[2*v+2].add*int64(st.segmentTree[2*v+2].size)
	st.segmentTree[v].add = 0
}

func (st *SegmentTree) sum(l, r, lx, rx, v int) int64 {
	if r <= lx || rx <= l {
		return 0
	}

	if l <= lx && rx <= r {
		if rx-lx != 1 {
			st.push(v)
		}
		return st.segmentTree[v].sum + st.segmentTree[v].add*int64(st.segmentTree[v].size)
	}

	st.push(v)

	m := (lx + rx) / 2
	return st.sum(l, r, lx, m, 2*v+1) + st.sum(l, r, m, rx, 2*v+2)
}

func (st *SegmentTree) set(l, r int, x int64, lx, rx, v int) {
	if r <= lx || rx <= l {
		return
	}

	if l <= lx && rx <= r {
		st.segmentTree[v].set = &x
		st.segmentTree[v].sum = int64(st.segmentTree[v].size) * x
		st.segmentTree[v].add = 0
		return
	}

	st.push(v)

	m := (lx + rx) / 2
	st.set(l, r, x, lx, m, 2*v+1)
	st.set(l, r, x, m, rx, 2*v+2)

	st.segmentTree[v].sum = st.segmentTree[2*v+1].sum + st.segmentTree[2*v+2].sum +
		st.segmentTree[2*v+1].add*int64(st.segmentTree[2*v+1].size) +
		st.segmentTree[2*v+2].add*int64(st.segmentTree[2*v+2].size)
	st.segmentTree[v].add = 0
}

func (st *SegmentTree) push(v int) {
	if st.segmentTree[v].set != nil {
		st.segmentTree[2*v+1].set = st.segmentTree[v].set
		st.segmentTree[2*v+2].set = st.segmentTree[v].set
		st.segmentTree[2*v+1].add = 0
		st.segmentTree[2*v+2].add = 0
		st.segmentTree[v].sum = *st.segmentTree[v].set * int64(st.segmentTree[v].size)
		st.segmentTree[2*v+1].sum = *st.segmentTree[v].set * int64(st.segmentTree[2*v+1].size)
		st.segmentTree[2*v+2].sum = *st.segmentTree[v].set * int64(st.segmentTree[2*v+2].size)
		st.segmentTree[v].set = nil
	}
	if st.segmentTree[v].add != 0 {
		st.segmentTree[v].sum += st.segmentTree[v].add * int64(st.segmentTree[v].size)
		st.segmentTree[2*v+1].add += st.segmentTree[v].add
		st.segmentTree[2*v+2].add += st.segmentTree[v].add
		st.segmentTree[v].add = 0
	}
}

func (st *SegmentTree) build(lx, rx, v int) {
	if rx-lx == 1 {
		st.segmentTree[v] = Node{0, 0, nil, 1}
	} else {
		m := (lx + rx) / 2
		st.build(lx, m, 2*v+1)
		st.build(m, rx, 2*v+2)
		st.segmentTree[v] = Node{0, 0, nil, rx - lx}
	}
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	st := NewSegmentTree(n)
	var answer []int64

	for i := 0; i < m; i++ {
		var command string
		fmt.Scan(&command)
		if command == "1" {
			var l, r, x int
			fmt.Scan(&l, &r, &x)
			st.Set(l, r, x)
		} else if command == "2" {
			var l, r, x int
			fmt.Scan(&l, &r, &x)
			st.Add(l, r, x)
		} else {
			var l, r int
			fmt.Scan(&l, &r)
			answer = append(answer, st.Sum(l, r))
		}
	}

	for _, item := range answer {
		fmt.Println(item)
	}
}

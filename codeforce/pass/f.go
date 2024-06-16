package main

import (
	"fmt"
	"math/rand"
)

type Node struct {
	size  int
	p     int
	data  int
	zero  bool
	left  *Node
	right *Node
}

func newNode(data int, isZero bool) *Node {
	return &Node{
		data:  data,
		zero:  isZero,
		p:     rand.Int(),
		size:  1,
		left:  nil,
		right: nil,
	}
}

type Treap struct {
	root *Node
	num  int
}

func (t *Treap) get_size(n *Node) int {
	if n == nil {
		return 0
	}
	return n.size
}

func (t *Treap) get_zero(n *Node) bool {
	if n == nil {
		return false
	}
	return n.zero
}

func (t *Treap) update_size(n *Node) {
	if n == nil {
		return
	}
	n.size = t.get_size(n.left) + t.get_size(n.right) + 1
}

func (t *Treap) update_zero(n *Node) {
	if n == nil {
		return
	}
	n.zero = t.get_zero(n.left) || t.get_zero(n.right) || (n.data == 0)
}

func (t *Treap) get_data(n *Node) int {
	if n == nil {
		return -1
	}
	return n.data
}

func (t *Treap) merge(l *Node, r *Node) *Node {
	if l == nil {
		return r
	}
	if r == nil {
		return l
	}

	if l.p > r.p {
		l.right = t.merge(l.right, r)
		t.update_size(l)
		t.update_zero(l)
		return l
	} else {
		r.left = t.merge(l, r.left)
		t.update_size(r)
		t.update_zero(r)
		return r
	}
}

func (t *Treap) split(n *Node, key int) (*Node, *Node) {
	if n == nil {
		return nil, nil
	}

	var l, r *Node
	if t.get_size(n.left) < key {
		l, n.right = t.split(n.right, key-t.get_size(n.left)-1)
		r = n
	} else {
		n.left, r = t.split(n.left, key)
		l = n
	}
	t.update_size(n)
	t.update_zero(n)
	return l, r
}

func (t *Treap) search_null(n *Node) (*Node, int) {
	if n == nil {
		return nil, 0
	}
	cur := n
	ind := t.get_size(cur.left)

	for t.get_zero(cur) {
		if cur.left != nil && t.get_zero(cur.left) {
			cur = cur.left
			ind -= t.get_size(cur.right) + 1
		} else if t.get_data(cur) == 0 {
			break
		} else {
			cur = cur.right
			ind += t.get_size(cur.left) + 1
		}
		if cur == nil {
			break
		}
	}

	return cur, ind
}

func (t *Treap) to_vector(node *Node, a *[]int) {
	if node != nil {
		t.to_vector(node.left, a)
		*a = append(*a, t.get_data(node))
		t.to_vector(node.right, a)
	}
}

func (t *Treap) remove(n *Node, key int) *Node {
	var t1, t2, t3 *Node
	t1, t2 = t.split(n, key)
	t2, t3 = t.split(t2, 1)
	n = t.merge(t1, t3)
	return n
}

func (t *Treap) build(n int) {
	for i := 0; i < n; i++ {
		t.root = t.merge(newNode(0, true), t.root)
	}
}

func (t *Treap) insert(ind int) {
	var l, r *Node
	l, r = t.split(t.root, ind)
	z, i := t.search_null(r)
	if z != nil && z.data == 0 {
		r = t.remove(r, i)
	}

	t.root = t.merge(t.merge(l, newNode(t.num+1, false)), r)
	t.num++
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	tree := Treap{root: nil, num: 0}
	tree.build(m)

	var tmp int
	for i := 0; i < n; i++ {
		fmt.Scan(&tmp)
		tree.insert(tmp - 1)
	}

	var ans []int
	tree.to_vector(tree.root, &ans)
	for len(ans) > 0 && ans[len(ans)-1] == 0 {
		ans = ans[:len(ans)-1]
	}

	fmt.Println(len(ans))
	for _, v := range ans {
		fmt.Printf("%d ", v)
	}
}

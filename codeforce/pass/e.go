package main

import (
	"fmt"
	"math"
)

type node struct {
	key         int64
	sum         int64
	min, max    int64
	height      int64
	left, right *node
}

func newNode(k int64) *node {
	return &node{
		key:    k,
		min:    k,
		max:    k,
		sum:    k,
		height: 1,
	}
}

func (n *node) getHeightLeft() int64 {
	if n.left == nil {
		return 0
	}
	return n.left.height
}

func (n *node) getHeightRight() int64 {
	if n.right == nil {
		return 0
	}
	return n.right.height
}

func (n *node) getBalance() int64 {
	return n.getHeightRight() - n.getHeightLeft()
}

func (n *node) getSumLeft() int64 {
	if n.left != nil {
		return n.left.sum
	}
	return 0
}

func (n *node) getSumRight() int64 {
	if n.right != nil {
		return n.right.sum
	}
	return 0
}

func (n *node) getMinLeft() int64 {
	if n.left != nil {
		return n.left.min
	}
	return math.MaxInt64
}

func (n *node) getMinRight() int64 {
	if n.right != nil {
		return n.right.min
	}
	return math.MaxInt64
}

func (n *node) getMaxLeft() int64 {
	if n.left != nil {
		return n.left.max
	}
	return math.MinInt64
}

func (n *node) getMaxRight() int64 {
	if n.right != nil {
		return n.right.max
	}
	return math.MinInt64
}

func (n *node) recalcMinMax() {
	n.min = min(min(n.getMinLeft(), n.getMinRight()), n.key)
	n.max = max(max(n.getMaxLeft(), n.getMaxRight()), n.key)
}

func (n *node) recalcSum() {
	n.sum = n.getSumLeft() + n.getSumRight() + n.key
}

func (n *node) recalc() {
	n.height = 1 + max(n.getHeightLeft(), n.getHeightRight())
	n.recalcMinMax()
	n.recalcSum()
}

func find(curNode *node, val int64) *node {
	if curNode == nil || curNode.key == val {
		return curNode
	}
	if curNode.key < val {
		return find(curNode.right, val)
	}
	return find(curNode.left, val)
}

func exists(curNode *node, val int64) bool {
	return find(curNode, val) != nil
}

func rightRotate(curNode *node) *node {
	left := curNode.left
	curNode.left = left.right
	left.right = curNode

	curNode.recalc()
	left.recalc()

	return left
}

func leftRotate(curNode *node) *node {
	right := curNode.right
	curNode.right = right.left
	right.left = curNode

	curNode.recalc()
	right.recalc()

	return right
}

func rebalance(curNode *node) *node {
	if curNode.getBalance() == 2 {
		if curNode.right.getBalance() < 0 {
			curNode.right = rightRotate(curNode.right)
		}
		return leftRotate(curNode)
	}
	if curNode.getBalance() == -2 {
		if curNode.left.getBalance() > 0 {
			curNode.left = leftRotate(curNode.left)
		}
		return rightRotate(curNode)
	}
	return curNode
}

func insert(curNode *node, newKey int64) *node {
	if curNode == nil {
		return newNode(newKey)
	}
	if newKey < curNode.key {
		curNode.left = insert(curNode.left, newKey)
	} else {
		curNode.right = insert(curNode.right, newKey)
	}
	curNode.recalc()
	return rebalance(curNode)
}

func insertNode(curNode *node, newKey int64) *node {
	if exists(curNode, newKey) {
		return curNode
	}
	return insert(curNode, newKey)
}

func sum(curNode *node, l, r int64) int64 {
	if curNode == nil {
		return 0
	}
	if curNode.key > r {
		return sum(curNode.left, l, r)
	}
	if curNode.key < l {
		return sum(curNode.right, l, r)
	}
	if curNode.left == nil && curNode.right == nil {
		return curNode.key
	}
	if curNode.min >= l && curNode.max <= r {
		return curNode.sum
	}
	return sum(curNode.left, l, r) + sum(curNode.right, l, r) + curNode.key
}

const TEN int64 = 1000000000

func main() {
	var root *node
	var prev = '+'
	var res int64 = 0
	var n int64
	fmt.Scan(&n)

	for i := int64(0); i < n; i++ {
		var c string
		fmt.Scan(&c)

		if c == "+" {
			var x int64
			fmt.Scan(&x)

			if prev == '?' {
				root = insertNode(root, (x+res)%TEN)
			} else {
				root = insertNode(root, x)
			}
		} else {
			var l, r int64
			fmt.Scan(&l, &r)

			res = sum(root, l, r)
			fmt.Println(res)
		}
		prev = rune(c[0])
	}
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

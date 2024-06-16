package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

// TreeNode represents a node in the Treap
type TreeNode struct {
	key, priority int
	left, right   *TreeNode
}

// CreateNode initializes a new TreeNode with given key
func CreateNode(key int) *TreeNode {
	rand.Seed(time.Now().UnixNano())
	return &TreeNode{key: key, priority: rand.Int() * rand.Int()}
}

// Split divides the tree into two subtrees by the given key
func Split(root *TreeNode, key int) (*TreeNode, *TreeNode) {
	if root == nil {
		return nil, nil
	}

	if root.key < key {
		rightSubtree, right := Split(root.right, key)
		root.right = rightSubtree
		return root, right
	} else {
		left, leftSubtree := Split(root.left, key)
		root.left = leftSubtree
		return left, root
	}
}

// Insert adds a new node to the Treap
func Insert(root **TreeNode, node *TreeNode) {
	if *root == nil {
		*root = node
		return
	}

	if (*root).priority > node.priority {
		if node.key < (*root).key {
			Insert(&((*root).left), node)
		} else {
			Insert(&((*root).right), node)
		}
		return
	}

	leftSubtree, rightSubtree := Split(*root, node.key)
	node.left = leftSubtree
	node.right = rightSubtree
	*root = node
}

// Merge combines two subtrees into one
func Merge(left, right *TreeNode) *TreeNode {
	if left == nil || right == nil {
		if right == nil {
			return left
		}
		return right
	}

	if left.priority > right.priority {
		left.right = Merge(left.right, right)
		return left
	} else {
		right.left = Merge(left, right.left)
		return right
	}
}

// Remove deletes a node from the Treap
func Remove(root **TreeNode, key int) {
	if *root == nil {
		return
	}

	if key < (*root).key {
		Remove(&((*root).left), key)
	} else if key > (*root).key {
		Remove(&((*root).right), key)
	} else {
		*root = Merge((*root).left, (*root).right)
	}
}

// Exists checks if a node with given key exists in the Treap
func Exists(root *TreeNode, key int) bool {
	if root == nil {
		return false
	}

	if key == root.key {
		return true
	} else if key < root.key {
		return Exists(root.left, key)
	} else {
		return Exists(root.right, key)
	}
}

// FindPrevious finds the largest node less than the given key
func FindPrevious(root *TreeNode, key int) *TreeNode {
	cur := root
	var predecessor *TreeNode

	for cur != nil {
		if cur.key < key {
			predecessor = cur
			cur = cur.right
		} else {
			cur = cur.left
		}
	}

	return predecessor
}

// FindNext finds the smallest node greater than the given key
func FindNext(root *TreeNode, key int) *TreeNode {
	cur := root
	var successor *TreeNode

	for cur != nil {
		if cur.key > key {
			successor = cur
			cur = cur.left
		} else {
			cur = cur.right
		}
	}

	return successor
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)
	var root *TreeNode

	for scanner.Scan() {
		input := scanner.Text()
		parts := strings.Fields(input)
		if len(parts) < 2 {
			continue
		}
		command := parts[0]
		key := atoi(parts[1])

		switch command {
		case "insert":
			node := CreateNode(key)
			if !Exists(root, key) {
				Insert(&root, node)
			}
		case "exists":
			if Exists(root, key) {
				fmt.Println("true")
			} else {
				fmt.Println("false")
			}
		case "delete":
			if Exists(root, key) {
				Remove(&root, key)
			}
		case "next":
			node := FindNext(root, key)
			if node == nil {
				fmt.Println("none")
			} else {
				fmt.Println(node.key)
			}
		case "prev":
			node := FindPrevious(root, key)
			if node == nil {
				fmt.Println("none")
			} else {
				fmt.Println(node.key)
			}
		}
	}
}

// atoi converts a string to an integer
func atoi(s string) int {
	n := 0
	for i := 0; i < len(s); i++ {
		n = n*10 + int(s[i]-'0')
	}
	return n
}

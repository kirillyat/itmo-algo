def print_tree(tree, offset=0):
    for k in sorted(tree.keys()):
        print(' '*offset, k, sep='')
        print_tree(tree[k], offset+2)
    
def main():
    tree = dict()
    n = int(input())
    for _ in range(n):
        path = input().split('/')
        d = tree
        for dir in path:
            d[dir]=d.get(dir, {})
            d = d[dir]
    print_tree(tree)

main()
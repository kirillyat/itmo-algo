#include <iostream>
#include <vector>
#include <cstdlib>

struct Node {
    int size;
    int priority;
    int data;
    bool zero;
    Node* left;
    Node* right;

    Node(int data = 0, bool isZero = true) : data(data), zero(isZero), size(1), left(nullptr), right(nullptr) {
        priority = rand() * rand();
    }
};

class Treap {
private:
    Node* root = nullptr;
    int num = 0;

    int getSize(Node* t) {
        return t ? t->size : 0;
    }

    bool getZero(Node* t) {
        return t ? t->zero : false;
    }

    void updateSize(Node* t) {
        if (t) {
            t->size = getSize(t->left) + getSize(t->right) + 1;
        }
    }

    void updateZero(Node* t) {
        if (t) {
            t->zero = getZero(t->left) || getZero(t->right) || (t->data == 0);
        }
    }

    Node* merge(Node* l, Node* r) {
        if (!l || !r) {
            return l ? l : r;
        }
        if (l->priority > r->priority) {
            l->right = merge(l->right, r);
            updateSize(l);
            updateZero(l);
            return l;
        } else {
            r->left = merge(l, r->left);
            updateSize(r);
            updateZero(r);
            return r;
        }
    }

    void split(Node* t, int key, Node*& l, Node*& r) {
        if (!t) {
            l = r = nullptr;
            return;
        }
        if (getSize(t->left) < key) {
            split(t->right, key - getSize(t->left) - 1, t->right, r);
            l = t;
        } else {
            split(t->left, key, l, t->left);
            r = t;
        }
        updateSize(t);
        updateZero(t);
    }

    Node* searchNull(Node* t, int& ind) {
        Node* cur = t;
        ind = getSize(cur->left);

        while (getZero(cur)) {
            if (cur->left && getZero(cur->left)) {
                cur = cur->left;
                ind -= getSize(cur->right) + 1;
            } else if (getData(cur) == 0) {
                break;
            } else {
                cur = cur->right;
                ind += getSize(cur->left) + 1;
            }
        }

        return cur;
    }

    int getData(Node* t) {
        return t ? t->data : -1;
    }

    void toArray(Node* node, std::vector<int>& a) {
        if (node) {
            toArray(node->left, a);
            a.push_back(getData(node));
            toArray(node->right, a);
        }
    }

    Node* remove(Node* r, int key) {
        Node *t1, *t2, *t3;
        split(r, key, t1, t2);
        split(t2, 1, t2, t3);
        r = merge(t1, t3);
        delete t2;
        return r;
    }

public:
    void build(int n) {
        for (int i = 0; i < n; ++i) {
            root = merge(new Node, root);
        }
    }

    void insert(int ind) {
        Node* l, * r, * z;
        int i;

        split(root, ind, l, r);
        z = searchNull(r, i);
        if (z && z->data == 0) {
            r = remove(r, i);
        }

        root = merge(merge(l, new Node(++num, false)), r);
    }

    void printNonZeroElements() {
        std::vector<int> ans;
        toArray(root, ans);
        while (!ans.empty() && ans.back() == 0) {
            ans.pop_back();
        }

        std::cout << ans.size() << '\n';
        for (int i = 0; i < ans.size(); ++i) {
            std::cout << ans[i] << ' ';
        }
        std::cout << '\n';
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    std::cin >> n >> m;

    Treap tree;
    tree.build(m);

    for (int i = 0; i < n; ++i) {
        int j;
        std::cin >> j;
        tree.insert(j - 1);
    }

    tree.printNonZeroElements();

    return 0;
}

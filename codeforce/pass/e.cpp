#include <iostream>
#include <climits>
#include <algorithm> // for std::min and std::max

struct Node {
    long long key;
    long long sum;
    long long min, max;
    long long height;
    Node* left;
    Node* right;

    Node(long long k) : key(k), min(k), max(k), sum(k), height(1), left(nullptr), right(nullptr) {}

    long long getHeight(Node* node) {
        return node ? node->height : 0;
    }

    long long getSum(Node* node) {
        return node ? node->sum : 0;
    }

    long long getMin(Node* node) {
        return node ? node->min : LLONG_MAX;
    }

    long long getMax(Node* node) {
        return node ? node->max : LLONG_MIN;
    }

    void updateMinMax() {
        min = std::min(key, std::min(getMin(left), getMin(right)));
        max = std::max(key, std::max(getMax(left), getMax(right)));
    }

    void updateSum() {
        sum = key + getSum(left) + getSum(right);
    }

    void updateHeight() {
        height = 1 + std::max(getHeight(left), getHeight(right));
    }

    long long getBalance() {
        return getHeight(right) - getHeight(left);
    }
};

Node* find(Node* cur_node, long long val) {
    if (cur_node == nullptr || cur_node->key == val) {
        return cur_node;
    }

    if (cur_node->key < val) {
        return find(cur_node->right, val);
    } else {
        return find(cur_node->left, val);
    }
}

bool exists(Node* cur_node, long long val) {
    return find(cur_node, val) != nullptr;
}

Node* rightRotate(Node* cur_node) {
    Node* left = cur_node->left;
    cur_node->left = left->right;
    left->right = cur_node;
    cur_node->updateHeight();
    cur_node->updateSum();
    cur_node->updateMinMax();
    left->updateHeight();
    left->updateSum();
    left->updateMinMax();
    return left;
}

Node* leftRotate(Node* cur_node) {
    Node* right = cur_node->right;
    cur_node->right = right->left;
    right->left = cur_node;
    cur_node->updateHeight();
    cur_node->updateSum();
    cur_node->updateMinMax();
    right->updateHeight();
    right->updateSum();
    right->updateMinMax();
    return right;
}

Node* rebalance(Node* cur_node) {
    if (cur_node->getBalance() == 2) {
        if (cur_node->right->getBalance() < 0) {
            cur_node->right = rightRotate(cur_node->right);
        }
        return leftRotate(cur_node);
    }
    if (cur_node->getBalance() == -2) {
        if (cur_node->left->getBalance() > 0) {
            cur_node->left = leftRotate(cur_node->left);
        }
        return rightRotate(cur_node);
    }
    return cur_node;
}

Node* insert(Node* cur_node, long long new_key) {
    if (cur_node == nullptr) {
        return new Node(new_key);
    }

    if (new_key < cur_node->key) {
        cur_node->left = insert(cur_node->left, new_key);
    } else {
        cur_node->right = insert(cur_node->right, new_key);
    }
    cur_node->updateHeight();
    cur_node->updateSum();
    cur_node->updateMinMax();

    return rebalance(cur_node);
}

Node* insertNode(Node* cur_node, long long new_key) {
    if (exists(cur_node, new_key)) {
        return cur_node;
    }
    return insert(cur_node, new_key);
}

long long sum(Node* cur_node, long long l, long long r) {
    if (cur_node == nullptr) {
        return 0;
    }

    if (cur_node->key > r) {
        return sum(cur_node->left, l, r);
    }

    if (cur_node->key < l) {
        return sum(cur_node->right, l, r);
    }

    if (cur_node->left == nullptr && cur_node->right == nullptr) {
        return cur_node->key;
    }

    if (cur_node->min >= l && cur_node->max <= r) {
        return cur_node->sum;
    }
    return sum(cur_node->left, l, r) + sum(cur_node->right, l, r) + cur_node->key;
}

const long long TEN = 1000000000;

int main() {
    Node* root = nullptr;
    char prev = '+';
    long long res = 0;
    long long n;
    std::cin >> n;

    for (long long i = 0; i < n; i++) {
        char c;
        std::cin >> c;

        if (c == '+') {
            long long x;
            std::cin >> x;

            if (prev == '?') {
                root = insertNode(root, (x + res) % TEN);
            } else {
                root = insertNode(root, x);
            }
        } else {
            long long l, r;
            std::cin >> l >> r;

            res = sum(root, l, r);
            std::cout << res << '\n';
        }
        prev = c;
    }

    return 0;
}

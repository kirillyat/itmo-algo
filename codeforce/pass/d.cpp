#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

struct Node {
    long long key;
    int priority;
    Node* left;
    Node* right;

    Node(long long k) : key(k), priority(rand() * rand()), left(nullptr), right(nullptr) {}
};

void split(Node* t, Node*& l, Node*& r, long long key) {
    if (!t) {
        l = nullptr;
        r = nullptr;
    } else if (key < t->key) {
        split(t->left, l, t->left, key);
        r = t;
    } else {
        split(t->right, t->right, r, key);
        l = t;
    }
}

void merge(Node*& t, Node* l, Node* r) {
    if (!l || !r) {
        t = l ? l : r;
    } else if (l->priority > r->priority) {
        merge(l->right, l->right, r);
        t = l;
    } else {
        merge(r->left, l, r->left);
        t = r;
    }
}

void insert(Node*& t, Node* v) {
    if (!t) {
        t = v;
    } else if (v->priority > t->priority) {
        split(t, v->left, v->right, v->key);
        t = v;
    } else {
        insert(v->key < t->key ? t->left : t->right, v);
    }
}

void remove(Node*& t, long long key) {
    if (!t) return;
    if (key == t->key) {
        Node* temp = t;
        merge(t, t->left, t->right);
        delete temp;
    } else {
        remove(key < t->key ? t->left : t->right, key);
    }
}

bool exists(Node* t, long long key) {
    while (t) {
        if (key == t->key) return true;
        t = key < t->key ? t->left : t->right;
    }
    return false;
}

Node* prev(Node* t, long long key) {
    Node* result = nullptr;
    while (t) {
        if (key > t->key) {
            result = t;
            t = t->right;
        } else {
            t = t->left;
        }
    }
    return result;
}

Node* next(Node* t, long long key) {
    Node* result = nullptr;
    while (t) {
        if (key < t->key) {
            result = t;
            t = t->left;
        } else {
            t = t->right;
        }
    }
    return result;
}

int main() {
    Node* root = nullptr;
    string command;
    long long key;
    
    while (cin >> command >> key) {
        if (command == "insert") {
            if (!exists(root, key)) {
                Node* newNode = new Node(key);
                insert(root, newNode);
            }
        } else if (command == "delete") {
            if (exists(root, key)) {
                remove(root, key);
            }
        } else if (command == "exists") {
            cout << (exists(root, key) ? "true" : "false") << "\n";
        } else if (command == "next") {
            Node* successor = next(root, key);
            if (successor) cout << successor->key << "\n";
            else cout << "none\n";
        } else if (command == "prev") {
            Node* predecessor = prev(root, key);
            if (predecessor) cout << predecessor->key << "\n";
            else cout << "none\n";
        }
    }
    
    return 0;
}

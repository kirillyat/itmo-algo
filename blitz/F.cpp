#include <iostream>
#include <stack>
#include <functional>
#include <algorithm>

int main() {
    std::stack<std::pair<std::function<int(int, int)>, int>> s;
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        int cmd, v;
        std::cin >> cmd >> v;
        s.push({[](int x, int y) { return std::max(x, y); }, 0});
        bool a = true;
        if (cmd == 1) { //max
            while (!s.empty()) {
                if (s.top().first(s.top().second, v) == std::max) {
                    if (s.top().second <= v) {
                        s.pop();
                    }
                    if (s.top().second <= v) {
                        s.pop();
                        s.push({[](int x, int y) { return std::min(x, y); }, v});
                        a = false;
                        break;
                    }
                    if (s.top().second > v) {
                        break;
                    }
                    if (s.top().first(s.top().second, v) == std::max && s.top().second >= v) {
                        a = false;
                        break;
                    }
                    break;
                }
            }
            if (a) {
                s.push({[](int x, int y) { return std::max(x, y); }, v});
            }
        } 
        else if (cmd == 2) { //min
            while (!s.empty()) {
                if (s.top().first(s.top().second, v) == std::max) {
                    if (s.top().second <= v) {
                        break;
                    }
                    if (s.top().second <= v) {
                        a = false;
                        break;
                    }
                    if (s.top().second > v) {
                        s.pop();
                    }
                    if (s.top().first(s.top().second, v) == std::max && s.top().second >= v) {
                        s.pop();
                        s.push({[](int x, int y) { return std::min(x, y); }, v});
                        a = false;
                        break;
                    }
                    break;
                }
            }
            if (a) {
                s.push({[](int x, int y) { return std::min(x, y); }, v});
            }
        } 
        else if (cmd == 3) {
            int v = 0;
            for (auto& p : s.begin()) {
                v = p.first(v, p.second);
            }
            std::cout << v << std::endl;
        }
    }

    return 0;
}

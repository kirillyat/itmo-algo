#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    int n;
    cin >> n;
    
    vector<pair<string, int> > blocks;

    for (int i = 0; i < n; ++i) {
        int cmd, v;
        cin >> cmd >> v;

        if (cmd == 1) {
            while (!blocks.empty() && 
                   ((blocks.back().first == "max" && blocks.back().second < v) ||
                    (blocks.back().first == "min" && blocks.back().second > v))) {
                blocks.pop_back();
            }
            blocks.push_back(make_pair("max", v));
        }

        if (cmd == 2) {
            while (!blocks.empty() && 
                   ((blocks.back().first == "min" && blocks.back().second < v) ||
                    (blocks.back().first == "max" && blocks.back().second > v))) {
                blocks.pop_back();
            }
            blocks.push_back(make_pair("min", v));
        }

        if (cmd == 3) {
            for (auto& block : blocks) {
                if (block.first == "max") {
                    v = max(block.second, v);
                } else if (block.first == "min") {
                    v = min(block.second, v);
                }
            }
            cout << v << endl;
        }

    }

    return 0;
}

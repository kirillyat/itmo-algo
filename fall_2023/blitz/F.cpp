#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int max_wrapper(int a, int b) {
    return max(a, b);
}

int min_wrapper(int a, int b) {
    return min(a, b);
}

int main() {
  int n;
  cin >> n;

  vector<pair<function<int(int, int)>, int> > s;

  for (int i = 0; i < n; ++i) {
      int cmd;
      int v;
      cin >> cmd >> v;

      if (cmd == 1) {
          while (!s.empty() && s.back().first(s.back().second, v) == s.back().second) {
              s.pop_back();
          }
          s.push_back(make_pair(max_wrapper, v));
      } else if (cmd == 2) {
          while (!s.empty() && s.back().first(s.back().second, v) == s.back().second) {
              s.pop_back();
          }
          s.push_back(make_pair(min_wrapper, v));
      } else if (cmd == 3) {
          int result = v;
          for (auto & block : s) {
              result = block.first(result, block.second);
          }
          cout << result << endl;
      }
  }

  return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> candies(n);
    for (int i = 0; i < n; i++) {
        std::cin >> candies[i];
    }

    std::sort(candies.begin(), candies.end());

    int ans = 0;
    int i = 0;
    while (i < candies.size() && candies[i] == candies[0]) {
        i++;
    }
    if (i == candies.size()) {
        std::cout << 0 << std::endl;
    } else {
        std::pair<int, int> a = std::make_pair(candies[0], i);
        std::pair<int, int> b = std::make_pair(candies[i], 1);

        for (int j = i + 1; j < candies.size(); j++) {
            if ((candies[j] - b.first) * b.second <= (b.first - a.first) * a.second) {
                ans += (candies[j] - b.first) * b.second;
                b.first = candies[j];
                b.second += 1;
            } else {
                ans += (b.first - a.first) * a.second;
                a.first = b.first;
                a.second += b.second;
                b = std::make_pair(candies[j], 1);
            }
        }

        std::cout << ans << std::endl;
    }

    return 0;
}

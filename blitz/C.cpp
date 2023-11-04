#include <iostream>
using namespace std;

int dist(int a, int b, int x, int y) {
    return (a-x)*(a-x) + (b-y)*(b-y);
}

int main() {
    int n, m, x, y, r;
    cin >> n >> m;
    cin >> x >> y >> r;
    int sx = max(0, x-r);
    int sy = max(0, y-r);
    int ex = min(n-1, x+r);
    int ey = min(m-1, y+r);
    int ans = 0;

    for (int i = sx; i <= ex; i++) {
        for (int j = sy; j <= ey; j++) {
            if (dist(i, j, x, y) <= r*r) {
                ans++;
            }
        }
    }

    cout << ans;
    return 0;
}

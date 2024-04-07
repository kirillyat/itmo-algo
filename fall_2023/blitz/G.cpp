#include <iostream>
#include <set>
#include <map>
using namespace std;

int main() {
    int m;
    cin >> m;

    set<int> available;
    map<int, set<int>::iterator> parked;

    for(int i = 1; i <= m + 1; i++) { // all parking slots are available initially
        available.insert(i);
    }

    for(int i = 0; i < m; i++) {
        char op;
        int car;
        cin >> op >> car;

        if(op == '+') {
            int slot = *available.begin();
            cout << slot << '\n';
            parked[car] = available.begin();
            available.erase(available.begin());
        } else {
            available.insert(*parked[car]);
            parked.erase(car);
        }
    }

    return 0;
}

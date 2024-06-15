#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

const int P = 31; // Обычное значение для базового числа
const ll MOD = 1e9 + 9; // Обычное значение для модуля

// Функция для вычисления хеша строки
ll computeHash(const string& s, vector<ll>& p, vector<ll>& h) {
    int n = s.size();
    p[0] = 1;
    for (int i = 1; i < n; i++)
        p[i] = (p[i-1] * P) % MOD;
    
    for (int i = 0; i < n; i++) {
        h[i+1] = (h[i] + (s[i] - 'a' + 1) * p[i]) % MOD;
    }
}

// Функция для вычисления хеша подстроки
ll substringHash(int l, int r, vector<ll>& p, vector<ll>& h) {
    ll hash = (h[r + 1] - h[l] + MOD) % MOD;
    hash = (hash * p[p.size() - l - 1]) % MOD;
    return hash;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    cin >> s >> t;

    int n = s.size();
    int m = t.size();

    int q;
    cin >> q;

    // Векторы для префиксных хешей и степеней базового числа
    vector<ll> p1(n + 1), h1(n + 1);
    vector<ll> p2(m + 1), h2(m + 1);

    computeHash(s, p1, h1);
    computeHash(t, p2, h2);

    while (q--) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        --l1; --r1; // Преобразуем индексы в 0-based
        --l2; --r2; // Преобразуем индексы в 0-based

        // Длина подстроки s
        int length_s = r1 - l1 + 1;
        // Хеш подстроки s
        ll hash_s = substringHash(l1, r1, p1, h1);

        int occurrences = 0;
        for (int i = l2; i + length_s - 1 <= r2; i++) {
            if (substringHash(i, i + length_s - 1, p2, h2) == hash_s) {
                occurrences++;
            }
        }

        cout << occurrences << '\n';
    }

    return 0;
}
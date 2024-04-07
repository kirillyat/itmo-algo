
#include <bits/stdc++.h>


#define forn(i,n) for(int i = 0; i < int(n); i++)
#define forsn(i,s,n) for(int i = int(s); i < int(n); i++)
#define dforn(i,n) for (int i = int(n)-1; i >= 0; i--)
#define dforsn(i,s,n) for(int i = int(n)-1; i >= int(s); i--)
#define all(c) (c).begin(),(c).end()
#define pb push_back
#define fst first
#define snd second
#define FAST_IO ios::sync_with_stdio(false);cin.tie(nullptr);

using namespace std;
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> ii;

const int MAXN = 102;
const int INF = 2e9+5;

ii P[MAXN];
int D[MAXN];

int roadblock(int N, int M, vector <int> a, vector <int> b, vector <int> c) {
    forn(i,MAXN) {D[i] = INF; P[i] = {-1,-1};}
    forn(i,M) {a[i]--; b[i]--;}
    D[0] = 0;
    forn(i,N) forn(j,M) { // Bellman-Ford
        int newD = D[a[j]]+c[j];
        if (newD < D[b[j]]) {D[b[j]] = newD; P[b[j]] = {a[j],j};}
        int newD2 = D[b[j]]+c[j];
        if (newD2 < D[a[j]]) {D[a[j]] = newD2; P[a[j]] = {b[j],j};}
    }
    int bst = D[N-1];
    vi ind;
    for (int i = N-1; P[i].snd != -1; i = P[i].fst)
        ind.pb(P[i].snd);

    int delta = 0;
    for (auto &i : ind) {
        c[i] <<= 1;
        forn(j,MAXN) D[j] = INF; D[0] = 0;
        forn(j,N) forn(k,M) {
            int newD = D[a[k]]+c[k];
            if (newD < D[b[k]]) D[b[k]] = newD;
            int newD2 = D[b[k]]+c[k];
            if (newD2 < D[a[k]]) D[a[k]] = newD2;
        }
        delta = max(delta,D[N-1]-bst);
        c[i] >>= 1;
    }

    return delta;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector <int> a(M), b(M), c(M);
    for(int i=0; i<M; i++)
        cin >> a[i] >> b[i] >> c[i];

    cout << roadblock(N, M, a, b, c) << endl;

    return 0;
}
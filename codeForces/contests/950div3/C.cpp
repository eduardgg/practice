
# include <iostream>
# include <vector>
# include <map>
# include <set>

using namespace std;

int main() {
    int t, n, m;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> a(n);
        vector<int> b(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        for (int i = 0; i < n; ++i) cin >> b[i];
        cin >> m;
        vector<int> d(m);
        for (int i = 0; i < m; ++i) cin >> d[i];
        set<int> sb(b.begin(), b.end());
        if (sb.find(d[m-1]) == sb.end()) {
            cout << "NO" << endl;
            continue;
        }
        map<int, int> D;
        for (int i = 0; i < n; ++i) {
            if (b[i] != a[i]) {
                D[b[i]] += 1;
            }
        }
        for (auto e : d) {
            if (D.find(e) != D.end()) {
                D[e] -= 1;
            }
        }
        bool ok = true;
        for (auto pair : D) {
            if (pair.second > 0) {
                ok = false;
                break;
            }
        }
        cout << (ok? "YES" : "NO") << endl;
    }
    return 0;
}
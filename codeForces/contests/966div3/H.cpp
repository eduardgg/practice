#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main() {
    int t, n, m, x;
    char c;
    cin >> t;

    while (t--) {
        cin >> n;
        map<int, set<int>> d;
        set<int> s;
        vector<int> ans;
        s.insert(0);
        d[1e7].insert(1);
        for (int i = 0; i < n; i ++) {
            cin >> x;
            if (s.lower_bound(x) == s.end()) {
                int xl = *--s.end();
                d[x - xl - 1].insert(xl + 1);
                d[1e7] = {x + 1};
            }
            else {
                auto slb = s.lower_bound(x);
                int xr = *slb;
                int xl = *--slb;
                d[xr - xl - 1].erase(xl + 1);
                if (d[xr - xl - 1].empty()) d.erase(xr - xl - 1);
                d[xr - x - 1].insert(x + 1);
                d[x - xl - 1].insert(xl + 1);
            }
            s.insert(x);
        }

        cin >> m;
        for (int i = 0; i < m; i ++) {
            
            /*
            cout << "Set: ";
            for (const auto& elem : s) cout << elem << " ";
            cout << endl << "Dictionary: ";
            for (const auto& pair : d) {
                cout << pair.first << " : ";
                for (const auto& elem : pair.second) {
                    cout << elem << " ";
                }
                cout << ",  ";
            }
            cout << endl;
            */

            cin >> c >> x;
            if (c == '+') {
                if (s.lower_bound(x) == s.end()) {
                    int xl = *--s.end();
                    d[x - xl - 1].insert(xl + 1);
                    d[1e7] = {x + 1};
                }
                else {
                    auto slb = s.lower_bound(x);
                    int xr = *slb;
                    int xl = *--slb;
                    d[xr - xl - 1].erase(xl + 1);
                    if (d[xr - xl - 1].empty()) d.erase(xr - xl - 1);
                    d[xr - x - 1].insert(x + 1);
                    d[x - xl - 1].insert(xl + 1);
                }
                s.insert(x);
            }
            else if (c == '-') {
                if (s.find(x) == --s.end()) {
                    auto xl = --s.find(x);
                    d[x - *xl - 1].erase(*xl + 1);
                    if (d[x - *xl - 1].empty()) d.erase(x - *xl - 1);
                    d[1e7] = {*xl + 1};
                }
                else {
                    int xr = *++s.find(x);
                    int xl = *--s.find(x);
                    d[xr - xl - 1].insert(xl + 1);
                    d[xr - x - 1].erase(x + 1);
                    if (d[xr - x - 1].empty()) d.erase(xr - x - 1);
                    d[x - xl - 1].erase(xl + 1);
                    if (d[x - xl - 1].empty()) d.erase(x - xl - 1);
                }
                s.erase(x);
            }
            else {
                ans.push_back(*(d.lower_bound(x)->second).begin());
            }
        }
        for (auto e : ans) cout << e << " ";
        cout << endl;
    }
    return 0;
}
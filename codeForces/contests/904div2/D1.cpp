#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        map<int, int> c;
        for (int num : a) {
            c[num]++;
        }

        vector<int> els;
        for (auto &p : c) {
            els.push_back(p.first);
        }
        sort(els.rbegin(), els.rend());

        unordered_map<int, int> dp;
        unordered_map<int, bool> used;
        int extra = 0;

        for (int e = n; e > 0; e--) {
            int s = c[e];
            int k = 2;
            while (k * e <= n) {
                dp[e] -= dp[k * e];
                if (find(els.begin(), els.end(), e) != els.end() && 
                    find(els.begin(), els.end(), k * e) == els.end() && 
                    !used[k * e]) {
                    used[k * e] = true;
                    extra += dp[k * e];
                }
                s += c[k * e];
                k++;
            }
            dp[e] += s * (s - 1) / 2;
        }

        int ans = n * (n - 1) / 2;
        for (const auto &p : dp) {
            if (find(els.begin(), els.end(), p.first) != els.end()) {
                ans -= p.second;
            }
        }
        ans -= extra;
        cout << ans << endl;
    }
    return 0;
}

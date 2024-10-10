#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        map<int, vector<int>> d;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            d[a[i] % k].push_back(a[i]);
        }
        int ans = 0;
        bool senar = false;
        for (auto &kv : d) {
            vector<int> &v = kv.second;
            sort(v.begin(), v.end());
            if (v.size() % 2 != 0) {
                if (n % 2 != 0 && !senar) {
                    senar = true;
                    if (v.size() == 1) {
                        continue;
                    }
                    vector<int> dp = {0, v[1] - v[0]};
                    for (int i = 2; i < v.size(); ++i) {
                        dp.push_back(v[i] - v[i - 1] + dp[i - 2]);
                        if (i % 2 == 0 && dp[i - 1] < dp.back()) {
                            dp.back() = dp[i - 1];
                        }
                    }
                    ans += dp.back() / k;
                    continue;
                } else {
                    ans = -1;
                    break;
                }
            }
            for (int i = 0; i < v.size() / 2; ++i) {
                ans += (v[2 * i + 1] - v[2 * i]) / k;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
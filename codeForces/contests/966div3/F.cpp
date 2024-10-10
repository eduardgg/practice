#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        const int maxn = 1e9;
        vector<int> dp(k + 2, maxn);
        dp[0] = 0;

        for (int i = 1; i <= n; ++i) {
            int a, b;
            cin >> a >> b;

            for (int p = k - 1; p >= 0; --p) {
                if (dp[p] == maxn) continue;

                int punts = 0;
                int cost = 0;
                int ai = a, bi = b;

                while (ai * bi > 1 && p + punts <= k) {
                    if (ai >= bi) {
                        punts += 1;
                        cost += bi;
                        ai -= 1;
                    } else {
                        punts += 1;
                        cost += ai;
                        bi -= 1;
                    }

                    dp[p + punts] = min(dp[p + punts], dp[p] + cost);
                }

                if (p + punts + 2 <= k + 1) {
                    dp[p + punts + 1] = min(dp[p + punts + 1], dp[p] + cost + 1);
                    dp[p + punts + 2] = min(dp[p + punts + 2], dp[p] + cost + 1);
                }
            }
        }

        int ans = dp[k];
        cout << (ans == maxn ? -1 : ans) << endl;
    }

    return 0;
}

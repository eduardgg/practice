#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <numeric>
#include <climits>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        vector<long long> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        
        vector<vector<int>> t(n);
        for (int i = 0; i < n - 1; ++i) {
            int x, y;
            cin >> x >> y;
            t[x - 1].push_back(y - 1);
            t[y - 1].push_back(x - 1);
        }
        
        vector<int> dfs = {0};
        stack<int> stack;
        stack.push(0);
        
        vector<int> parent(n, -1);
        vector<long long> dp(n, -1);
        
        while (!stack.empty()) {
            int u = stack.top();
            stack.pop();
            if (t[u].size() == 1) {
                dp[u] = a[u];
            }
            for (int v : t[u]) {
                if (v != parent[u]) {
                    parent[v] = u;
                    dfs.push_back(v);
                    stack.push(v);
                }
            }
        }
        
        vector<vector<long long>> dp_table(20, vector<long long>(n, -1));
        
        for (int u = dfs.size() - 1; u >= 0; --u) {
            int node = dfs[u];
            for (int i = 0; i < 20; ++i) {
                dp_table[i][node] = i * a[node];
                for (int v : t[node]) {
                    if (v != parent[node]) {
                        long long min_val = LLONG_MAX;
                        for (int j = 0; j < 20; ++j) {
                            if (j != i) {
                                min_val = min(min_val, dp_table[j][v]);
                            }
                        }
                        dp_table[i][node] += min_val;
                    }
                }
            }
        }
        
        long long total_sum = accumulate(a.begin(), a.end(), 0LL);
        long long min_dp0 = LLONG_MAX;
        for (int i = 0; i < 20; ++i) {
            if (dp_table[i][0] < min_dp0) {
                min_dp0 = dp_table[i][0];
            }
        }
        long long ans = total_sum + min_dp0;
        
        cout << ans << endl;
    }
    
    return 0;
}
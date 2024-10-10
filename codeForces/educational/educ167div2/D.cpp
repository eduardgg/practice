#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> a, p, dp;

int f(int e) {
    if (e >= a.back()) {
        int ops = (e - a.back()) / p.back() + 1;
        return ops + f(e - ops * p.back());
    }
    if (e < a[0]) {
        return 0;
    }
    if (dp[e] != -1) {
        return dp[e];
    }
    auto it = upper_bound(a.begin(), a.end(), e);
    int i = distance(a.begin(), it);
    int ops = (e - a[i-1]) / p[i-1] + 1;
    dp[e] = ops + f(e - ops * p[i-1]);
    return dp[e];
}

int main() {
    int n, m;
    cin >> n >> m;
    
    a.resize(n);
    vector<int> b(n), c(m);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }
    for (int i = 0; i < m; ++i) {
        cin >> c[i];
    }

    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; ++i) {
        v[i] = {a[i], a[i] - b[i]};
    }
    sort(v.begin(), v.end());
    sort(a.begin(), a.end());

    p.resize(n);
    int cur = INT_MAX;
    for (int i = 0; i < n; ++i) {
        cur = min(cur, v[i].second);
        p[i] = cur;
    }

    long long int ans = 0;
    dp.assign(1000001, -1);
    for (int e : c) {
        ans += f(e);
    }

    ans *= 2;
    cout << ans << endl;

    return 0;
}
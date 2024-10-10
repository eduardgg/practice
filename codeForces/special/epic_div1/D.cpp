
#include <bits/stdc++.h>
using namespace std;
#define maxn 500005

int n, q, parent[maxn], p[maxn], pos[maxn], sizes[maxn];
set<int> son[maxn];

int check(int x) {
    if (son[x].empty()) return 1;
    return (pos[x] < *son[x].begin() && *--son[x].end() + sizes[p[*--son[x].end()]] <= pos[x] + sizes[x]);
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        cin >> n >> q;
        for (int i = 1; i <= n; i++) sizes[i] = 1, son[i].clear();
        for (int i = 2; i <= n; i++) cin >> parent[i];
        for (int i = n; i >= 2; i--) sizes[parent[i]] += sizes[i];
        for (int i = 1; i <= n; i++) {
            cin >> p[i];
            son[parent[p[i]]].insert(i);
            pos[p[i]] = i;
        }
        int counter = 0;
        for (int i = 1; i <= n; i++) counter += check(i);
        while(q--) {
            int i, j, x, y;
            cin >> i >> j;
            x = p[i]; y = p[j];
            set<int> s = {x, y, parent[x], parent[y]};
            for (auto x: s) if(x) counter -= check(x);
            son[parent[x]].erase(i), son[parent[y]].erase(j);
            swap(p[i], p[j]), swap(pos[x], pos[y]);
            son[parent[x]].insert(j), son[parent[y]].insert(i);
            for (auto x: s) if(x) counter += check(x);
            puts(counter == n ? "YES" : "NO");
        }
    };
    return 0;
}
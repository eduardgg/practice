#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

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

        vector<int> b(n);
        unordered_map<int, int> d;

        for (int i = 0; i < n; ++i) {
            if (d.find(a[i]) == d.end()) {
                d[a[i]] = i;
            }
            b[i] = d[a[i]];
        }

        int m;
        cin >> m;

        while (m--) {
            string s;
            cin >> s;

            if (s.length() != n) {
                cout << "NO" << endl;
                continue;
            }

            vector<int> d(26, -1);
            bool ok = true;

            for (int i = 0; i < n; ++i) {
                int index = s[i] - 'a';
                if (d[index] == -1) {
                    d[index] = i;
                }
                if (d[index] != b[i]) {
                    ok = false;
                    break;
                }
            }

            cout << (ok ? "YES" : "NO") << endl;
        }
    }

    return 0;
}

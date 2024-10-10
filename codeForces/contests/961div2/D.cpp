#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <bitset>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, c, k;
        cin >> n >> c >> k;
        string s;
        cin >> s;

        int bm = 0;
        vector<int> prefix(26, 0);
        for (int i = 0; i < k; ++i) {
            int pos = s[i] - 'A';
            prefix[pos]++;
            bm |= (1 << pos);
        }

        unordered_set<int> substrs;
        substrs.insert(bm);
        for (int i = 0; i < n - k; ++i) {
            int newpos = s[k + i] - 'A';
            int oldpos = s[i] - 'A';
            prefix[newpos]++;
            prefix[oldpos]--;
            bm |= (1 << newpos);
            if (prefix[oldpos] == 0) {
                bm &= ~(1 << oldpos);
            }
            substrs.insert(bm);
        }

        set<int> dp;
        for (int e = 1; e < (1 << c); ++e) {
            if (e & (1 << (s.back() - 'A'))) {
                dp.insert(e);
            }
        }

        for (int ss : substrs) {
            for (auto it = dp.begin(); it != dp.end(); ) {
                if ((ss & *it) == 0) {
                    it = dp.erase(it);
                } else {
                    ++it;
                }
            }
        }

        int ans = c;
        for (int st : dp) {
            ans = min(ans, __builtin_popcount(st));
        }
        cout << ans << endl;
    }

    return 0;
}

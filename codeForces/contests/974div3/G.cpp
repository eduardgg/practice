#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>  // per a la funció max i min
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m, k, d, a;
        cin >> n >> m >> k;
        cin >> d >> a;
        n -= 1;
        int i = 1;
        int ans = 0;
        stack<pair<int, int>> stk;

        while (n > 0 || i - d < k) {
            if (i == d) {
                stk.push({d, a});
                if (n > 0) {
                    cin >> d >> a;
                    n -= 1;
                }
            }

            int mc = m;
            bool b = false;

            while (!stk.empty()) {
                auto [dn, an] = stk.top();
                stk.pop();

                if (i - dn >= k) {
                    continue;
                }

                if (an >= mc) {
                    ans += 1;
                    i += 1;
                    b = true;
                    an -= mc;

                    int incr = max(0, min(an / m, min(dn + k - i, d - i)));
                    ans += incr;
                    i += incr;
                    an -= incr * m;

                    stk.push({dn, an});
                    break;
                } else {
                    mc -= an;
                }
            }

            if (!b) {
                i = max(i+1, d);
            }
        }

        cout << ans << endl;
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        vector<int> a(n), b(m);
        for (int i = 0; i < n; ++i) cin >> a[i];
        for (int i = 0; i < m; ++i) cin >> b[i];

        int kmax;
        if (n > 2 * m) {
            kmax = m;
        } else if (m > 2 * n) {
            kmax = n;
        } else {
            kmax = (n + m) / 3;
        }
        cout << kmax << "\n";

        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        vector<int> adre(a.begin() + n / 2, a.end());
        vector<int> aesq(a.begin(), a.begin() + n / 2);
        reverse(aesq.begin(), aesq.end());

        vector<int> bdre(b.begin() + m / 2, b.end());
        vector<int> besq(b.begin(), b.begin() + m / 2);
        reverse(besq.begin(), besq.end());

        for (int i = 1; i <= kmax; ++i) {
            vector<int> adre2 = adre, aesq2 = aesq, bdre2 = bdre, besq2 = besq;
            int n2 = n, m2 = m, ans = 0;

            for (int e = 0; e < i; ++e) {
                if (n2 == i - e) {
                    ans += bdre2.back() - besq2.back();
                    bdre2.pop_back();
                    besq2.pop_back();
                    n2 -= 1;
                    m2 -= 2;
                } else if (m2 == i - e) {
                    ans += adre2.back() - aesq2.back();
                    adre2.pop_back();
                    aesq2.pop_back();
                    n2 -= 2;
                    m2 -= 1;
                } else if (bdre2.back() - besq2.back() > adre2.back() - aesq2.back()) {
                    ans += bdre2.back() - besq2.back();
                    bdre2.pop_back();
                    besq2.pop_back();
                    n2 -= 1;
                    m2 -= 2;
                } else {
                    ans += adre2.back() - aesq2.back();
                    adre2.pop_back();
                    aesq2.pop_back();
                    n2 -= 2;
                    m2 -= 1;
                }
            }
            cout << ans << " ";
        }
        cout << "\n";
    }

    return 0;
}

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    long long obj = (1LL * n * n) / 2;
    long long l = 1, r = 1LL * n * n;

    while (r - l > 1) {
        long long m = (r + l) / 2;
        long long less = 0, trobat = 0;

        for (int i = 1; i <= n; ++i) {
            less += min(m / i, (long long)n);
            if (m % i == 0 && m / i <= n) {
                ++trobat;
            }
        }

        if (less - trobat > obj) {
            r = m;
        } else if (less <= obj) {
            l = m + 1;
        } else {
            l = m;
            break;
        }

    }

    cout << l << endl;
    return 0;
}

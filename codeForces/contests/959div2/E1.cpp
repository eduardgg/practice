#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int k;
        cin >> k;
        vector<int> sizes;

        for (int i = 0; i < k; ++i) {
            int n;
            cin >> n;
            sizes.push_back(n);
            int val;
            for (int i = 1; i < n; ++ i) {
                cin >> val;
            }
        }

        sort(sizes.begin(), sizes.end());

        unsigned int ans = 0;
        while (!sizes.empty()) {
            int s = sizes.back();
            sizes.pop_back();
            
            unsigned int highest_bit = 1 << (int(log2(s)));

            if ((highest_bit & ans) != 0) {
                ans |= (highest_bit - 1);
                break;
            }
            ans |= s;
        }
        
        cout << ans << endl;
    }

    return 0;
}

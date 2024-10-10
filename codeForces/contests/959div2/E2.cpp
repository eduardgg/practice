#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    for (int i = 0; i < t; ++i) {
        int k;
        cin >> k;
        unsigned int ans = 0;
        
        for (int j = 0; j < k; ++j) {
            int n;
            cin >> n;
            vector<int> l(n-1);
            for (int i = 0; i < n-1; ++ i) {
                cin >> l[i];
            }

            unsigned int highest_bit = 1 << (int(log2(n)));

            if ((highest_bit & ans) != 0) {
                ans |= (highest_bit - 1);
            } else {
                ans |= n;
            }
        }
        cout << ans << endl;
    }
    
    return 0;
}

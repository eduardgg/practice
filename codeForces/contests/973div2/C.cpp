#include <iostream>
#include <vector>
using namespace std;

void reverse_vector(vector<char>& vec) {
    int n = vec.size();
    for (int i = 0; i < n / 2; ++i) {
        swap(vec[i], vec[n - i - 1]);
    }
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<char> ans;

        while (ans.size() < n) {
            cout << "? ";
            for (char c : ans) cout << c;
            cout << "1" << endl;
            fflush(stdout);

            string response;
            cin >> response;
            if (response == "1") {
                ans.push_back('1');
            } else {
                cout << "? ";
                for (char c : ans) cout << c;
                cout << "0" << endl;
                fflush(stdout);

                cin >> response;
                if (response == "1") {
                    ans.push_back('0');
                } else {
                    break;
                }
            }
        }

        reverse_vector(ans);

        while (ans.size() < n) {
            cout << "? 1";
            for (char c : ans) cout << c;
            cout << endl;
            fflush(stdout);

            char next_char;
            cin >> next_char;
            ans.push_back(next_char);
        }

        reverse_vector(ans);

        cout << "! ";
        for (char c : ans) cout << c;
        cout << endl;
        fflush(stdout);

    }

    return 0;
}

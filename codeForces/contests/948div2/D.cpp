
// No és el meu problema preferit però estic molt orgullós
// del resultat, i de com motivar-me a utilitzar C++ per
// combatre el recursion depth gegant del backtracking
// ha donat els seus fruits! També he hagut de fer algunes
// optimitzacions al codi, com introduir el vector "notUse"
// per evitar el cost excessiu d'iterar en massa vectors
// plens de zeros.

#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

int n, m;
vector<string> mat;
vector<int> v;
vector<bool> notUse;
string xorVec;

int f(int i, set<int> cjt, int& top, string& topstr) {
    
    if (cjt.size() <= top) {
        return 0;
    }
    
    if (i == n) {
        int ans = 0;
        for (int e : cjt) {
            if (v[e] == 1) {
                ans += 1;
            }
        }
        if (ans > top) {
            top = ans;
            topstr = xorVec;
        }
        return ans;
    }

    if (notUse[i]) {
        if (mat[i][0] == '0') {
            xorVec[i] = '0';
            return f(i + 1, cjt, top, topstr);
        }
        else {
            xorVec[i] = '1';
            return f(i + 1, cjt, top, topstr);
        }
    }
    
    vector<int> backup = v;
    set<int> cjt1 = cjt;
    xorVec[i] = '0';
    for (int j : cjt) {
        v[j] += mat[i][j] - '0';
        if (v[j] > 1) cjt1.erase(j);
    }
    int ans1 = f(i + 1, cjt1, top, topstr);

    v = backup;
    set<int> cjt2 = cjt;
    xorVec[i] = '1';
    for (int j : cjt) {
        v[j] += 1 - (mat[i][j] - '0');
        if (v[j] > 1) cjt2.erase(j);
    }
    int ans2 = f(i + 1, cjt2, top, topstr);

    return max(ans1, ans2);
}

int main() {
    int t;
    cin >> t;
    cin.ignore();
    for (int _ = 0; _ < t; ++_ ) {
        cin >> n >> m;
        mat = vector<string>(n);
        v = vector<int>(m, 0);
        xorVec = string(n, '-');
        notUse = vector<bool>(n, true);
        bool primer = false;
        for (int i = 0; i < n; ++i) {
            cin >> mat[i];
            for (int j = 1; j < m; ++j) {
                if (mat[i][j] != mat[i][j-1]) {
                    notUse[i] = false;
                    break;
                }
            }
            if (notUse[i] and not primer) {
                notUse[i] = false;
                primer = true;
            }
        }
        set<int> cjt;
        for (int i = 0; i < m; ++i) {
            cjt.insert(i);
        }
        int top = 0;
        string topstr = "";
        int ans = f(0, cjt, top, topstr);
        cout << top << endl;
        cout << topstr << endl;
    }
    return 0;
}

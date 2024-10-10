#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        int t0, t1, t2;
        cin >> t0 >> t1 >> t2;

        // Crear el graf com a llista d'adjacències
        vector<vector<tuple<int, int, int>>> g(n + 1); 

        // Llegir les arestes del graf
        for (int i = 0; i < m; ++i) {
            int u, v, l1, l2;
            cin >> u >> v >> l1 >> l2;
            g[u].emplace_back(v, l1, l2);
            g[v].emplace_back(u, l1, l2);
        }

        // Inicialitzar el vector "best" i "fet"
        vector<int> best(n, INT_MAX);
        best.push_back(0);  // L'últim node (n) té cost 0

        vector<bool> fet(n, false);
        fet.push_back(true);  // El node n ja està processat

        // Crear la cua de prioritats (min-heap)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        heap.emplace(0, n);  // Inserir el node n amb cost 0

        // Algoritme principal
        while (!heap.empty()) {
            int t = heap.top().first;
            int u = heap.top().second;
            heap.pop();

            fet[u] = true;

            // Si arribem al node 1 o si el cost és major que t0, aturar
            if (u == 1 || best[u] > t0) break;

            // Processar els veïns del node actual
            for (const auto& [v, l1, l2] : g[u]) {
                if (fet[v]) continue;

                // Actualitzar el millor camí per al node v
                best[v] = min(best[v], best[u] + l2);

                if (best[u] + l1 <= t0 - t2) {
                    best[v] = min(best[v], best[u] + l1);
                } else {
                    best[v] = min(best[v], max(t0 - t1, best[u]) + l1);
                }

                // Inserir el nou cost del node v a la cua
                heap.emplace(best[v], v);
            }
        }

        // Resultat final
        int result = max(t0 - best[1], -1);
        cout << result << endl;
    }

    return 0;
}

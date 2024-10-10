#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Graph {
    int V;
    vector<int> *adj;

public:
    Graph(int V);
    void addEdge(int u, int v);
    Graph getTranspose();
    void DFSUtil(int v, vector<bool> &visited, vector<int> &scc);
    void fillOrder(int v, vector<bool> &visited, stack<int> &Stack);
    vector<vector<int>> kosarajuSCC();
};

Graph::Graph(int V) {
    this->V = V;
    adj = new vector<int>[V];
}

void Graph::addEdge(int u, int v) {
    adj[u].push_back(v);
}

Graph Graph::getTranspose() {
    Graph g(V);
    for (int v = 0; v < V; v++) {
        for (auto i = adj[v].begin(); i != adj[v].end(); ++i) {
            g.adj[*i].push_back(v);
        }
    }
    return g;
}

void Graph::DFSUtil(int v, vector<bool> &visited, vector<int> &scc) {
    visited[v] = true;
    scc.push_back(v);

    for (auto i = adj[v].begin(); i != adj[v].end(); ++i) {
        if (!visited[*i]) {
            DFSUtil(*i, visited, scc);
        }
    }
}

void Graph::fillOrder(int v, vector<bool> &visited, stack<int> &Stack) {
    visited[v] = true;

    for (auto i = adj[v].begin(); i != adj[v].end(); ++i) {
        if (!visited[*i]) {
            fillOrder(*i, visited, Stack);
        }
    }
    Stack.push(v);
}

vector<vector<int>> Graph::kosarajuSCC() {
    stack<int> Stack;
    vector<bool> visited(V, false);
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            fillOrder(i, visited, Stack);
        }
    }

    Graph gr = getTranspose();

    for (int i = 0; i < V; i++) {
        visited[i] = false;
    }

    vector<vector<int>> SCCs;
    while (!Stack.empty()) {
        int v = Stack.top();
        Stack.pop();

        if (!visited[v]) {
            vector<int> scc;
            gr.DFSUtil(v, visited, scc);
            SCCs.push_back(scc);
        }
    }
    return SCCs;
}

bool isSatisfiable(int n, vector<pair<int, int>> clauses) {
    Graph g(2 * n);

    for (auto clause : clauses) {
        int u = clause.first;
        int v = clause.second;

        if (u > 0 && v > 0) {
            g.addEdge(u + n - 1, v - 1);
            g.addEdge(v + n - 1, u - 1);
        } else if (u > 0 && v < 0) {
            g.addEdge(u + n - 1, -v + n - 1);
            g.addEdge(-v - 1, u - 1);
        } else if (u < 0 && v > 0) {
            g.addEdge(-u - 1, v - 1);
            g.addEdge(v + n - 1, -u + n - 1);
        } else {
            g.addEdge(-u - 1, -v + n - 1);
            g.addEdge(-v - 1, -u + n - 1);
        }
    }

    vector<vector<int>> SCCs = g.kosarajuSCC();

    for (auto scc : SCCs) {
        for (int i : scc) {
            if (find(scc.begin(), scc.end(), i + n) != scc.end()) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    
    int t;
    cin >> t;

    while (t --) {

        int n = 3;
        cin >> n;

        vector<vector<int>> M(3, vector<int>(n));
        for (int i = 0; i < 3; ++ i) {
            for (int j = 0; j < n; ++ j) {
                cin >> M[i][j];
            }
        }

        vector<pair<int, int>> clauses;

        for (int i = 0; i < n; ++ i) {
            clauses.push_back(pair<int, int> (M[0][i], M[1][i]));
            clauses.push_back(pair<int, int> (M[1][i], M[2][i]));
            clauses.push_back(pair<int, int> (M[2][i], M[0][i]));
        }

        cout << (isSatisfiable(n, clauses) ? "YES" : "NO") << endl;
        
    }

    return 0;
}
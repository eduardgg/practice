#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// Funció recursiva per construir el recorregut postordre
void buildPostOrder(const vector<int>& preOrder, const vector<int>& inOrder, 
                    int preStart, int preEnd, int inStart, int inEnd,
                    unordered_map<int, int>& inOrderMap) {
    if (preStart > preEnd || inStart > inEnd) {
        return;
    }

    // La primera entrada del preordre és l'arrel
    int root = preOrder[preStart];

    // Troba la posició de l'arrel al recorregut inOrder en O(1)
    int rootIndex = inOrderMap[root];

    // Calcular la mida del subarbre esquerre
    int leftSubtreeSize = rootIndex - inStart;

    // Processa el subarbre esquerre
    buildPostOrder(preOrder, inOrder, preStart + 1, preStart + leftSubtreeSize,
                   inStart, rootIndex - 1, inOrderMap);

    // Processa el subarbre dret
    buildPostOrder(preOrder, inOrder, preStart + leftSubtreeSize + 1, preEnd,
                   rootIndex + 1, inEnd, inOrderMap);

    // Imprimeix l'arrel després dels subarbres (postordre)
    cout << root << " ";
}

int main() {
    int n;
    cin >> n;

    vector<int> preOrder(n), inOrder(n);

    // Llegeix el recorregut preordre
    for (int i = 0; i < n; ++i) {
        cin >> preOrder[i];
    }

    // Llegeix el recorregut inordre
    for (int i = 0; i < n; ++i) {
        cin >> inOrder[i];
    }

    // Crea un mapa per guardar les posicions dels nodes a inOrder
    unordered_map<int, int> inOrderMap;
    for (int i = 0; i < n; ++i) {
        inOrderMap[inOrder[i]] = i;
    }

    // Construeix el postordre a partir dels límits inicials
    buildPostOrder(preOrder, inOrder, 0, n - 1, 0, n - 1, inOrderMap);
    cout << endl;

    return 0;
}

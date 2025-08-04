#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Funció recursiva per imprimir el recorregut postordre
void printPostOrder(vector<int>& preOrder, vector<int>& inOrder) {
    if (preOrder.size() != inOrder.size()) {
        cout << "Length Error!" << endl;
        return;
    }

    if (preOrder.empty()) {
        return;
    }

    // Troba la posició de la root en el recorregut inordre
    int root = preOrder[0];
    auto it = find(inOrder.begin(), inOrder.end(), root);

    if (it == inOrder.end()) {
        cout << "Element not found in inOrder!" << endl;
        return;
    }

    int rootIndex = distance(inOrder.begin(), it);

    // Divideix els recorreguts en subarbres esquerre i dret
    vector<int> leftPreOrder(preOrder.begin() + 1, preOrder.begin() + 1 + rootIndex);
    vector<int> leftInOrder(inOrder.begin(), inOrder.begin() + rootIndex);
    vector<int> rightPreOrder(preOrder.begin() + 1 + rootIndex, preOrder.end());
    vector<int> rightInOrder(inOrder.begin() + rootIndex + 1, inOrder.end());

    // Processa els subarbres recursivament
    printPostOrder(leftPreOrder, leftInOrder);
    printPostOrder(rightPreOrder, rightInOrder);

    // Imprimeix l'arrel
    cout << root << " ";
}

int main() {
    int n;
    cin >> n;

    vector<int> preOrder(n), inOrder(n);

    for (int i = 0; i < n; ++i) {
        cin >> preOrder[i];
    }

    for (int i = 0; i < n; ++i) {
        cin >> inOrder[i];
    }

    printPostOrder(preOrder, inOrder);
    cout << endl;

    return 0;
}

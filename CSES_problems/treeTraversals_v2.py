
def printPostOrder(po, io, k):
    if len(po) != len(io):
        print("Length Error!")
        return
    if len(po) == 0:
        return
    i = index[po[0]]
    printPostOrder(po[1:i-k+1], io[:i-k], k)
    printPostOrder(po[i-k+1:], io[i-k+1:], i+1)
    print(po[0], end = " ")

n = int(input())
preOrder = list(map(int, input().split()))
inOrder = list(map(int, input().split()))
index = {inOrder[i]:i for i in range(n)}
# He hagut de definir aquest mapa per evitar cost quadràtic.
# Com que la funció recursiva es crida fent servir trossos del
# inOrder i preOrder, cal saber a quina posició real correspon
# el primer element del subvector agafat. Ho fem amb l'input k.

printPostOrder(preOrder, inOrder, 0)
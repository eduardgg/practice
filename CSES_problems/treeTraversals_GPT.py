def printPostOrder(preOrder, inOrder):
    # Crea un diccionari per emmagatzemar les posicions dels elements en inOrder
    inOrderMap = {value: index for index, value in enumerate(inOrder)}

    # Funció recursiva utilitzant índexs en lloc de subllistes
    def buildPostOrder(preStart, preEnd, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return

        # L'arrel és el primer element del subarray preOrder
        root = preOrder[preStart]

        # Troba la posició de l'arrel al inOrder en O(1)
        rootIndex = inOrderMap[root]

        # Mida del subarbre esquerre
        leftSubtreeSize = rootIndex - inStart

        # Processa el subarbre esquerre
        buildPostOrder(preStart + 1, preStart + leftSubtreeSize, inStart, rootIndex - 1)

        # Processa el subarbre dret
        buildPostOrder(preStart + leftSubtreeSize + 1, preEnd, rootIndex + 1, inEnd)

        # Imprimeix l'arrel (postordre)
        print(root, end=" ")

    # Crida inicial amb els límits complets
    buildPostOrder(0, len(preOrder) - 1, 0, len(inOrder) - 1)


# Lectura de dades d'entrada
n = int(input())
preOrder = list(map(int, input().split()))
inOrder = list(map(int, input().split()))

# Crida a la funció per imprimir el postordre
printPostOrder(preOrder, inOrder)

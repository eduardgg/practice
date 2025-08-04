
def printPostOrder(po, io):
    if len(po) != len(io):
        print("Length Error!")
        return
    if len(po) == 0:
        return
    i = io.index(po[0])
    printPostOrder(po[1:i+1], io[:i])
    printPostOrder(po[i+1:], io[i+1:])
    print(po[0], end = " ")

n = int(input())
preOrder = list(map(int, input().split()))
inOrder = list(map(int, input().split()))
printPostOrder(preOrder, inOrder)
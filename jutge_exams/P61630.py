
def f(linies, j, i):

    n = len(linies)
    m = len(linies[0])
    
    if j == n:
        for l in linies:
            print(''.join(l))
        print()
        return
    
    if linies[j][i] != '?':
        if i < m-1:
            f(linies, j, i+1)
            return
        f(linies, j+1, 0)
        return
    
    linies[j][i] = '.'
    if i < m-1:
        f(linies, j, i+1)
    else:
        f(linies, j+1, 0)
    
    for y in range(max(0, j-1), min(n, j+2)):
        for x in range(max(0, i-1), min(m, i+2)):
            if (x != i or y != j) and linies[y][x] == 'C':
                linies[j][i] = '?'
                return
                 
    linies[j][i] = 'C'
    if i < m-1:
        f(linies, j, i+1)
    else:
        f(linies, j+1, 0)

    linies[j][i] = '?'
    return
            

def main():
    while True:
        linia = input().split(" ")
        n = int(linia[0])
        linies = []
        for _ in range(n):
            linies += [list(input())]
        f(linies, 0, 0)
        print("----------")
        _ = input()

if __name__ == "__main__":
    main()
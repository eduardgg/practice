
def matriu_integral(matriu):
    n = len(matriu)
    integral = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            integral[i][j] = matriu[i-1][j-1] + integral[i][j-1] + integral[i-1][j] - integral[i-1][j-1]
    return integral

def main():
    while True:
        linia = input().split(" ")
        n, m = (int(linia[0]), int(linia[1]))
        matriu = []
        for _ in range(n):
            fila = list(map(int, input().split()))
            matriu.append(fila)
        integral = matriu_integral(matriu)
        maxim = float('-inf')
        for i in range(n-3*m+1):
            for j in range(n-3*m+1):
                quadratGran = integral[i+3*m][j+3*m] - integral[i][j+3*m] - integral[i+3*m][j] + integral[i][j]
                quadratPetit = integral[i+2*m][j+2*m] - integral[i+m][j+2*m] - integral[i+2*m][j+m] + integral[i+m][j+m]
                donut = quadratGran - quadratPetit
                maxim = max(maxim, donut)
        print(maxim)
        _ = input()

        
if __name__ == "__main__":
    main()
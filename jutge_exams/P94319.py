
def exp_modular(base, exponent, modul):
    result = 1
    base = base % modul

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modul
        exponent = exponent // 2
        base = (base * base) % modul

    return result

def main():
    GRAN = 10**9 + 7
    while True:
        linia = input().split(" ")
        n, v, c = (int(linia[0]), int(linia[1]), int(linia[2]))
        # Paraules de n lletres, v vocals, c consonants.
        # Definim C: paraules sense vocals seguides, que acaben en consonant
        # Definim P: paraules sense vocals seguides, totals
        # Establim una recurrència senzilla usant les dues funcions:
        (P, C) = (c+v, c)
        for _ in range(n-1):
            (P, C) = (c*P + v*C, c*P)
            P = P % GRAN
            C = C % GRAN
        # Al resultat final (P), cal restar aquelles paraules sense cap vocal:
        resultat = (P - exp_modular(c, n, GRAN)) % GRAN
        print(resultat)
        
        
if __name__ == "__main__":
    main()

def f(paraula, alfabet, vocals, consonants, n):
    if len(paraula) == n:
        hiHaVocals = False
        for char in paraula:
            if char in vocals:
                hiHaVocals = True
                break
        if hiHaVocals:
            print(paraula)
        return
    if (len(paraula) > 0) and (paraula[-1] in vocals):
        for char in consonants:
            f(paraula + char, alfabet, vocals, consonants, n)
        return
    for char in alfabet:
        f(paraula + char, alfabet, vocals, consonants, n)
    return

def main():
    while True:
        linia = input().split(" ")
        n, v, c = (int(linia[0]), int(linia[1]), int(linia[2]))
        # Paraules de n lletres, v vocals, c consonants.
        vocals = list("aeiou"[:v])
        consonants = list("bcdfghjklmnpqrstvwxyz"[:c])
        alfabet = sorted(vocals + consonants)
        f("", alfabet, vocals, consonants, n)
        print("----------")

if __name__ == "__main__":
    main()
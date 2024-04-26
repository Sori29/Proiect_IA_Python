import random
import math

def numar_conflicte(stare):
    """Calcularea numărului de conflicte dintr-o stare"""
    n = len(stare)
    numar = 0
    for i in range(n):
        for j in range(i+1, n):
            # Verificăm dacă reginele sunt pe aceeași diagonală
            if abs(i-j) == abs(stare[i]-stare[j]):
                numar += 1
            # Verificăm dacă reginele sunt pe aceeași linie
            if stare[i] == stare[j]:
                numar += 1
    return numar

def mutare_aleatoare(stare):
    """Mutăm aleator un element din starea curentă"""
    n = len(stare)
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    noua_stare = list(stare)
    noua_stare[i] = j
    return tuple(noua_stare)

def accepta_ea(noua_conflicte, vechi_conflicte, temperatura):
    """Determinăm dacă o mutare trebuie acceptată"""
    if noua_conflicte <= vechi_conflicte:
        return True
    probabilitate = math.exp((vechi_conflicte - noua_conflicte) / temperatura)
    return random.random() < probabilitate

def cautare_simulata(n):
    """Algoritmul de căutare simulată pentru problema celor N regine"""
    stare_curenta = tuple(random.randint(0, n-1) for i in range(n))
    temperatura = 1000
    temperatura_minima = 0.01
    reducerea_temperaturii = 0.95
    while temperatura > temperatura_minima:
        # Facem o mutare aleatoare în starea curentă
        stare_noua = mutare_aleatoare(stare_curenta)
        # Calculăm numărul de conflicte pentru starea nouă și veche
        vechi_conflicte = numar_conflicte(stare_curenta)
        noua_conflicte = numar_conflicte(stare_noua)
        # Acceptăm sau nu mutarea
        if accepta_ea(noua_conflicte, vechi_conflicte, temperatura):
            stare_curenta = stare_noua
        # Scădem temperatura
        temperatura *= reducerea_temperaturii
    return stare_curenta

def afisare_fisier(stare_finala,numeFisier):
    with open(numeFisier,"w") as f:
       f.write(",".join(map(str, stare_finala)) + "\n")
       f.write(str(numar_conflicte(stare_finala)))

# Exemplu de utilizare
#n = 8
#stare_finala = cautare_simulata(n)
#print("Starea finală: ", stare_finala)
#print("Numărul de conflicte: ", numar_conflicte(stare_finala))

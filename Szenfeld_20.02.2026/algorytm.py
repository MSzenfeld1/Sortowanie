# *************** algorytm.edu.pl ***********************

def sortowanie_przez_wstawianie(lista, n):
    for i in range(1, n):
        # wstawienie elementu w odpowiednie miejsce
        pom = lista[i]          # ten element zostanie wstawiony w odpowiednie miejsce
        j = i - 1

        # przesuwanie elementów większych od pom
        while j >= 0 and lista[j] > pom:
            lista[j + 1] = lista[j]   # przesuwanie elementów
            j -= 1

        lista[j + 1] = pom     # wstawienie wartości zmiennej pom w odpowiednie miejsce


# *************** Główna część programu ***********************

n = int(input("Podaj wielość zbioru: "))
lista = []

for i in range(n):
    lista.append(int(input()))

sortowanie_przez_wstawianie(lista, n)   # sortujemy dane

# wypisujemy listę po wykonaniu sortowania
print(*lista)

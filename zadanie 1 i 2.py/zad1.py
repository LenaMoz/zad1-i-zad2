##
def dodaj_wpis(slowo, definicja, slownik):
    slownik[slowo] = definicja
    print(f'Dodano wpis: {slowo} - {definicja}')

def edytuj_wpis(slowo, nowa_definicja, slownik):
    if slowo in slownik:
        slownik[slowo] = nowa_definicja
        print(f'Zaktualizowano wpis: {slowo} - {nowa_definicja}')
    else:
        print(f'Brak wpisu o nazwie {slowo} w słowniku')

def usun_wpis(slowo, slownik):
    if slowo in slownik:
        del slownik[slowo]
        print(f'Usunięto wpis: {slowo}')
    else:
        print(f'Brak wpisu o nazwie {slowo} w słowniku')

def wypisz_słownik(slownik):
    print("--------- SŁOWNIK ---------")
    for slowo, definicja in slownik.items():
        print(f'{slowo} - {definicja}')

##main.py?

slownik = {
    "A": "symbol jednostki prądu elektrycznego amper"
}

while True:
    print("1. Dodaj wpis")
    print("2. Edytuj wpis")
    print("3. Usuń wpis")
    print("4. Wyświetl słownik")
    print("5. Wyjście")

    wybor = input("Wybierz opcję (1-5): ")

    if wybor == '1':
        slowo = input("Podaj słowo: ")
        definicja = input("Podaj definicję: ")
        dodaj_wpis(slowo, definicja, slownik)

    elif wybor == '2':
        slowo = input("Podaj słowo do edycji: ")
        nowa_definicja = input("Podaj nową definicję: ")
        edytuj_wpis(slowo, nowa_definicja, slownik)

    elif wybor == '3':
        slowo = input("Podaj słowo do usunięcia: ")
        usun_wpis(slowo, slownik)

    elif wybor == '4':
        wypisz_słownik(slownik)

    elif wybor == '5':
        print("Dziękujemy za skorzystanie ze słownika. Do widzenia!")
        break

    else:
        print("Nieprawidłowy wybór. Wybierz liczbę od 1 do 5.")
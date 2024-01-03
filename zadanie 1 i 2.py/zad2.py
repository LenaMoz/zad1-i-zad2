def inf(lst: list) -> None:
    for ksiazka in lst:
        print(f"Książka: {ksiazka}")
    print("---" * 10)

def edycja_listy(lst):
    while True:
        inf(lst)
        print('d - dodaj książkę')
        print('u - usuń książkę')
        print('w - wyjdź z edycji listy')
        inp = input().lower()
        
        if inp == 'd':
            nowa_ksiazka = {
                "nazwa": input("Podaj nazwę książki: "),
                "liczbaStron": int(input("Podaj liczbę stron: ")),
                "Autor": input("Podaj autora książki: ")
            }
            lst.append(nowa_ksiazka)
            print('Książka dodana')
        elif inp == 'u':
            numer_ksiazki = int(input("Podaj numer książki do usunięcia: "))
            if 1 <= numer_ksiazki <= len(lst):
                del lst[numer_ksiazki - 1]
                print(f'Książka numer {numer_ksiazki} usunięta')
            else:
                print("Nieprawidłowy numer książki.")
        elif inp == 'w':
            break
        else:
            print("Nie ma takiej komendy")

biblioteka = []
ksiazki = [
    {"nazwa": "Harry Potter i Kamień Filozoficzny", "liczbaStron": 328, "Autor": "J.K. Rowling"}
]

while True:
    print("===" * 25)
    print("w - wyjdź z programu")
    print("i - informacje o książkach")
    print("ed - edytuj dane")
    print("===" * 25)
    inp = input().lower()
    
    if inp == 'w':
        break
    elif inp == 'i':
        inf(ksiazki)
    elif inp == 'ed':
        edycja_listy(ksiazki)
    else:
        print("Nieprawidłowa komenda. Spróbuj ponownie.")

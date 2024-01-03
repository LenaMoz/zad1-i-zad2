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

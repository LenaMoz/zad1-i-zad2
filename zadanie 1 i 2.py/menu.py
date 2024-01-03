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

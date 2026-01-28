def vis_meny():
    print("1) legg til tall")
    print("2) vis sum")
    print("q) avslutt")

tall_liste = []

while True:
    vis_meny()
    valg = input("Velg: ").strip().lower()

    if valg == "1":
        try:
            t = int(input("tall: "))
            tall_liste.append(t)
        except ValueError:
            print("Det var ikke et gyldig tall. Prøv igjen.")
    elif valg == "2":
        print(f"Summen av tallene er: {sum(tall_liste)}")
    elif valg == "q":
        print("Avslutter programmet.")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")
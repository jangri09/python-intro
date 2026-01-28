def vis_meny():
    print("1) plus")
    print("2) minus")
    print("3) gange")
    print("4) dele")
    print("q) avslutt")



while True:
    try:
        tall1 = float (input("skriv et tall: "))
        tall2 = float (input("skriv et tall: "))
    except ValueError:
        print("Ugyldig tall. Prøv igjen.")
        continue
    vis_meny()
    valg = input("Velg: ").strip().lower()
    if valg == "1":
        print(f"summen av tallene er: {(tall1 + tall2)}")
    elif valg == "2":
        print(f"Summen av tallene er: {(tall1 - tall2)}")
    elif valg == "3":
        print(f"summen av tallene er: {(tall1 * tall2)}")
    elif valg == "4":
        if tall2 != 0:
            print(f"summen av tallene er: {(tall1 / tall2)}")
        else:
            print("Kan ikke dele med null.")
    elif valg == "q":
        break
    else:
        print("Ugyldig valg. Prøv igjen.")
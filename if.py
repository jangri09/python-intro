while True:
    alder = int(input("Skriv inn alderen din: "))
    if alder < 6:
        print("Du får gratis inngang.")
    elif alder < 18:
        print("Du er mindreårig")
    elif alder >= 67:
        print("unc!")
    else:
        print("Du må betale full pris.")


while True:
    try:
        tall = int(input("Skriv inn et heltall: "))
        break
    except ValueError:
        print("Det var ikke et gyldig heltall. Prøv igjen.")

print(f"Du skrev inn tallet: {tall}")
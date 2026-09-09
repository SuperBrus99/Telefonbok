telefonbok = []

person1 = {
    "navn": "Ola",
    "nummer": "12345678"
}

person2 = {
    "navn": "Kari",
    "nummer": "87654321"
}

telefonbok.append(person1)
telefonbok.append(person2)


def vis_alle():
    for person in telefonbok:
        print(person["navn"] + ": " + person["nummer"])


def legg_til():
    navn = input("Skriv inn navn: ")
    nummer = input("Skriv inn nummer: ")

    ny_person = {
        "navn": navn,
        "nummer": nummer
    }

    telefonbok.append(ny_person)
    print(f"{navn} ble lagt til i telefonboka.")


while True:
    print("\n--- TELEFONBOK ---")
    print("1. Vis alle")
    print("2. Legg til ny")
    print("3. Søk")
    print("4. Avslutt")

    valg = input("Skriv inn 1, 2, 3 eller 4: ")

    if valg == "1":
        vis_alle()

    elif valg == "2":
        legg_til()

    elif valg == "3":
        print("Søk er ikke laget ennå.")

    elif valg == "4":
        print("Programmet avsluttes.")
        break

    else:
        print("Ugyldig valg. Skriv inn 1, 2, 3 eller 4.")


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
vis_alle()
legg_til()

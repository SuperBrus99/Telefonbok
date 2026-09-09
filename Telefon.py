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

vis_alle()

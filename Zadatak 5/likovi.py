
class Kruznica:

    def __init__(self, radijus):
        self.radijus = radijus

    def __str__(self):
        radijus = self.radijus
        return "Kruznica radijusa {:0.2f}".format(radijus)


class Kvadrat:
    def __init__(self, stranica):
        self.stranica = stranica

    def __str__(self):
        stranica = self.stranica
        return "Kvadrat stranice {:0.2f}".format(stranica)


if __name__ == "__main__":
    print('*** test likovi ***')
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)
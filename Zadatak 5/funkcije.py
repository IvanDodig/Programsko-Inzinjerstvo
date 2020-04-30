import likovi
from math import pi


def opseg(lik):
    if(isinstance(lik, likovi.Kruznica)):
        return f"Opseg je { 2 * lik.radijus * pi}"
    if(isinstance(lik, likovi.Kvadrat)):
        return f"Opseg je {4 * lik.stranica}"


def povrsina(lik):
    if(isinstance(lik, likovi.Kruznica)):
        return f"Povrsina je { pow(lik.radijus, 2) * pi}"
    if(isinstance(lik, likovi.Kvadrat)):
        return f"Povrsina je {pow(lik.stranica, 2)}"


if __name__ == '__main__':
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)

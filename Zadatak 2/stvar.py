'''

Napravi klasu Stvar koja će imati statički atribut broj_stvari.
Napravi __init__() od klase Stvar u kojem će se broj_stvari povećati za jedan.
Napravi specijalnu medotu __del__() od klase Stvar u kojem će se broj_stvari smanjiti za jedan.
'''
class Stvar(object):

    broj_stvari = 0

    def __init__(self):
        Stvar.broj_stvari += 1
    
    def __del__(self):
        Stvar.broj_stvari -= 1

print('*** test 1 ***')
s1 = Stvar()
s2 = Stvar()
s3 = s2
print(Stvar.broj_stvari)
del(s2)
print(Stvar.broj_stvari)
del(s3)
print(Stvar.broj_stvari)
del(s1)
print(Stvar.broj_stvari)
from fractions import Fraction

class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    #getteri i setteri
    @property
    def brojnik(self):
        return self._brojnik

    @property
    def nazivnik(self):
        return self._nazivnik

    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value

    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik = value
    
    #metoda koja vraca prirodni broj radi usporedbe razlomka
    @property
    def prirodniBroj(self):
        return float(self._brojnik)/float(self._nazivnik)

    #specijalne metode za ispis citljiv covjeku    
    def __str__(self):
        return  str(self._brojnik) + '|' + str(self._nazivnik)
    
    def __repr__(self):
        return "Razlomak("+repr(self._brojnik) + ',' + repr(self._nazivnik) + ")"

    #metode usporedbe
    def __eq__(self, other):
        return self.prirodniBroj == other.prirodniBroj

    def __lt__(self,other):
        return self.prirodniBroj < other.prirodniBroj

    def __le__(self,other):
        return self.prirodniBroj <= other.prirodniBroj

    #skracivanje razlomka
    def skrati(self):
        a = Fraction(self._brojnik,self._nazivnik)
        self._brojnik = a.numerator
        self._nazivnik = a.denominator

    #spec metoda za zbrajanje 
    def __add__(self, other):
        naz = self._nazivnik * other._nazivnik
        prviBro = (naz/self._nazivnik) * self._brojnik
        drugiBro = (naz/other._nazivnik) * other._brojnik
        bro = prviBro + drugiBro
        return str(bro) + '|' + str(naz)

    #spec metoda za oduzimanje 
    def __sub__ (self,other):
        naz = self._nazivnik * other._nazivnik
        prviBro = (naz/self._nazivnik) * self._brojnik
        drugiBro = (naz/other._nazivnik) * other._brojnik
        bro = prviBro - drugiBro
        return str(bro) + '|' + str(naz)

    #spec metoda za mnozenje
    def __mul__ (self,other):
        naz = self._nazivnik * other._nazivnik
        bro = self._brojnik * other._brojnik
        return str(bro) + '|' + str(naz)

    #spec metoda za dijeljenje 
    def __truediv__(self,other):
        naz = self._nazivnik * other._brojnik
        bro = self._brojnik * other._nazivnik
        return str(bro) + '|' + str(naz)




print('*** test 1 ***')
r1 = Razlomak(12,30)
print(r1.brojnik, r1.nazivnik)
r1.skrati()
print(r1.brojnik, r1.nazivnik)

print('*** test 2 ***')
r1 = Razlomak(12,30)
r2 = Razlomak(2,5)
r3 = Razlomak(3,6)
print(r1,r2,repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(3,4)+Razlomak(5,2))
print(Razlomak(1,3)-Razlomak(2,6))
print(Razlomak(2,8)*Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))
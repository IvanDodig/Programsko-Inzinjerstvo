class Polje(object):

    def __init__(self, broj = 0):
        self.__broj = broj
    
    @property
    def broj(self):
        return self.__broj

    @broj.setter
    def broj(self,broj):
        self.__broj = broj
    
    @property
    def jeBroj(self):
        if self.__broj != 0:
            return True
        else:
            return False
    
    @property
    def jePrazno(self):
        if self.__broj == 0:
            return True
        else:
            return False

    def __str__(self):
        if self.__broj == 0:
            return '.'
        else:
            return str(self.__broj)

    def __repr__(self):
        return self.__class__.__name__ + '(%r)' % (self.__broj)
    
    def __eq__(self,other):
        if isinstance(other, Polje):
            if self.__broj == other.__broj:
                return True
            else:
                return False
        else:
            return False

print('*** test 2 ***')
polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 12)]
for p in polja:
    print(repr(str(p)), repr(p))
print()
polja = [Polje(0)] + [Polje(2**broj) for broj in range(1, 3)]
elementi = [2, Polje(2), 3, Polje(3)]
for el in elementi:
    for p in polja:
        print('%r %r %s' % (el, p, el == p))
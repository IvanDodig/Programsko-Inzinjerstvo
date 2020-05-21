class Polje(object):

    def __init__(self, broj = 0):
        self.__broj = broj
    
    @property
    def vratiBroj(self):
        return self.__broj
    
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
            return ' '
        else:
            return str(self.__broj)

    def __repr__(self):
        return self.__class__.__name__ + '(%r)' % (self.__broj)

print('*** test 2 ***')
polja = [Polje(broj) for broj in range(9)]
for p in polja:
    print(repr(str(p)), repr(p))

class Kvadrat(object):

    def __init__(self, broj = 0):
        self.__broj = broj
        self.__otkriven = False
        self.__oznacen = False
    
   
    def otkrij(self):
        if self.__oznacen == False:
            self.__otkriven = True
    
   
    def oznaci(self):
        if self.__otkriven == False:
            if self.__oznacen == False:
                self.__oznacen = True
            else:
                self.__oznacen = False
    
    @property
    def jeBroj(self):
        if self.__broj > 0:
            return True
        else:
            return False
    
    @property
    def jeMina(self):
        if self.__broj == -1:
            return True
        else:
            return False

    @property
    def jePrazan(self):
        if self.__broj == 0:
            return True
        else:
            return False

    def __str__(self):
        if self.__oznacen:
            return '?'
        elif self.__otkriven == False:
            return '.'
        elif self.__otkriven and self.jeMina:
            return 'x'
        elif self.__otkriven and self.jeBroj:
            return str(self.__broj)
        elif self.__otkriven and self.jePrazan:
            return ' '


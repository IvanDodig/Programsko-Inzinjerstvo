
from math import pow

class Trokut(object):

    def __init__(self,a,b,c):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c:
            raise Exception("Nije trokut")
        else:
            self.__stranice = (a,b,c)
    
    def __repr__(self):
        return "Trokut" + str(self.__stranice) 

    def __str__(self):
        return "trokut " + " ".join([str(i) for i in self.__stranice])

    def opseg(self):
        a = self.__stranice[0]
        b = self.__stranice[1]
        c = self.__stranice[2]

        return float(a + b + c)

    def povrsina(self):
        a = float(self.__stranice[0])
        b = float(self.__stranice[1])
        c = float(self.__stranice[2])
        s = float(self.opseg() / 2)
        pov = (s-a)*(s-b)*(s-c)
        return  pow(pov,0.5)


class JednakokracniTrokut(Trokut):

    def __init__(self,krak,baza):
        super(JednakokracniTrokut, self).__init__(krak,krak,baza)

class JednakostranicniTrokut(Trokut):

    def __init__(self,stranica):
        super(JednakostranicniTrokut, self).__init__(stranica,stranica,stranica)


print('*** test 1 ***')
lista_stranica = [(1,2,3),(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
    try:
        t = Trokut(*stranice)
        print(repr(t))
    except Exception as e:
        print(e, stranice) 

print('*** test 2 ***')
lista_stranica = [(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
    t = Trokut(*stranice)
    print('%r ima opseg %.3f i povrsinu %.3f' % (t, t.opseg(), t.povrsina()))


print('*** test 3 ***')
trokuti = [Trokut(3,4,5),JednakokracniTrokut(3,4),JednakostranicniTrokut(5)]
for t in trokuti:
    print(t)
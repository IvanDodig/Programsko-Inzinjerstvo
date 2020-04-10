import bisect

class MultiSkup(object):

    def __init__( self, skup = None ):
        self.__skup = sorted(skup)
        self.__kljucevi = []
        self.__rijecnik = {}

        if self.__skup is not None:
            for x in self.__skup:
                if x in self.__rijecnik:
                    self.__rijecnik[x] += 1
                else:
                    self.__rijecnik[x] = 1
                    self.__kljucevi.append(x)

        self.__kljucevi = sorted(self.__kljucevi)

    def __str__(self):
        djelovi = []
        for key in self.__kljucevi:
            djelovi.append("%r*%r" % (key, self.__rijecnik[key]))
        return "{{%s}}" % ", ".join(djelovi)

 

    def __iter__(self):
        return iter(self.__skup)

    def __repr__(self):
        
        return "Multiskup("+repr(self.__skup) +")"

    def add(self,num, times=1):
        for i in range(times):
            self.__skup.append(num)
            if self.__rijecnik[num] is not None:
                self.__rijecnik[num] += 1
            else:
                self.__rijecnik[num] = 1
                self.__kljucevi = num

    def remove(self, num, times=1):
        for i in range(times):
            self.__skup.remove(num)
            if self.__rijecnik[num] > 1:
                self.__rijecnik[num] -= 1
            else:
                del self.__rijecnik[num]
                self.__kljucevi.remove(num)

    
print('*** test 1 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
print(a)

print('*** test 2 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
for el in a:
 print(el)
print(repr(a))

print('*** test 3 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
a.add(4)
print(a)
a.add(2,3)
print(a)
a.remove(4,2)
print(a)
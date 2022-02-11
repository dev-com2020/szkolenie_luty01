from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc=0):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def fly(self):
        print("Tu", self.gatunek, ".Startuje i osiągnę prędkość max: ", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def __init__(self, szybkosc):
        super().__init__("Orzeł", szybkosc)

    def poluj(self):
        print("Tu", self.gatunek, ".Rozpoczynam polowanie")

    def wydajOdglos(self):
        print("PIIII!")


class Pingwin(Ptak):

    def __init__(self):
        super().__init__("Pingwin", 0)

    def slizgaj(self):
        print("Tu", self.gatunek, ".Rozpoczynam ślizganie!")

    def fly(self):
        print("Tu", self.gatunek, ". Niestety ja nie latam :(")

    def wydajOdglos(self):
        print("Pooooo!")


p2 = Orzel(55)
p2.poluj()
p2.fly()
p2.wydajOdglos()

p3 = Pingwin()
p3.slizgaj()
p3.fly()
p3.wydajOdglos()
print(p3.szybkosc)


class First:
    def f1(self):
        print("f1")


class Second(First):
    def f2(self):
        print("f2")

    def f1(self):
        print("f1")


class Third(Second):
    def f3(self):
        print("f3")


x = Third()

print(isinstance(x, Third))
print(isinstance(x, Second))
print(isinstance(x, First))
x.f3()
x.f2()
x.f1()

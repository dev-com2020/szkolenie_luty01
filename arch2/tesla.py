class Tesla():
    """
    Klasa symulująca auto Tesla
    """

    def __init__(self):
        self.__silnik = False
        self.__bieg = 0
        self.__predkosc = 0

    def uruchom(self):
        self.__silnik = True

    def wylacz(self):
        self.__silnik = False

    def __biegN(self):
        if self.__bieg <= 5: self.__bieg += 1;print(self.__bieg)

    def __biegP(self):
        if self.__bieg >= 0: self.__bieg -= 1;print(self.__bieg)

    def przyspiesz(self):
        if self.__silnik is True:
            self.__predkosc += 10
            print(self.__predkosc)
            self.__biegN()

    def hamuj(self):
        """
        Zatrzymuje samochód
        :return:
        """
        if self.__predkosc >= 10:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0
        print(self.__predkosc)
        self.__biegP()


car = Tesla()
car.uruchom()
car.przyspiesz()
car.hamuj()
car.wylacz()

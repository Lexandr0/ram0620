from abc import ABC, abstractmethod
import random


# Abstraktne klass
class Tegelane(ABC):

    def __init__(self, nimi, elu):
        self.nimi = nimi
        self._elu = elu   # kapseldamine

    def vota_kahju(self, kahju):
        self._elu -= kahju
        if self._elu < 0:
            self._elu = 0

    def on_elus(self):
        return self._elu > 0

    @abstractmethod
    def runda(self, vastane):
        pass


# Sõdalane
class Sodalane(Tegelane):

    def runda(self, vastane):
        kahju = random.randint(10, 20)
        print(self.nimi, "löb mõõgaga ja teeb", kahju, "kahju")
        vastane.vota_kahju(kahju)


# Maag
class Maag(Tegelane):

    def __init__(self, nimi, elu, mana):
        super().__init__(nimi, elu)
        self._mana = mana

    def runda(self, vastane):

        if self._mana >= 10:
            kahju = random.randint(15, 25)
            self._mana -= 10
            print(self.nimi, "kasutab maagia rünnakut ja teeb", kahju, "kahju")
        else:
            kahju = random.randint(5, 10)
            print(self.nimi, "on mana otsas ja teeb väikse rünnaku", kahju)

        vastane.vota_kahju(kahju)

        if self._mana < 0:
            self._mana = 0


# Vibukütt
class Vibukutt(Tegelane):

    def __init__(self, nimi, elu, nooled):
        super().__init__(nimi, elu)
        self._nooled = nooled

    def runda(self, vastane):

        if self._nooled > 0:
            kahju = random.randint(12, 18)
            self._nooled -= 1
            print(self.nimi, "laseb noole ja teeb", kahju, "kahju")
        else:
            kahju = random.randint(3, 6)
            print(self.nimi, "on nooltest ilma ja teeb nõrga rünnaku", kahju)

        vastane.vota_kahju(kahju)

        if self._nooled < 0:
            self._nooled = 0


# Lahingu funktsioon
def lahing(t1, t2):

    print("Lahing algab:", t1.nimi, "vs", t2.nimi)

    while t1.on_elus() and t2.on_elus():

        t1.runda(t2)
        print(t2.nimi, "elu:", t2._elu)

        if not t2.on_elus():
            print(t2.nimi, "sai surma!")
            break

        t2.runda(t1)
        print(t1.nimi, "elu:", t1._elu)

        if not t1.on_elus():
            print(t1.nimi, "sai surma!")
            break

    print("Lahing lõppes!")


# Test
t1 = Sodalane("Aragorn", 100)
t2 = Maag("Gandalf", 80, 50)

lahing(t1, t2)
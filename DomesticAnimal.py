import random

class DomesticAnimal:
    name = None # string
    gender = None # string
    age = 0
    sound = None

    def __init__(self, age, name):
        self.age = age
        self.gender = random.choice(['male', 'female'])
        self.name = name
        print(self.sound)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def __del__(self):
        print('Меня убили')

class Mammal(DomesticAnimal):
    wool = random.choice(['long', 'short', 'middle'])

    def get_wool(self):
        return self.wool

class Mammal(DomesticAnimal):
    wool = random.choice(['long', 'short', 'middle'])

    def get_wool(self):
        return self.wool

class Bird(DomesticAnimal):
    wings = True

    def is_Bird(self):
        return self.wings

class Duck(Bird):
    sound = 'Kriya-kriya-kriya!'

class Chicken(Bird):
    sound = 'Kudah-kudah!'

class Goose(Bird):
    sound = 'Ga-ga-ga!'

class Cow(Mammal):
    sound = 'Mu-mu!'

class Goat(Mammal):
    sound = 'Be-be!'

class Sheep(Mammal):
    sound = 'Ble-ble!'

class Pig(Mammal):
    sound = 'Hru-hru!'

d_1 = Duck(1, 'Didi')
print(d_1.get_name())
print(d_1.__dict__)

d_2 = Duck(2, 'Ki')
print(d_2.is_Bird())

ch_1 = Chicken(1, 'ChiChi')
print(ch_1.get_gender())

g_1 = Goose(3, 'Gigi')

c_1 = Cow(2, 'Zizi')
go_1 = Goat(3, 'Boniya')
sh_1 = Sheep(4, 'Zorro')
p_1 = Pig(2, 'Pipi')
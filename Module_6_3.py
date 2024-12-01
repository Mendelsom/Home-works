import random


class Animal:
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self, speed, _cords=[0, 0, 0]):
        self.speed = speed
        self._cords = _cords
        # super().__init__()

    def move(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self._cords[1] = self._cords[1] + self.speed * self.dy
        self._cords[0] = self._cords[0] + self.speed * self.dx

        if self.dz * self.speed < 0:
            print("It's too deep, i can't dive :(")

        self._cords[2] = self._cords[2] + self.speed * self.dz

    def get_cords(self):

        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random_n = random.randint(1, 4)
        print(f"Here are(is) {random_n} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        self.dz = dz
        self._cords[2] = self._cords[2] - (self.speed * self.dz / 2)
        return self.dz


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

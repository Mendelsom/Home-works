class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors and new_floor > 0:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('no such floor')


h1 = House("ЖК", 10)
h2 = House("cottage", 3)
h1.go_to(8)
h2.go_to(5)

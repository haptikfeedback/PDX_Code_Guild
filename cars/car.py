#car.py
class Car:
    def __init__(self, doors, color):
        self.number_of_wheels = 4
        self.num_doors = doors
        self.color_choice = color
        print("{} Wheels, {} Doors, and the Color is {}".format(self.number_of_wheels, self.num_doors, self.color_choice))


    def honk(self):
        print('honk')

#


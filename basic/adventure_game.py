# LAB: ADVENTURE GAME

from random import randint

class Creature:
    def __init__(self, name, location, health, weapon=None):
        self.name = name
        self.location = location
        self.health = health
        if not weapon:
            self.weapon = Weapon(None, randint(1, 15))
        else:
            self.weapon = weapon

    def __str__(self):
        return 'You see {} at {} with a weapon that does {} damage.'.format(self.name, self.location, self.weapon.damage)

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


class Weapon:
    def __init__(self, location, damage):
        self.location = location
        self.damage = damage

    def describe(self):
        print('This weapon deals {} damage.'.format(self.damage))


class Potion:
    def __init__(self, location, health_restored):
        self.location = location
        self.health_restored = health_restored



chris = Creature('Chris', 'Desk', 100)
chelsea = Creature("Chelsea", "Outside", 100)
new_weapon = Weapon('hall', 99)
print(chris, chelsea)

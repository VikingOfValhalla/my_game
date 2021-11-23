class Attack(object):
    def __init__(self, name, damage, energy_cost):
        self.name = name
        self.damage = damage
        self.energy_cost = energy_cost


class Weapon(object):
    def __init__(self, name, sustained_damage, attack_damage=None):
        self.name = name
        self.sustained_damage = sustained_damage
        self.attack_damage = attack_damage or []


class Tribe(object):
    def __init__(self, name, energy, attacks=None):
        self.name = name
        self.energy = energy
        self.attacks = attacks or []


class Character(object):
    def __init__(self, name, tribe, energy, attacks=None, weapons=None):
        self.name = name
        self.tribe = tribe
        self.energy = energy
        self.attacks = attacks or []
        self.weapons = weapons or []


class World(object):
    def __init__(self, name, weapon_damage, tribe_energy=None):
        self.name = name
        self.weapon_damage = weapon_damage
        self.tribe_energy = tribe_energy or []

from random import randint


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        self.attack_damage = randint(0, max_damage)

    def attack(self):
        print(self.attack_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block():
        pass


class Hero:
    def __init__(self, name, starting_health):
        self.name = name
        self.starting_health = starting_health

    def add_ability(obj):
        pass

    def attack():
        pass

    def defend(incoming_damage):
        pass

    def take_damage(damage):
        pass

    def is_alive():
        pass


if(__name__ == "__main__"):
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    ability.attack()

from random import randint


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        self.attack_damage = randint(0, max_damage)

    def attack(self):
        return self.attack_damage


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return randint(0, self.max_block)


class Hero:
    def __init__(self, name, current_health):
        self.name = name
        self.abilities = []
        self.armors = []
        self.current_health = current_health

    def add_ability(self, obj):
        return self.abilities.append(obj)

    def add_armor(self, obj):
        return self.armors.append(obj)

    def attack(self):
        attack_sum = 0
        for ability in self.abilities:
            attack_sum += ability.attack()
        return attack_sum

    def defend(self, damage_atm):
        sum_armor = 0
        for armor in damage_atm:
            sum_armor += armor.block()
        return sum_armor

    def take_damage(self, damage):
        print(damage)
        print(self.current_health)
        return self.setCurrentHealth(self.current_health - (damage - self.defend(self.armors)))

    def is_alive(self):
        if(self.current_health <= 0):
            return False
        else:
            return True

    def setCurrentHealth(self, amount):
        self.current_health = amount

    def fight(self, opponent):
        while(True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if(self.current_health <= 0):
                print("WINNER:", opponent.name)
                break
            elif(opponent.current_health <= 0):
                print("WINNER:", self.name)
                break



if(__name__ == "__main__"):
    hero1 = Hero("Wonder Woman", 200)
    hero2 = Hero("Dumbledore", 200)
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

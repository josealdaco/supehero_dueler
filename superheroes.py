from random import randint


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        pass

    def attack(self):
        return randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
        pass

    def block(self):
        return randint(0, self.max_block)


class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.kills = 0
        self.deaths = 0
        pass

    def add_ability(self, obj):
        return self.abilities.append(obj)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        pass

    def add_armor(self, obj):
        return self.armors.append(obj)

    def attack(self):
        attack_sum = 0
        for ability in self.abilities:
            attack_sum += ability.attack()
        return attack_sum

    def defend(self):
        sum_armor = 0
        for armor in self.armors:
            sum_armor += armor.block()
        return sum_armor

    def take_damage(self, damage):
        print(damage)
        print(self.current_health)
        self.setCurrentHealth(self.current_health - (damage - self.defend()))
        pass

    def is_alive(self):
        if(self.current_health <= 0):
            return False
        else:
            return True

    def add_kill(self, num_kills):
        num_kills += self.kills
        pass

    def add_deaths(self, num_deaths):
        num_deaths += self.deaths
        pass

    def setCurrentHealth(self, amount):
        self.current_health = amount
        pass

    def fight(self, opponent):
        while(True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if(self.current_health <= 0):
                print("WINNER:", opponent.name)
                opponent.kills += 1
                self.deaths += 1
                break
            elif(opponent.current_health <= 0):
                self.kills += 1
                opponent.deaths += 1
                print("WINNER:", self.name)
                break
        pass


class Weapon(Ability):
    def attack(self):
        value = self.max_damage//2
        value_2 = self.max_damage
        val3 = randint(value, value_2)
        return val3


class Team(Hero):
    def __init__(self, name):

        self.name = name
        self.heroes = []
        self.deaths = 0
        pass

    def remove_hero(self, name):
        """ Will iterate all heroes and if nothing was removed, return 0   """
        index = 0
        removed = False
        for heroes in self.heroes:
            if(name == heroes.name):
                self.heroes.pop(index)
                removed = True
            index += 1
        if(removed is False):
            return 0

    def add_armor(self, armor):
        self.armors.append(armor)

    def view_all_heroes(self):
        for heroes in self.heroes:
            print(heroes.name)

    def add_hero(self, hero):
        print("Hero name:", hero)
        self.heroes.append(hero)  # Gets hero name

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        collect = [[], []]
        num_myTeam_alive = 0
        num_opponent_alive = 0

        for my_team in self.heroes:
            if(my_team.is_alive() is True):
                collect[0].append(my_team)
        for team in other_team.heroes:
            if(team.is_alive() is True):
                collect[1].append(team)
        for ability in range(len(collect[0])):
            for ability_2 in range(len(collect[1])):
                print(len(collect[0][ability].abilities))
                if(len(collect[0][ability].abilities) == 0 and len(collect[1][ability].abilities) != 0):
                    print("Opponent automatically wins")
                    collect[0][ability].deaths += 1
                    collect[1][ability].kills += 1
                    collect[0][ability].current_health = 0
                elif(len(collect[1][ability].abilities) == 0 and len(collect[0][ability].abilities) != 0):
                    print("You automatically win")
                    collect[0][ability].kills += 1
                    collect[1][ability].deaths += 1
                    collect[1][ability].current_health = 0
                elif(len(collect[1][ability].abilities) == 0 and len(collect[0][ability].abilities) == 0):
                    print("Both teams lose")
                else:
                    while(True):
                        for team in range(len(collect[1])):
                            print(collect[1][team].is_alive())
                            if collect[1][team].is_alive() is False:
                                num_opponent_alive += 1
                        for my_team in range(len(collect[0])):
                            if(collect[0][my_team].is_alive() is False):
                                num_myTeam_alive += 1
                        if(len(collect[1]) == num_myTeam_alive):
                            break
                        elif(len(collect[1]) == num_opponent_alive):
                            break
                        collect[0][randint(0, len(collect[0]) - 1)].fight(collect[1][randint(0, len(collect[0])-1)])


        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for heroes in self.heroes:
            heroes.max_health = health

        # TODO: This method should reset all heroes health to their
        # original starting value.

    def stats(self):
        '''Print team statistics'''
        for heroes in self.heroes:
            if(heroes.deaths != 0):
                print(f"This is the K/D for {heroes.name}: ", (heroes.kills/heroes.deaths))
            else:
                print(f"This is the K/D for {heroes.name}:", heroes.kills)
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        ability = str(input("Enter ability name:"))
        ability_damage = int(input("Ability damage:"))
        return Ability(ability, ability_damage)

    def create_weapon(self):
        weapon = str(input("Enter weapon name:"))
        weapon_damage = int(input("Enter weapon damage:"))
        return Weapon(weapon, weapon_damage)

    def create_armor(self):
        armor = str(input("Enter armor name:"))
        armor_damage = int(input("Enter armor damage:"))
        return Armor(armor, armor_damage)

    def create_hero(self):
        name = input("Name for hero:")
        ability = self.create_ability()
        armor = self.create_armor()
        weapon = self.create_weapon()
        print(ability)
        obj = Hero(name)
        if(ability != "N"):
            obj.add_ability(ability)
            print("ability attached")
        if(armor != "N"):
            obj.add_armor(armor)
        if(weapon != "N"):
            obj.add_weapon(weapon)
        return obj

    def build_team_one(self):
        obj = Team("Team one")
        hero_number = int(input("How many heroes?:"))
        for x in range(hero_number):
            obj.add_hero(self.create_hero())
        self.team_one = obj
        print("Object", self.team_one)

    def build_team_two(self):
        obj = Team("Team two")
        hero_number_2 = int(input("How many heroes for team [Two]?:"))
        for x in range(hero_number_2):
            obj.add_hero(self.create_hero())
        self.team_two = obj
        print(self.team_two)

    def team_battle(self):

        while(True):
            team_one_result = 0
            team_two_result = 0

            for team in self.team_one.heroes:
                print("Teams in team one", team)
                if(team.is_alive() == False):
                    team_one_result += 1

            for team_2 in self.team_two.heroes:
                if(team_2.is_alive() == False):
                    team_two_result += 1

            if(team_one_result == len(self.team_one.heroes)):
                print("Opponent has won the battle")
                break
            elif(team_two_result == len(self.team_two.heroes)):
                print("You have one, Opponent lost")
                break

            for x in range(len(self.team_one.heroes)):
                for y in range(len(self.team_two.heroes)):
                    print(self.team_one.heroes[x])
                    self.team_one.heroes[x].fight(self.team_two.heroes[y])

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

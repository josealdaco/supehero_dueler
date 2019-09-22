from dog import Dog


class Sub_Dog(Dog):
    """ This class is a subclass of Dog and
    will inherit all methods in parent Class  """

    def __init__(self, name, breed, points):
        super().__init__(name, breed, points)

    def extra(self):
        self.points += 2


def test(obj):
    obj.bark()
    print(obj)
    print(obj.name)
    print(obj.breed)


def fight(obj_1, obj_2):
    """
        This function is used
        to show how the sub class can add more additional features
        then the parent and still having all the parent's class data
     """

    while(True):
        obj_1.points -= 1
        obj_2.points -= 1
        obj_2.extra()
        print("Dog 1 health:", obj_1.points)
        print("Dog 2 health:", obj_2.points)
        if(obj_1.points == 0):
            print("WINNER:", obj_2.name)
            break
        elif(obj_2.points == 0):
            print("WINNER:", obj_1.name)
            break


dog_name = Dog("REX", "POODLES", 100)
other_dog = Sub_Dog("Max", "Husky", 100)

fight(dog_name, other_dog)  # Remember, this dogs area fake

# sub = Sub_Dog(dog_name.getName(), dog_name.getBreed())
# sub.bark()

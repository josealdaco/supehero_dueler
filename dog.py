class Dog:
    def __init__(self, name, breed, points):
        self.name = name
        self.breed = breed
        self.points = points

    def bark(self):
        print("Woof!")

    def getName(self):
        return self.name

    def getBreed(self):
        return self.breed

    def getPoints(self):
        return self.points

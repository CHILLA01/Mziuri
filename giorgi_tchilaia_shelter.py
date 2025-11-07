class Animal:
    shelter_name = "Tavshesafari"
    total_animals = 0

    def __init__(self, name, species, health=100, hunger=0):
        self.__name = name
        self.__species = species
        self.__health = health
        self.__hunger = hunger
        Animal.total_animals += 1

    def feed(self, amount):
        self.__hunger = max(0, self.__hunger - amount)

    def play(self, time):
        self.__hunger += time * 2
        self.__health = max(0, self.__health - time)

    def check_health(self):
        print(f"{self.__name} - Health: {self.__health}, Hunger: {self.__hunger}")

    @classmethod
    def shelter_info(cls):
        print(f"Shelter: {cls.shelter_name}, Total animals: {cls.total_animals}")

    @staticmethod
    def is_healthy(health):
        return health >= 70



dog = Animal("maxoo", "Dog")
cat = Animal("jaboo", "Cat", 90, 10)

dog.feed(20)
cat.play(5)
dog.check_health()
cat.check_health()
Animal.shelter_info()
print(Animal.is_healthy(90))

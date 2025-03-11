class Car:
    def __init__(self, color, model, makeYear, fuelType):
        self.color = color
        self.model = model
        self.makeYear = makeYear
        self.fuelType = fuelType

    def sell(self):
        print(f"{self.model} ({self.makeYear}) გაყიდულია.")

    def buy(self):
        print(f"{self.model} ({self.makeYear}) შეძენილია.")

    def rent(self):
        print(f"{self.model} ({self.makeYear}) გაქირავებულია.")

    def insurance(self):
        print(f"{self.model} ({self.makeYear}) დაზღვეულია.")
car1 = Car("red", "Mercedes", 2015, "Gas")
car2 = Car("blue", "BMW", 2013, "Gas")
car3 = Car("orange", "Audi", 2009, "Diesel")

print(f"Car 1: {car1.color}, {car1.model}, {car1.makeYear}, {car1.fuelType}")
print(f"Car 2: {car2.color}, {car2.model}, {car2.makeYear}, {car2.fuelType}")
print(f"Car 3: {car3.color}, {car3.model}, {car3.makeYear}, {car3.fuelType}")
car1.sell()
car2.buy()
car3.rent()
car1.insurance()











class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = temperature


    def get_temp(self):
        return self.__temperature


    def set_temp(self, Text):
        self.__temperature = Text


    def del_temp(self):
        print("Deleting temperature")
        del self.__temperature


    temperature = property(get_temp, set_temp, del_temp)


temp1 = Celsius(25)
temp2 = Celsius(-10)

print(f"temp1: {temp1.temperature}C")
print(f"temp2: {temp2.temperature}C")
temp1.temperature = 30
print(f"temp1: {temp1.temperature}C")
del temp1.temperature



















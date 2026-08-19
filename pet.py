class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__health = 100   # private attribute

    def display_info(self):
        print(f"Pet: {self.name}, Age: {self.age}, Health: {self.__health}")

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if 0 <= value <= 100:
            self.__health = value
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Invalid health value. Must be between 0 and 100.")

    def care_action(self):
        print(f"{self.name} is being cared for.")


class Dog(Pet):
    def care_action(self):
        print(f"{self.name} enjoys a walk. Woof!")


class Cat(Pet):
    def care_action(self):
        print(f"{self.name} loves being cuddled. Meow!")


class Rabbit(Pet):
    def care_action(self):
        print(f"{self.name} hops happily after being fed. Thump!")


dog = Dog("Bruno", 5)
cat = Cat("Kitty", 3)
rabbit = Rabbit("Snowy", 2)

pets = [dog, cat, rabbit]

print("=== Pet Care Dashboard ===\n")
for pet in pets:
    pet.display_info()
    pet.care_action()
    print()

dog.set_health(85)
cat.set_health(110)   # invalid update
rabbit.set_health(95)

print("\n=== Updated Pet Health ===\n")
for pet in pets:
    pet.display_info()

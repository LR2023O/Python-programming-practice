class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name} is barking!"
    def eat(self,food):
        return f"{self.name} is eating {food}."
    def sleep(self):
        return f"{self.name} is sleeping."
    def fetch(self):
        return f"{self.name} fetched a bone."
my_dog = Dog("Buddy","Golden Retriever")
print(my_dog.bark())
print(my_dog.eat("meat"))
print(my_dog.sleep())
print(my_dog.fetch())

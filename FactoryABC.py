from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("Woof")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")

class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type =="dog":
            return Dog()
        elif animal_type=="cat":
            return Cat()
        else:
            return ValueError("Unknown animal type")
        
factory = AnimalFactory()

animal1 = factory.get_animal("dog")
animal1.speak()
                           
animal2 = factory.get_animal("cat")
animal2.speak()                           
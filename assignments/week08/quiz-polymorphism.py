"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""


class Animal:
    def move(self):
        """Generic move method (to be overridden)"""
        pass
 
class Fish(Animal):
    def move(self):
        return "The fish swims in the water."
 
class Bird(Animal):
    def move(self):
        return "The bird flies in the sky."
 
class Dog(Animal):
    def move(self):
        return "The dog runs on the ground."
  
def make_it_move(animal: Animal):
    print(animal.move())
 
 
fish = Fish()
bird = Bird()
dog = Dog()
 
make_it_move(fish) 
make_it_move(bird) 
make_it_move(dog)   
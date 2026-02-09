from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("animal is sleeping")


class Dog(Animal):
    def sound(self):
        print("dog barks")


class Cat(Animal):
    def sound(self):
        print("cat meows")


dog = Dog()
cat = Cat()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

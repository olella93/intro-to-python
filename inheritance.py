class Pet:
    def speak(self):
        print("pet is speaking")

class Dog (Pet):
    def speak(self):
        super().speak() #super() is used to call the parent class method. super means parent
        print("Dog is speaking")

class Cat (Pet):
    def speak(self):
        print("Cat is speaking")

dog1 = Dog()
dog1.speak()

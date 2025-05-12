class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am a pet."
    def speak(self):
        print("pet is speaking")

class Dog (Pet):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def speak(self):
        super().speak() #super() is used to call the parent class method. super means parent
        print("Dog is speaking")

class Cat (Pet):
    def speak(self):
        print("Cat is speaking")

dog1 = Dog("Buddy", "Brown")
print(dog1.color)
# dog1.speak()

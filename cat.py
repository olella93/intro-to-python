class Cat:
    def __init__(self, name):
        self.name = name

    def speak (self): #instance method always has the first parameter as "self"
        print("Meow!")

cat1 = Cat("Whiskers")
cat1.speak()
cat2 = Cat("Mittens")
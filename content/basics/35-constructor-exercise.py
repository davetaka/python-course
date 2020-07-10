class Person():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi, i am {self.name}")


person1 = Person("David")
person1.talk()
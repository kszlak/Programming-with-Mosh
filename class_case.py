class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print (f'Hi {self.name}')

hr_specialist = Person('John Smith')
hr_specialist.talk()

accountant = Person('Lara Tabasko')
accountant.talk()
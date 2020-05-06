class Person(object):
    def __init__(self, age):
        self.age = age

    # def drive(self):
    #     if self.age >= 18
    #         print()
    #     else:
    #         raise Exception('No Drive')

class Baby(Person):
    def __init__(self, age = 1):
        if age <= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No Drive')

class Adult(Person):
    def __init__(self, age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

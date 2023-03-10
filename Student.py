from Homework.Human import Human


class Student(Human):
    def __init__(self, name, age, klass, numb_school):
        super().__init__(name, age)
        self.klass = klass
        self.numb_school = numb_school
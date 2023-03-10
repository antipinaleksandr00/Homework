from Homework.Human import Human


class Director(Human):

    def __init__(self, name, age, numb_school):
        super().__init__(name, age)

        self.numb_school = numb_school
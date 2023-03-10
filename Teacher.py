from Homework.Director import Director
from Homework.Human import Human


class Teacher(Director, Human):

    def __init__(self, name, age, numb_school, lesson):
        super().__init__(name, age, numb_school)
        self.lesson = lesson

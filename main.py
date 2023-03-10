from Homework.Director import Director
from Homework.Student import Student
from Homework.Teacher import Teacher

director_1 = Director("Игорь", 35, 157)
print(f"Учитель и директор : {director_1.name}", end=' ')
print(f"{director_1.age} лет", end=' ')
print(f"{director_1.numb_school} школы")


teacher_1 = Teacher("Игорь", 35, 157, "математике")
print(f"Учитель и директор : {teacher_1.name}", end=' ')
print(f"{teacher_1.age} лет", end=' ')
print(f"{teacher_1.numb_school} школы", end=' ')
print(f"по {teacher_1.lesson}")


teacher_2 = Teacher("Павел", 29, 157, "технологии")
print(f"Учитель : {teacher_2.name}", end=' ')
print(f"{teacher_2.age} лет", end=' ')
print(f"{teacher_1.numb_school} школы", end=' ')
print(f"по {teacher_2.lesson}")

student_1 = Student("Миша", 15, 157, 9)
print(f"Ученик : {student_1.name}", end=' ')
print(f"{student_1.age} лет", end=' ')
print(f"{student_1.numb_school} школы", end=' ')
print(f"{student_1.klass} класса ")
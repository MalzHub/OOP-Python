class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
        self.semester = 6

    def show_details(self):
        super().show_details()
        print(f"Course is: {self.course}")
        print(f"Semester is: {self.semester}")

stud1 = Student("Malavika", 23, "B.Tech CSE")
stud1.show_details()

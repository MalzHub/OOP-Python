class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name              # public
        self._roll_no = roll_no       # protected
        self.__grade = grade          # private

    def update_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print(f"Grade updated to: {self.__grade}")
        else:
            print("Invalid grade! Must be between 0 and 100.")

    def get_grade(self):
        return self.__grade

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self._roll_no}")
        print(f"Grade: {self.__grade}")

s1 = Student("Malavika", 101, 85)

print(s1.name)          
print(s1._roll_no)       

print("Grade:", s1.get_grade())

s1.update_grade(92)
print("Updated Grade:", s1.get_grade())

s1.display_details()

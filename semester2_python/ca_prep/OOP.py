class Person:
    def __init__(self, name, email, password):
        self.name = name  # Public attribute
        self._email = email  # Protected attribute
        self.__password = password  # Private attribute

    def get_infor(self):
        return f"Name: {self.name}, Email:{self._email}"


class Student(Person):  # Inheritance
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)  # Call parent constructor
        self.student_id = student_id

    def get_infor(self):  # Method overriding
        return f"Student ID: {self.student_id}, Name: {self.name}, Email:{self._email}"

class Teacher(Person): # Inheritance
    def __init__(self, name, email, password, subject): # Constructor
        super().__init__(name, email, password) # Call parent constructor
        self.subject = subject

    def get_infor(self): # Method overriding
        return f"Subject: {self.subject}, Name: {self.name}, Email:{self._email}"



def show_info(person): # Polymorphism
    print(person.get_infor())

    if isinstance(person, Student):
        print("This is a student.")
    elif isinstance(person, Teacher):
        print("This is a teacher.")

def main():
    person = Person("Alice", "alice@gmail.com", "pass123")
    student = Student("Bob", "bob@gmail.com"," student123", "S12345")
    teacher = Teacher("Charlie", "charlie@gmail.com", "teach123", "Math")

    show_info(person)
    show_info(student)
    show_info(teacher)

main()

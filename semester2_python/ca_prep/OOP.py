"""
1. Inheritance allows one class to reuse the properties and methods of another class.
2. Encapsulation means hiding sensitive data and controlling access using getters and setters.
3. Polymorphism allows different classes to implement the same method but behave differently.
4. Abstraction means exposing only essential features and hiding complex implementation details.
5. Method Overriding allows a subclass to provide a specific implementation of a method already defined in its superclass.
6. Method Overloading allows a class to have multiple methods with the same name but different parameters (not natively supported in Python).
7. Constructors are special methods called when an object is instantiated, typically used to initialize attributes.
8. Destructors are special methods called when an object is about to be destroyed, used for cleanup activities.
9. Access Modifiers control the visibility of class members: public age (accessible from anywhere), protected _age (accessible within the class and its subclasses), and private __age (accessible only within the class).
10. Class Variables are shared across all instances of a class, while Instance Variables are unique to each instance.
11. Static Methods belong to the class rather than any instance and can be called without creating an object of the class.
12. Class Methods are methods that operate on the class itself rather than on instances, and they are defined using the @classmethod decorator.
13. The super() function is used to call methods from a parent class in a subclass, facilitating code reuse and method overriding.
14. The isinstance() function checks if an object is an instance of a specific class or a subclass thereof.
15. The hasattr() function checks if an object has a specific attribute or method.
"""

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
        return f"Student ID: {self.student_id}, Name: {self.name}, Email:{self._email}, Student Id: {self.student_id}"

class Teacher(Person): # Inheritance
    def __init__(self, name, email, password, subject): # Constructor
        super().__init__(name, email, password) # Call parent constructor
        self.subject = subject

    def get_infor(self): # Method overriding
        return f"Subject: {self.subject}, Name: {self.name}, Email:{self._email}, Subject: {self.subject}"



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
    has = hasattr(teacher, 'name')
    print("Has attribute 'name':", has)


main()


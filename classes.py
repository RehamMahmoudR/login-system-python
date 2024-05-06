import random

database = []


class Admin:
    def __init__(self, identity, age, name, lastname, department, email, password, city, date):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.dep = department
        self.identity = identity
        self.email = email
        self.password = password
        self.city = city
        self.date = date

    def addStudent(self, name, lastname, age, level, faculty, identity):
        database.append(name)
        database.append(age)
        database.append(level)
        database.append(faculty)
        database.append(identity)
        database.append(lastname)
        e_mail = name[0] + '.' + lastname + "@su.edu.eg"
        password = ''
        for i in range(7):
            value = random.randint(0, 9)
            password += str(value)

    def updateStudent(self, email, identity):
        check = email in database
        # view info

    def deleteStudent(self, email, identity):
        check = email in database
        if email in database:
            print("keep student")
        else:
            print("student will be deleted.")


class Student:
    def __init__(self, name, lastname, age, faculty, level, identity, ):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.faculty = faculty
        self.level = level
        self.identity = identity

    def viewInfo(self):
        return f'''Your name is {self.name}, and your age is {self.age}. You are in faculty of {self.faculty} in level
        {self.level}. Id is {self.identity}'''

    # def view schedule
    # def view grade report

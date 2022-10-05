class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def show(self):
        print(f"name: {self.name}")
        print(f"branch: {self.branch}")


class Programmer(Student):
    def __init__(self, name, branch, course, clg):
        super().__init__(name, branch)
        self.course = course
        self.clg = clg

    def show(self):
        super().show()
        print(f"course : {self.course}")
        print(f"clg : {self.clg}")

s = Programmer("ben", "CSE", "data science", "mysori university")
s.show()
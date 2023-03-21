"""
* Project Name : Data Structure and Algorithms Lab02.6
* Program Description :
* - student class
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import random


class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGrade(self):
        return self.grade

    def __repr__(self):
        return "({}, {}, {})".format(self.id, self.name, self.grade)


def main():
    s1 = Student(20152041, "kim", 3.7)
    s2 = Student(20171132, "ahn", 3.2)
    s3 = Student(20191234, "cho", 3.3)
    li = [s1, s2, s3]
    print(sorted(li, key=lambda x: x.getId()))


if __name__ == "__main__":
    main()

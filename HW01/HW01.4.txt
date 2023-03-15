"""
* Project Name : Data Structure and Algorithms HW01.4
* Program Description :
* - class Rectangle
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        s = "좌측 하단: ({}, {}), ".format(self.x, self.y)
        s += "너비와 높이: ({} * {})".format(self.width, self.height)
        return s

    def __gt__(self, other):
        if self.width * self.height > other.width * other.height:
            return True
        else:
            return False

    def overlap(self, other):
        r1 = [self.x, self.y, self.x + self.width, self.y + self.height]
        r2 = [other.x, other.y, other.x + other.width, other.y + other.height]
        return not(r1[2] <= r2[0] or r1[0] >= r2[2] or r1[1] >= r2[3] or r1[3] <= r2[1])

def main():
    r1 = Rectangle(0, 10, 10, 10)
    r2 = Rectangle(5, 5, 10, 5)
    print(r1)
    print(r2)
    print("r1 < r2?", r1 > r2)
    print("r1과 r2가 겹치는가?", "네"if r1.overlap(r2) else "아니오")


if __name__ == "__main__":
    main()

"""
* Project Name : Data Structure and Algorithms Lab02.5
* Program Description :
* - squareEvenList
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import random


def squareEvenList(l):
    return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, l)))


def main():
    l1 = list(range(1, 10))
    l2 = list(range(1, 50, 5))
    print(squareEvenList(l1))
    print(squareEvenList(l2))


if __name__ == "__main__":
    main()

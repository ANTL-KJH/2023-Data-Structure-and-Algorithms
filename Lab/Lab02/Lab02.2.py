"""
* Project Name : Data Structure and Algorithms Lab02.2
* Program Description :
* - calc perimeter
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import math


def get_peri(radius=5.0):
    return 2 * math.pi * radius


def main():
    print(get_peri())


if __name__ == "__main__":
    main()

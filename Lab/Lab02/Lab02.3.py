"""
* Project Name : Data Structure and Algorithms Lab02.3
* Program Description :
* - find max data
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import math


def max_data(*args):
    return max(args)


def main():
    print(max_data(1, 2))
    print(max_data(1, 3, 2))
    print(max_data(1, 4, 5, 2))


if __name__ == "__main__":
    main()

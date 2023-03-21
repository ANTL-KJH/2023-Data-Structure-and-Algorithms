"""
* Project Name : Data Structure and Algorithms Lab02.4
* Program Description :
* - make otp
* ==========================================================================
* Program History
* ==========================================================================
* Author            Date            Version     Modifications
* JH KIM            2023.03.14      v1.0        FirstWrite
"""
import random


def makeOTP(s):
    L = [random.choice(s) for _ in range(6)]
    return "".join(L)


def main():
    s = "abcdefghijklnmopqrstuvwxyz0123456789"
    print(makeOTP(s))


if __name__ == "__main__":
    main()
